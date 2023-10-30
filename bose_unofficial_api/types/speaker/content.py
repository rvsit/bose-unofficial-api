from typing import TypedDict


class Capabilities(TypedDict, total=False):
    favoriteSupported: bool
    ratingsSupported: bool
    repeatSupported: bool
    resumeSupported: bool
    seekRelativeBackwardSupported: bool
    seekRelativeForwardSupported: bool
    shuffleSupported: bool
    skipNextSupported: bool
    skipPreviousSupported: bool


class ContentItem(TypedDict, total=False):
    containerArt: str
    isLocal: bool
    location: str
    name: str
    presetable: bool
    source: str
    sourceAccount: str
    type: str


class Container(TypedDict, total=False):
    capabilities: Capabilities
    contentItem: ContentItem


class Links(TypedDict, total=False):
    moreInfo: str


class Metadata(TypedDict):
    album: str
    artist: str
    containerName: str
    duration: int
    trackName: str


class Source(TypedDict, total=False):
    sourceDisplayName: str
    sourceID: str


class State(TypedDict, total=False):
    canFavorite: bool
    canPause: bool
    canRate: bool
    canRepeat: bool
    canSeek: bool
    canShuffle: bool
    canSkipNext: bool
    canSkipPrevious: bool
    canStop: bool
    quality: str
    repeat: str
    shuffle: str
    status: str
    timeIntoTrack: int
    timestamp: str


class Track(TypedDict, total=False):
    contentItem: ContentItem
    favorite: str
    rating: str
    type: str


class GetContentNowPlaying(TypedDict, total=False):
    collectData: bool
    container: Container
    initiatorID: str
    links: Links
    metadata: Metadata
    source: Source
    state: State
    track: Track
