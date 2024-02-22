from bose_unofficial_api.connection import BoseWebsocketConnection
from bose_unofficial_api.types.speaker.audio import GetAudioFormat, GetAudioVolume
from bose_unofficial_api.types.speaker.content import GetContentNowPlaying
from bose_unofficial_api.types.speaker.system import (
    GetSystemInfo,
    GetSystemPowerControl,
    SystemPowerState,
)
from bose_unofficial_api.types.speaker.system_capabilities import (
    GetSystemCapabilities,
)


class BoseConnectionApi:
    def __init__(self, connection: BoseWebsocketConnection):
        self.connection = connection

    async def get_system_info(self) -> GetSystemInfo:
        return await self.connection.send_and_get_body("GET", "/system/info")

    async def get_system_capabilities(self) -> GetSystemCapabilities:
        return await self.connection.send_and_get_body("GET", "/system/capabilities")

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
