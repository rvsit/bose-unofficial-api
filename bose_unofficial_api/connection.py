import asyncio
import json
import logging
import ssl
import uuid
from asyncio import Future
from typing import Dict, Optional

import websockets

from bose_unofficial_api.event.sender import Sender


class BoseWebsocketConnection:
    def __init__(self, ip_address: str, jwt_token: str, log_messages=False):
        self.device_guid: Optional[str] = None
        self._ip_address = ip_address
        self._log_messages = log_messages
        self._jwt_token = jwt_token
        # Bose apps seem to use something called a "clientIdentifierPrefix"
        # format: ?product=<prefix>:<uuid>
        # uuid is just a random one, seems to change with restart
        self._ws_url = f"wss://{ip_address}:8082?product=unofficial_api:{uuid.uuid4()}"
        self._websocket: websockets.WebSocketClientProtocol = None
        self._req_id = 1  # Initialize reqID
        self._pending_requests: Dict[int, Future] = {}  # To store pending requests
        self._is_running = False
        self._notify_sender = Sender()

    async def connect(self) -> None:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        self._websocket = await websockets.connect(
            self._ws_url, ssl=ssl_context, subprotocols=["eco2"]
        )
        self._is_running = True

        connection_ready_future = Future()  # To store the pending ready message

        # Start listening for messages
        asyncio.create_task(self.listen_for_messages(connection_ready_future))

        if self._log_messages:
            logging.info(
                "Connected to %s, waiting for '/connectionReady'", self._ws_url
            )

        await connection_ready_future

    async def send_message(self, method: str, resource: str, version=1, body=None):
        self._req_id += 1  # Increment reqID
        message = {
            "header": {
                "token": self._jwt_token,
                "resource": resource,
                "msgtype": "REQUEST",
                # GET, POST, PUT
                "method": method,
                "reqID": self._req_id,
                "version": version,
                "device": self.device_guid or "",
            },
            "body": body,
        }
        await self._websocket.send(json.dumps(message))

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self._log_messages:
            logging.debug("Sent: %s", json.dumps(message))

        # Create a Future object for the response
        self._pending_requests[self._req_id] = Future()
        return self._req_id

    async def listen_for_messages(self, connection_ready_future: Future = None):
        while self._is_running:
            try:
                message = await self.receive_message()
            except websockets.exceptions.ConnectionClosedOK:
                # Requested by client so no error needs to be thrown
                logging.info("Connection closed")
            except websockets.exceptions.ConnectionClosedError as e:
                logging.warning("Connection closed error")
                raise e
            except websockets.exceptions.WebSocketException as e:
                logging.error("Websocket exception: %s", e)
                raise e

            header = message.get("header", {})
            req_id = header.get("reqID", None)

            if req_id and req_id in self._pending_requests:
                future = self._pending_requests.pop(req_id)
                future.set_result(message)
            elif header.get("method", None) == "NOTIFY":
                self.handle_notify(message, connection_ready_future)
            else:
                logging.warning("Received message with unknown reqID: %s", message)

    def handle_notify(self, message, connection_ready_future: Future = None):
        header = message.get("header", {})
        resource = header.get("resource", None)
        body = message.get("body", {})
        if self._log_messages:
            logging.info(
                'Received NOTIFY message "%s": %s',
                resource,
                body,
            )

        if resource == "/connectionReady" and connection_ready_future:
            connection_ready_future.set_result(True)

        self._notify_sender.send_message(message)

    def add_notify_observer(self, observer):
        self._notify_sender.add_observer(observer)

    async def send_and_wait(self, method: str, resource: str, version=1, body=None):
        req_id = await self.send_message(method, resource, version, body)
        future = self._pending_requests[req_id]
        return await future

    async def send_and_get_body(self, method: str, resource: str, version=1, body=None):
        response = await self.send_and_wait(method, resource, version, body)

        if response["header"]["status"] != 200:
            raise ValueError(
                f"Received {response['header']['status']} in send_and_get_body: {response}"
            )

        return response["body"]

    async def receive_message(self):
        message = await self._websocket.recv()
        message = json.loads(message)

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self._log_messages:
            logging.debug("Received: %s", json.dumps(message))

        return message

    async def close(self) -> None:
        self._is_running = False
        if self._websocket:
            if self._log_messages:
                logging.info("Closing connection to %s", self._ws_url)
            await self._websocket.close()
