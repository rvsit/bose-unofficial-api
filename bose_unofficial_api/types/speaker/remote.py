from typing import TypedDict


class GetRemote(TypedDict):
    macAddr: str
    name: str
    pairingState: str
    version: str
