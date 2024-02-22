from typing import TypedDict


class Endpoint(TypedDict):
    # Example: "/content/nowPlaying"
    endpoint: str


class CapabilitiesGroup(TypedDict):
    # Example: "Bluetooth"
    apiGroup: str
    endpoints: list[Endpoint]
    # Example: 1.0
    version: float


class GetSystemCapabilities(TypedDict):
    group: list[CapabilitiesGroup]
