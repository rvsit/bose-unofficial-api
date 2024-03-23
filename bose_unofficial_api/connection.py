import asyncio
import json
import logging
import ssl
import uuid
from asyncio import Future
from typing import Dict, Optional

import websockets


class BoseWebsocketConnection:
    def __init__(self, ip_address: str, jwt_token: str, log_messages=False):
        self.ip_address = ip_address
        self.log_messages = log_messages
        self.jwt_token = jwt_token
        # Bose apps seem to use something called a "clientIdentifierPrefix"
        # format: ?product=<prefix>:<uuid>
        # uuid is just a random one, seems to change with restart
        self.ws_url = f"wss://{ip_address}:8082?product=unofficial_api:{uuid.uuid4()}"
        self.websocket: websockets.WebSocketClientProtocol = None
        self.req_id = 1  # Initialize reqID
        self.pending_requests: Dict[int, Future] = {}  # To store pending requests
        self.is_running = False
        self.device_guid: Optional[str] = None
        self.buffet: Dict[str, Future] = {}  # To store NOTIFY's on subscription

    async def connect(self) -> None:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        self.websocket = await websockets.connect(
            self.ws_url, ssl=ssl_context, subprotocols=["eco2"]
        )
        self.is_running = True

        connection_ready_future = Future()  # To store the pending ready message

        # Start listening for messages
        asyncio.create_task(self.listen_for_messages(connection_ready_future))

        if self.log_messages:
            logging.info("Connected to %s, waiting for '/connectionReady'", self.ws_url)

        await connection_ready_future

    async def send_message(self, method: str, resource: str, version=1, body=None):
        self.req_id += 1  # Increment reqID
        message = {
            "header": {
                "token": self.jwt_token,
                "resource": resource,
                "msgtype": "REQUEST",
                # GET, POST, PUT
                "method": method,
                "reqID": self.req_id,
                "version": version,
                "device": self.device_guid or "",
            },
            "body": body,
        }
        await self.websocket.send(json.dumps(message))

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self.log_messages:
            logging.debug("Sent: %s", json.dumps(message))

        # Create a Future object for the response
        self.pending_requests[self.req_id] = Future()
        return self.req_id

    async def listen_for_messages(self, connection_ready_future: Future = None):
        while self.is_running:
            try:
                message = await self.receive_message()
            except websockets.exceptions.ConnectionClosedOK:
                logging.info("Connection closed")
                exit(-1)
            except websockets.exceptions.ConnectionClosedError:
                logging.warning("Connection closed error")
                exit(-2)
            except:
                logging.warning("Connection error")
                exit(-3)
            header = message.get("header", {})
            req_id = header.get("reqID", None)

            if req_id and req_id in self.pending_requests:
                future = self.pending_requests.pop(req_id)
                future.set_result(message)
            elif header.get("method", None) == "NOTIFY":
                resource = header.get("resource", None)
                body = message.get("body", {})
                if self.log_messages:
                    logging.info(
                        'Received NOTIFY message "%s": %s',
                        resource,
                        body,
                    )
                if resource == "/connectionReady" and connection_ready_future:
                    connection_ready_future.set_result(True)
                else:
                    self.buffet[resource] = Future()
                    self.buffet[resource].set_result(body)
            else:
                logging.warning("Received message with unknown reqID: %s", message)

    async def serve_buffet(self):
        return self.buffet

    async def clear_buffet(self):
        self.buffet.clear()

    async def send_and_wait(self, method: str, resource: str, version=1, body=None):
        req_id = await self.send_message(method, resource, version, body)
        future = self.pending_requests[req_id]
        return await future

    async def send_and_get_body(self, method: str, resource: str, version=1, body=None):
        response = await self.send_and_wait(method, resource, version, body)

        if response["header"]["status"] != 200:
            raise ValueError(
                f"Received {response['header']['status']} in send_and_get_body: {response}"
            )

        return response["body"]

    async def receive_message(self):
        message = await self.websocket.recv()
        message = json.loads(message)

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self.log_messages:
            logging.debug("Received: %s", json.dumps(message))

        return message

    async def close(self) -> None:
        self.is_running = False
        if self.websocket:
            if self.log_messages:
                logging.info("Closing connection to %s", self.ws_url)
            await self.websocket.close()
