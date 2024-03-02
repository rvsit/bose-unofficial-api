# Subscription

The device can automatically notify the client about changes in the device state. The client can subscribe to a list of resources and the device will notify the client when the resource changes.

## PUT /subscription

Body example:

```json
{
  "notifications": [
    {
      "resource": "/system/update/start",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/sink/connect"
    },
    {
      "version": 1,
      "resource": "/bluetooth/sink/list"
    },
    {
      "version": 2,
      "resource": "/subscription"
    },
    {
      "version": 1,
      "resource": "/bluetooth/sink/macAddr"
    },
    {
      "version": 1,
      "resource": "/cast/setup"
    },
    {
      "resource": "/audio/treble",
      "version": 1
    },
    {
      "resource": "/audio/volume/increment",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/pair"
    },
    {
      "resource": "/bluetooth/sink/remove",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/cast/teardown"
    },
    {
      "resource": "/bluetooth/sink/disconnect",
      "version": 1
    },
    {
      "resource": "/system/setup",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/status"
    },
    {
      "version": 1,
      "resource": "/voice/settings"
    },
    {
      "version": 1,
      "resource": "/content/nowPlaying/repeat"
    },
    {
      "resource": "/bluetooth/source/scan",
      "version": 1
    },
    {
      "resource": "/system/productSettings",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/ui/ttsPrompt/supportedLanguages"
    },
    {
      "version": 1,
      "resource": "/network/status"
    },
    {
      "version": 1,
      "resource": "/system/activated"
    },
    {
      "resource": "/bluetooth/source/list",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/system/update/status"
    },
    {
      "version": 1,
      "resource": "/content/nowPlaying/rating"
    },
    {
      "resource": "/voice/setup/start",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/audio/bass"
    },
    {
      "resource": "/network/wifi/siteScan",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/disconnect"
    },
    {
      "resource": "/content/transportControl",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/network/wifi/profile"
    },
    {
      "version": 2,
      "resource": "/system/capabilities"
    },
    {
      "resource": "/bluetooth/sink/connectionStatus",
      "version": 1
    },
    {
      "resource": "/audio/volume/decrement",
      "version": 1
    },
    {
      "resource": "/bluetooth/sink/status",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/network/wifi/status"
    },
    {
      "resource": "/system/power/control",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/audio/volume"
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/pairStatus"
    },
    {
      "version": 1,
      "resource": "/system/battery"
    },
    {
      "resource": "/cast/settings",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/homekit/info"
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/connectionStatus"
    },
    {
      "resource": "/system/challenge",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/content/nowPlaying/shuffle"
    },
    {
      "resource": "/bluetooth/source/scanResult",
      "version": 1
    },
    {
      "resource": "/content/nowPlaying",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/content/nowPlaying/favorite"
    },
    {
      "version": 1,
      "resource": "/system/info"
    },
    {
      "resource": "/system/reset",
      "version": 1
    },
    {
      "resource": "/content/playbackRequest",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/source/volume"
    },
    {
      "version": 1,
      "resource": "/audio/zone"
    },
    {
      "resource": "/bluetooth/source/stopScan",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/bluetooth/sink/pairable"
    },
    {
      "resource": "/system/sources",
      "version": 1
    },
    {
      "resource": "/cloudSync",
      "version": 1
    },
    {
      "resource": "/bluetooth/source/connect",
      "version": 1
    },
    {
      "version": 1,
      "resource": "/system/sources/status"
    },
    {
      "resource": "/bluetooth/source/remove",
      "version": 1
    }
  ]
}
```

Responds with the same notifications list.

## Example "Notifications"

Seen variants:

`/system/battery`

```json
{
  "chargeStatus": "DISCHARGING",
  "chargerConnected": "CONNECTED",
  "minutesToEmpty": 65535,
  "minutesToFull": 65535,
  "percent": 100,
  "sufficientChargerConnected": true,
  "temperatureState": "NORMAL"
}
```

`/network/wifi/status`

```json
{
  "frequencyKhz": 5220000,
  "signalDbm": -46,
  "signalDbmLevel": "WIFI_SIGNAL_DBM_LEVEL_EXCELLENT",
  "ssid": "<REDACTED>",
  "state": "WIFI_STATION_CONNECTED"
}
```

`/system/power/control`

```json
{
  "power": "ON"
}
```

`/content/nowPlaying`

```json
{
  "collectData": true,
  "container": {
    "capabilities": {
      "favoriteSupported": true,
      "ratingsSupported": false,
      "repeatSupported": false,
      "resumeSupported": true,
      "seekRelativeBackwardSupported": false,
      "seekRelativeForwardSupported": false,
      "shuffleSupported": false,
      "skipNextSupported": false,
      "skipPreviousSupported": false
    },
    "contentItem": {
      "containerArt": "http://cdn-radiotime-logos.tunein.com/s9483g.png",
      "isLocal": true,
      "location": "/playback/station/s9483",
      "name": "NPO Radio 2",
      "presetable": true,
      "source": "TUNEIN",
      "sourceAccount": "<UUID>",
      "type": "stationurl"
    }
  },
  "initiatorID": "",
  "links": { "moreInfo": "/more_info/np/s9483" },
  "metadata": {
    "album": "",
    "artist": "Er is maar één NPO Radio 2",
    "containerName": "NPO Radio 2",
    "trackName": "NPO Radio 2"
  },
  "source": { "sourceDisplayName": "TuneIn", "sourceID": "TUNEIN" },
  "state": {
    "canFavorite": true,
    "canPause": false,
    "canRate": false,
    "canRepeat": false,
    "canSeek": false,
    "canShuffle": false,
    "canSkipNext": false,
    "canSkipPrevious": false,
    "canStop": true,
    "quality": "NOT_SET",
    "repeat": "OFF",
    "shuffle": "OFF",
    "status": "PLAY",
    "timestamp": "2024-02-24T22:09:16-0500"
  },
  "track": {
    "contentItem": {
      "containerArt": "http://cdn-radiotime-logos.tunein.com/s9483g.png",
      "isLocal": true,
      "name": "NPO Radio 2",
      "presetable": false,
      "source": "TUNEIN",
      "sourceAccount": "<UUID>"
    },
    "favorite": "NO",
    "rating": "UNRATED"
  }
}
```
