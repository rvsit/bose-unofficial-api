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


class SupportedPersistence(str, Enum):
    SESSION = "SESSION"
    GLOBAL = "GLOBAL"
    CONTENT_ITEM = "CONTENT_ITEM"


class SupportedSurroundValues(str, Enum):
    DIALOG = "DIALOG"
    NORMAL = "NORMAL"


class AudioModeProperties(TypedDict):
    # list of supportedPersistence options
    supportedPersistence: list[SupportedPersistence]
    max: int
    min: int
    step: int


class GetAudioMode(TypedDict):
    persistence: SupportedPersistence
    properties: AudioModeProperties
    value: int


class SurroundProperties(TypedDict):
    supportedPersistence: list[SupportedPersistence]
    supportedValues: list[SupportedSurroundValues]


class GetAudioSurround(TypedDict):
    persistence: SupportedPersistence
    properties: SurroundProperties
    value: SupportedSurroundValues
