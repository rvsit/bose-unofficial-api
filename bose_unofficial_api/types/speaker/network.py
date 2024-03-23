from typing import TypedDict


class GetWiFiStatus(TypedDict):
    frequencyKhz: int
    signalDbm: int
    signalDbmLevel: str
    ssid: str
    state: str
