from bose_unofficial_api.connection import BoseWebsocketConnection
from bose_unofficial_api.types.speaker.audio import (
    GetAudioFormat,
    GetAudioMode,
    GetAudioSurround,
    GetAudioVolume,
)
from bose_unofficial_api.types.speaker.content import GetContentNowPlaying
from bose_unofficial_api.types.speaker.network import GetWiFiStatus
from bose_unofficial_api.types.speaker.remote import GetRemote
from bose_unofficial_api.types.speaker.subscription import NotificationItem
from bose_unofficial_api.types.speaker.system import (
    GetSystemInfo,
    GetSystemPowerControl,
    SystemPowerState,
)
from bose_unofficial_api.types.speaker.system_capabilities import GetSystemCapabilities


class BoseConnectionApi:
    def __init__(self, connection: BoseWebsocketConnection):
        self.connection = connection

    async def get_system_info(self) -> GetSystemInfo:
        return await self.connection.send_and_get_body("GET", "/system/info")

    async def get_system_capabilities(self) -> GetSystemCapabilities:
        return await self.connection.send_and_get_body("GET", "/system/capabilities", 2)

    async def get_system_power_control(self) -> GetSystemPowerControl:
        return await self.connection.send_and_get_body("GET", "/system/power/control")

    async def set_system_power_control(self, power: SystemPowerState) -> None:
        await self.connection.send_and_get_body(
            "POST", "/system/power/control", 1, {"power": power}
        )

    async def get_now_playing(self) -> GetContentNowPlaying:
        return await self.connection.send_and_get_body("GET", "/content/nowPlaying")

    async def get_audio_volume(self) -> GetAudioVolume:
        return await self.connection.send_and_get_body("GET", "/audio/volume")

    async def get_audio_format(self) -> GetAudioFormat:
        return await self.connection.send_and_get_body("GET", "/audio/format")

    async def get_audio_mode(self) -> GetAudioMode:
        return await self.connection.send_and_get_body("GET", "/audio/mode")

    async def get_audio_surround(self) -> GetAudioSurround:
        return await self.connection.send_and_get_body("GET", "/audio/surround")

    async def put_subscription(self, notifications: list[NotificationItem]) -> None:
        return await self.connection.send_and_get_body(
            "PUT", "/subscription", 2, {"notifications": notifications}
        )

    async def get_remote(self) -> GetRemote:
        return await self.connection.send_and_get_body("GET", "/remote")

    async def get_wifi_status(self) -> GetWiFiStatus:
        return await self.connection.send_and_get_body("GET", "/network/wifi/status")
