from typing import Optional
from bose_unofficial_api.capabilities import SpeakerCapabilities
from bose_unofficial_api.connection import BoseWebsocketConnection
from bose_unofficial_api.api import BoseConnectionApi
from bose_unofficial_api.types.speaker import subscription


class BoseSpeaker:
    def __init__(self, ip_address: str, jwt_token: str, log_messages=False):
        self.connection = BoseWebsocketConnection(
            ip_address=ip_address, jwt_token=jwt_token, log_messages=log_messages
        )
        self.api = BoseConnectionApi(connection=self.connection)
        self.capabilities: Optional[SpeakerCapabilities] = None

    @staticmethod
    async def connect(
        ip_address: str, jwt_token: str, log_messages=False
    ) -> "BoseSpeaker":
        instance = BoseSpeaker(
            ip_address=ip_address, jwt_token=jwt_token, log_messages=log_messages
        )
        await instance.connection.connect()

        # We are setting the device GUID here because future requests expect it
        system_info = await instance.api.get_system_info()
        instance.connection.device_guid = system_info["guid"]

        # Get the capabilities of the speaker
        raw_capabilities = await instance.api.get_system_capabilities()
        instance.capabilities = SpeakerCapabilities(raw_response=raw_capabilities)

        await instance.create_subscription()

        return instance

    async def close(self):
        await self.connection.close()

    async def create_subscription(self, notifications=subscription.DEFAULT_SUBSCRIPTION_BODY):
        return await self.api.put_subscription(notifications)
