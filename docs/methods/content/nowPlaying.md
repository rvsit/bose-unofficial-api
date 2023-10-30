# GET /content/nowPlaying

## Example Responses:

#### When playing spotify

```json
{
  "header": {
    "device": "00000000-0000-0000-0000-000000000000",
    "resource": "/content/nowPlaying",
    "method": "GET",
    "msgtype": "RESPONSE",
    "reqID": 3,
    "version": 1.0,
    "status": 200,
    "token": "***"
  },
  "body": {
    "collectData": true,
    "container": {
      "capabilities": {
        "favoriteSupported": true,
        "ratingsSupported": false,
        "repeatSupported": true,
        "resumeSupported": true,
        "seekRelativeBackwardSupported": false,
        "seekRelativeForwardSupported": false,
        "shuffleSupported": true,
        "skipNextSupported": true,
        "skipPreviousSupported": true
      },
      "contentItem": {
        "containerArt": "https://i.scdn.co/image/ab67616d0000b27335001635a799837ce5892f27",
        "isLocal": true,
        "location": "/playback/container/<containerID>",
        "name": "Chill Mix",
        "presetable": true,
        "source": "SPOTIFY",
        "sourceAccount": "00000000-0000-0000-0000-000000000000",
        "type": "tracklisturl"
      }
    },
    "initiatorID": "",
    "links": {
      "moreInfo": "/more_info/np/container/<containerID>/track/<trackID>/"
    },
    "metadata": {
      "album": "Only Human (Deluxe)",
      "artist": "Calum Scott",
      "containerName": "Chill Mix",
      "duration": 260,
      "trackName": "Dancing On My Own"
    },
    "source": {
      "sourceDisplayName": "Spotify",
      "sourceID": "SPOTIFY"
    },
    "state": {
      "canFavorite": true,
      "canPause": true,
      "canRate": false,
      "canRepeat": true,
      "canSeek": true,
      "canShuffle": true,
      "canSkipNext": true,
      "canSkipPrevious": true,
      "canStop": false,
      "quality": "NOT_SET",
      "repeat": "OFF",
      "shuffle": "ON",
      "status": "PLAY",
      "timeIntoTrack": 223,
      "timestamp": "2023-10-29T18:08:02-0400"
    },
    "track": {
      "contentItem": {
        "containerArt": "https://i.scdn.co/image/ab67616d0000b273f2d671c22b70e01b78a618a8",
        "isLocal": true,
        "name": "Dancing On My Own",
        "presetable": false,
        "source": "SPOTIFY",
        "sourceAccount": "cc578309-7029-465a-926c-df25802dcaa6"
      },
      "favorite": "NO",
      "rating": "UNRATED",
      "type": "REGULAR"
    }
  }
}
```

#### When off

```json
{
  "header": {
    "device": "00000000-0000-0000-0000-000000000000",
    "resource": "/content/nowPlaying",
    "method": "GET",
    "msgtype": "RESPONSE",
    "reqID": 3,
    "version": 1.0,
    "status": 200,
    "token": "***"
  },
  "body": {
    "container": {
      "contentItem": {
        "isLocal": true,
        "presetable": false,
        "source": "INVALID_SOURCE"
      }
    },
    "source": {
      "sourceDisplayName": "INVALID_SOURCE"
    }
  }
}
```
