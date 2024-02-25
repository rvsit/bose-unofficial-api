from typing import TypedDict


class NotificationItem(TypedDict):
    # Example: /system/update/start
    resource: str
    # Example: 2
    # Only seen integers so far but the capabilities endpoint returns a float
    version: float


# Static variable with the default array of NotificationItems
# This is grabbed from the TAYLOR speaker, need to do more reverse engineering
# Theory is that it is derived from the "capabilities" endpoint but doesn't seem a 1-1 match
DEFAULT_SUBSCRIPTION_BODY: list[NotificationItem] = [
    {"resource": "/system/update/start", "version": 1},
    {"version": 1, "resource": "/bluetooth/sink/connect"},
    {"version": 1, "resource": "/bluetooth/sink/list"},
    {"version": 2, "resource": "/subscription"},
    {"version": 1, "resource": "/bluetooth/sink/macAddr"},
    {"version": 1, "resource": "/cast/setup"},
    {"resource": "/audio/treble", "version": 1},
    {"resource": "/audio/volume/increment", "version": 1},
    {"version": 1, "resource": "/bluetooth/source/pair"},
    {"resource": "/bluetooth/sink/remove", "version": 1},
    {"version": 1, "resource": "/cast/teardown"},
    {"resource": "/bluetooth/sink/disconnect", "version": 1},
    {"resource": "/system/setup", "version": 1},
    {"version": 1, "resource": "/bluetooth/source/status"},
    {"version": 1, "resource": "/voice/settings"},
    {"version": 1, "resource": "/content/nowPlaying/repeat"},
    {"resource": "/bluetooth/source/scan", "version": 1},
    {"resource": "/system/productSettings", "version": 1},
    {"version": 1, "resource": "/ui/ttsPrompt/supportedLanguages"},
    {"version": 1, "resource": "/network/status"},
    {"version": 1, "resource": "/system/activated"},
    {"resource": "/bluetooth/source/list", "version": 1},
    {"version": 1, "resource": "/system/update/status"},
    {"version": 1, "resource": "/content/nowPlaying/rating"},
    {"resource": "/voice/setup/start", "version": 1},
    {"version": 1, "resource": "/audio/bass"},
    {"resource": "/network/wifi/siteScan", "version": 1},
    {"version": 1, "resource": "/bluetooth/source/disconnect"},
    {"resource": "/content/transportControl", "version": 1},
    {"version": 1, "resource": "/network/wifi/profile"},
    {"version": 2, "resource": "/system/capabilities"},
    {"resource": "/bluetooth/sink/connectionStatus", "version": 1},
    {"resource": "/audio/volume/decrement", "version": 1},
    {"resource": "/bluetooth/sink/status", "version": 1},
    {"version": 1, "resource": "/network/wifi/status"},
    {"resource": "/system/power/control", "version": 1},
    {"version": 1, "resource": "/audio/volume"},
    {"version": 1, "resource": "/bluetooth/source/pairStatus"},
    {"version": 1, "resource": "/system/battery"},
    {"resource": "/cast/settings", "version": 1},
    {"version": 1, "resource": "/homekit/info"},
    {"version": 1, "resource": "/bluetooth/source/connectionStatus"},
    {"resource": "/system/challenge", "version": 1},
    {"version": 1, "resource": "/content/nowPlaying/shuffle"},
    {"resource": "/bluetooth/source/scanResult", "version": 1},
    {"resource": "/content/nowPlaying", "version": 1},
    {"version": 1, "resource": "/content/nowPlaying/favorite"},
    {"version": 1, "resource": "/system/info"},
    {"resource": "/system/reset", "version": 1},
    {"resource": "/content/playbackRequest", "version": 1},
    {"version": 1, "resource": "/bluetooth/source/volume"},
    {"version": 1, "resource": "/audio/zone"},
    {"resource": "/bluetooth/source/stopScan", "version": 1},
    {"version": 1, "resource": "/bluetooth/sink/pairable"},
    {"resource": "/system/sources", "version": 1},
    {"resource": "/cloudSync", "version": 1},
    {"resource": "/bluetooth/source/connect", "version": 1},
    {"version": 1, "resource": "/system/sources/status"},
    {"resource": "/bluetooth/source/remove", "version": 1},
]
