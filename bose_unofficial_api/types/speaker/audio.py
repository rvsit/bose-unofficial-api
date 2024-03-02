from enum import Enum
from typing import TypedDict

class AudioProperties(TypedDict):
    maxLimit: int
    maxLimitOverride: bool
    minLimit: int
    startupVolume: int
    startupVolumeOverride: bool

class GetAudioVolume(TypedDict):
    defaultOn: int
    max: int
    min: int
    muted: bool
    properties: AudioProperties
    value: int

class GetAudioFormat(TypedDict):
    channels: str
    format: str
    type: str

class supportedPersistence(str, Enum):
    SESSION = "SESSION"
    GLOBAL = "GLOBAL"
    CONTENT_ITEM = "CONTENT_ITEM"

class GetsupportedPersistence(TypedDict):
     supportedPersistence: supportedPersistence

class GetAudioMode(TypedDict):
    persistence: supportedPersistence
    properties: object
    supportedValues: object
    value: supportedPersistence

class SurroundProperties(TypedDict):
    supportedPersistence: supportedPersistence
    max: int
    min: int
    step: int

class GetAudioSurround(TypedDict):
    persistence: supportedPersistence
    properties: SurroundProperties
    value:int