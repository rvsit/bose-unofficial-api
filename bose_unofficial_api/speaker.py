from bose_unofficial_api.connection import BoseWebsocketConnection
from bose_unofficial_api.types.speaker.audio import GetAudioFormat, GetAudioVolume
from bose_unofficial_api.types.speaker.content import GetContentNowPlaying
from bose_unofficial_api.types.speaker.system import (
    GetSystemInfo,
    GetSystemPowerControl,
    SystemPowerState,
)


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

    async def load_device_info(self) -> GetSystemInfo:
        body = await self.connection.send_and_get_body("GET", "/system/info")
        self.connection.device_guid = body["guid"]
        return body

    async def get_system_power_control(self) -> GetSystemPowerControl:
        return await self.connection.send_and_get_body("GET", "/system/power/control")

    async def set_system_power_control(self, power: SystemPowerState) -> None:
        await self.connection.send_and_get_body(
            "POST", "/system/power/control", {"power": power}
        )

    async def get_now_playing(self) -> GetContentNowPlaying:
        return await self.connection.send_and_get_body("GET", "/content/nowPlaying")

    async def get_audio_volume(self) -> GetAudioVolume:
        return await self.connection.send_and_get_body("GET", "/audio/volume")

    async def get_audio_format(self) -> GetAudioFormat:
        return await self.connection.send_and_get_body("GET", "/audio/format")
