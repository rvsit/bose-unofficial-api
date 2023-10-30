from connection import BoseWebsocketConnection

from bose_unofficial_api.types.speaker.system import SpeakerSystemInfo


class BoseSpeaker:
    def __init__(self, ip_address: str, jwt_token: str, log_messages=False):
        self.connection = BoseWebsocketConnection(
            ip_address=ip_address, jwt_token=jwt_token, log_messages=log_messages
        )

    @staticmethod
    async def connect(
        ip_address: str, jwt_token: str, log_messages=False
    ) -> "BoseSpeaker":
        instance = BoseSpeaker(
            ip_address=ip_address, jwt_token=jwt_token, log_messages=log_messages
        )
        await instance.connection.connect()
        return instance

    async def load_device_info(self) -> SpeakerSystemInfo:
        response = await self.connection.send_and_wait("GET", "/system/info")

        if response["header"]["status"] != 200:
            raise Exception(
                f"Received status code {response['header']['status']} when loading device info: {response}"
            )

        self.connection.device_guid = response["body"]["guid"]
        return response
