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
