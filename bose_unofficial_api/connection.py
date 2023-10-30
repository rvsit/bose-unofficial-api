import asyncio
import json
import logging
import ssl
import uuid
from asyncio import Future
from typing import Dict

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
        self.reqID = 1  # Initialize reqID
        self.pending_requests: Dict[int, Future] = {}  # To store pending requests
        self.is_running = False
        self.device_guid: str = None

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
            logging.info(f"Connected to {self.ws_url}, waiting for '/connectionReady'")

        await connection_ready_future

        await self.load_device_info()

    async def send_message(self, method: str, resource: str, body=None):
        self.reqID += 1  # Increment reqID
        message = {
            "header": {
                "token": self.jwt_token,
                "resource": resource,
                "msgtype": "REQUEST",
                # GET, POST
                "method": method,
                "reqID": self.reqID,
                "device": self.device_guid or "",
            },
            "body": body,
        }
        await self.websocket.send(json.dumps(message))

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self.log_messages:
            logging.info(f"Sent: {json.dumps(message)}")

        self.pending_requests[
            self.reqID
        ] = Future()  # Create a Future object for the response
        return self.reqID

    async def listen_for_messages(self, connection_ready_future: Future = None):
        while self.is_running:
            try:
                message = await self.receive_message()
            except websockets.exceptions.ConnectionClosedOK:
                logging.info("Connection closed")
                break
            header = message.get("header", {})
            reqID = header.get("reqID", None)

            if reqID and reqID in self.pending_requests:
                future = self.pending_requests.pop(reqID)
                future.set_result(message)
            elif header.get("method", None) == "NOTIFY":
                if (
                    header.get("resource", None) == "/connectionReady"
                    and connection_ready_future
                ):
                    connection_ready_future.set_result(True)
            else:
                logging.warning(f"Received message with unknown reqID: {message}")

    async def send_and_wait(self, method: str, resource: str, body=None):
        reqID = await self.send_message(method, resource, body)
        future = self.pending_requests[reqID]
        return await future

    async def receive_message(self):
        message = await self.websocket.recv()
        message = json.loads(message)

        if "header" in message and "token" in message["header"]:
            message["header"]["token"] = "***"

        if self.log_messages:
            logging.info(f"Received: {json.dumps(message)}")

        return message

    async def close(self) -> None:
        self.is_running = False
        if self.websocket:
            if self.log_messages:
                logging.info(f"Closing connection to {self.ws_url}")
            await self.websocket.close()

    async def load_device_info(self):
        response = await self.send_and_wait("GET", "/system/info")

        if response["header"]["status"] != 200:
            raise Exception(
                f"Received status code {response['header']['status']} when loading device info: {response}"
            )

        self.device_guid = response["body"]["guid"]
