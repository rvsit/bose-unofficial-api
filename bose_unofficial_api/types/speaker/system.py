from enum import Enum
from typing import TypedDict


class GetSystemInfo(TypedDict):
    countryCode: str
    defaultName: str
    guid: str
    limitedFeatures: bool
    name: str
    productColor: int
    productId: int
    productName: str
    productType: str
    regionCode: str
    serialNumber: str
    softwareVersion: str
    variantId: int


class SystemPowerState(str, Enum):
    OFF = "OFF"
    ON = "ON"


class GetSystemPowerControl(TypedDict):
    power: SystemPowerState  # "OFF" or "ON"
