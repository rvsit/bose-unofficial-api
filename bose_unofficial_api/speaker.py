from typing import Optional

from bose_unofficial_api.api import BoseConnectionApi
from bose_unofficial_api.capabilities import SpeakerCapabilities
from bose_unofficial_api.connection import BoseWebsocketConnection
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

    async def create_subscription(self, notifications=None):
        if notifications is None:
            notifications = subscription.DEFAULT_SUBSCRIPTION_BODY
        return await self.api.put_subscription(notifications)

    async def create_subscription_by_group(self, api_groups):
        capabilities = self.capabilities.get_groups()
        # Extracting "apiGroup" keys with their respective value and index
        all_api_groups = [
            (index, item["apiGroup"]) for index, item in enumerate(capabilities)
        ]

        # Printing the result
        notifications = []
        for index, api_group in all_api_groups:
            # print(f"Index: {index}, apiGroup: {api_group}")
            if api_group in api_groups:
                for resource in range(1, len(capabilities[index]["endpoints"])):
                    endpoint = capabilities[index]["endpoints"][resource]["endpoint"]
                    version = int(capabilities[index]["version"])
                    # print(endpoint)
                    notifications.append({"version": version, "resource": endpoint})

        return await self.api.put_subscription(notifications)
