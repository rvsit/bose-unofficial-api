from bose_unofficial_api.connection import BoseWebsocketConnection
from bose_unofficial_api.api import BoseConnectionApi


class BoseSpeaker:
    def __init__(self, ip_address: str, jwt_token: str, log_messages=False):
        self.connection = BoseWebsocketConnection(
            ip_address=ip_address, jwt_token=jwt_token, log_messages=log_messages
        )
        self.api = BoseConnectionApi(connection=self.connection)

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

        return instance

    async def close(self):
        await self.connection.close()
