# GET /system/capabilities

Response for `TAYLOR`:

```json
{
  "group": [
    {
      "apiGroup": "/featureFlag",
      "endpoints": [
        {
          "endpoint": "/featureFlag/APServer"
        },
        {
          "endpoint": "/featureFlag/bluetooth"
        },
        {
          "endpoint": "/featureFlag/diagfileservice"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Bluetooth",
      "endpoints": [
        {
          "endpoint": "/bluetooth/aclConnectionStatus"
        },
        {
          "endpoint": "/bluetooth/deviceMode"
        },
        {
          "endpoint": "/bluetooth/le/list"
        },
        {
          "endpoint": "/bluetooth/le/pairStatus"
        },
        {
          "endpoint": "/bluetooth/le/remove"
        },
        {
          "endpoint": "/bluetooth/le/setupActivate"
        },
        {
          "endpoint": "/bluetooth/le/setupDeactivate"
        },
        {
          "endpoint": "/bluetooth/le/setupStatus"
        },
        {
          "endpoint": "/bluetooth/macAddr"
        },
        {
          "endpoint": "/bluetooth/sink/config"
        },
        {
          "endpoint": "/bluetooth/sink/connect"
        },
        {
          "endpoint": "/bluetooth/sink/connectionStatus"
        },
        {
          "endpoint": "/bluetooth/sink/delayReporting"
        },
        {
          "endpoint": "/bluetooth/sink/disconnect"
        },
        {
          "endpoint": "/bluetooth/sink/list"
        },
        {
          "endpoint": "/bluetooth/sink/macAddr"
        },
        {
          "endpoint": "/bluetooth/sink/pairable"
        },
        {
          "endpoint": "/bluetooth/sink/passthrough"
        },
        {
          "endpoint": "/bluetooth/sink/profileStatus"
        },
        {
          "endpoint": "/bluetooth/sink/remove"
        },
        {
          "endpoint": "/bluetooth/sink/status"
        },
        {
          "endpoint": "/bluetooth/source/capability"
        },
        {
          "endpoint": "/bluetooth/source/capabilitySettings"
        },
        {
          "endpoint": "/bluetooth/source/config"
        },
        {
          "endpoint": "/bluetooth/source/connect"
        },
        {
          "endpoint": "/bluetooth/source/connectionStatus"
        },
        {
          "endpoint": "/bluetooth/source/darrSetting"
        },
        {
          "endpoint": "/bluetooth/source/disconnect"
        },
        {
          "endpoint": "/bluetooth/source/list"
        },
        {
          "endpoint": "/bluetooth/source/pair"
        },
        {
          "endpoint": "/bluetooth/source/pairStatus"
        },
        {
          "endpoint": "/bluetooth/source/passthrough"
        },
        {
          "endpoint": "/bluetooth/source/quickSimpleSync"
        },
        {
          "endpoint": "/bluetooth/source/remove"
        },
        {
          "endpoint": "/bluetooth/source/scan"
        },
        {
          "endpoint": "/bluetooth/source/scanResult"
        },
        {
          "endpoint": "/bluetooth/source/status"
        },
        {
          "endpoint": "/bluetooth/source/stopScan"
        },
        {
          "endpoint": "/bluetooth/source/volume"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Bluetooth",
      "endpoints": [
        {
          "endpoint": "/bluetooth/source/profileStatus"
        }
      ],
      "version": 2.0
    },
    {
      "apiGroup": "CAPS",
      "endpoints": [
        {
          "endpoint": "/addZoneSlave"
        },
        {
          "endpoint": "/audio/volume"
        },
        {
          "endpoint": "/audio/volume/decrement"
        },
        {
          "endpoint": "/audio/volume/increment"
        },
        {
          "endpoint": "/audio/zone"
        },
        {
          "endpoint": "/audio/zone/control"
        },
        {
          "endpoint": "/audio/zone/version"
        },
        {
          "endpoint": "/content/nowPlaying"
        },
        {
          "endpoint": "/content/nowPlaying/favorite"
        },
        {
          "endpoint": "/content/nowPlaying/rating"
        },
        {
          "endpoint": "/content/nowPlaying/repeat"
        },
        {
          "endpoint": "/content/nowPlaying/shuffle"
        },
        {
          "endpoint": "/content/playbackRequest"
        },
        {
          "endpoint": "/content/selectLastSource"
        },
        {
          "endpoint": "/content/selectLastStreamingSource"
        },
        {
          "endpoint": "/content/transportControl"
        },
        {
          "endpoint": "/getZone"
        },
        {
          "endpoint": "/removeZoneSlave"
        },
        {
          "endpoint": "/setZone"
        },
        {
          "endpoint": "/startDiscoveryAdvertisement"
        },
        {
          "endpoint": "/system/sources"
        },
        {
          "endpoint": "/system/sources/status"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Cast",
      "endpoints": [
        {
          "endpoint": "/cast/settings"
        },
        {
          "endpoint": "/cast/setup"
        },
        {
          "endpoint": "/cast/teardown"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "DFService",
      "endpoints": [
        {
          "endpoint": "/dfservice/diagitemregistration"
        },
        {
          "endpoint": "/dfservice/upload"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "DataCollection",
      "endpoints": [],
      "version": 1.0
    },
    {
      "apiGroup": "Demo",
      "endpoints": [
        {
          "endpoint": "/demo"
        },
        {
          "endpoint": "/demo/chimes"
        },
        {
          "endpoint": "/demo/keyConfig"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "FrontDoor",
      "endpoints": [
        {
          "endpoint": "/network/ping"
        },
        {
          "endpoint": "/system/capabilities"
        },
        {
          "endpoint": "/system/passportAccountInfo"
        },
        {
          "endpoint": "subscription"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "FrontDoor",
      "endpoints": [
        {
          "endpoint": "/network/ping"
        },
        {
          "endpoint": "/subscription"
        },
        {
          "endpoint": "/system/capabilities"
        },
        {
          "endpoint": "/system/passportAccountInfo"
        }
      ],
      "version": 2.0
    },
    {
      "apiGroup": "HomeKit",
      "endpoints": [
        {
          "endpoint": "/homekit/info"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Lightbar",
      "endpoints": [
        {
          "endpoint": "/ui/lightbar"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Network",
      "endpoints": [
        {
          "endpoint": "/network/status"
        },
        {
          "endpoint": "/network/wifi/ap"
        },
        {
          "endpoint": "/network/wifi/profile"
        },
        {
          "endpoint": "/network/wifi/siteScan"
        },
        {
          "endpoint": "/network/wifi/status"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Passport",
      "endpoints": [
        {
          "endpoint": "/cloudSync"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "ProductActivation",
      "endpoints": [
        {
          "endpoint": "/system/activated"
        },
        {
          "endpoint": "/system/authentication"
        },
        {
          "endpoint": "/system/challenge"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "ProductController",
      "endpoints": [
        {
          "endpoint": "/audio/bass"
        },
        {
          "endpoint": "/audio/treble"
        },
        {
          "endpoint": "/system/battery"
        },
        {
          "endpoint": "/system/buttonEvent"
        },
        {
          "endpoint": "/system/event"
        },
        {
          "endpoint": "/system/factorydefault"
        },
        {
          "endpoint": "/system/info"
        },
        {
          "endpoint": "/system/language"
        },
        {
          "endpoint": "/system/power/control"
        },
        {
          "endpoint": "/system/productName"
        },
        {
          "endpoint": "/system/productSettings"
        },
        {
          "endpoint": "/system/reset"
        },
        {
          "endpoint": "/system/setup"
        },
        {
          "endpoint": "/system/state"
        },
        {
          "endpoint": "/system/timeZone"
        },
        {
          "endpoint": "/system/update/start"
        },
        {
          "endpoint": "/ui/alive"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "SASS",
      "endpoints": [
        {
          "endpoint": "/sass/error"
        },
        {
          "endpoint": "/sass/frontingRequest"
        },
        {
          "endpoint": "/sass/playRequest"
        },
        {
          "endpoint": "/sass/sassToggle"
        },
        {
          "endpoint": "/sass/stopAll"
        },
        {
          "endpoint": "/sass/stopRequest"
        },
        {
          "endpoint": "/sass/streamStatus"
        }
      ],
      "version": 2.0
    },
    {
      "apiGroup": "SystemEventService",
      "endpoints": [],
      "version": 1.0
    },
    {
      "apiGroup": "TelemetryService",
      "endpoints": [],
      "version": 1.0
    },
    {
      "apiGroup": "Unknown",
      "endpoints": [
        {
          "endpoint": "/p2j/action"
        },
        {
          "endpoint": "/voice/introspect"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Update",
      "endpoints": [
        {
          "endpoint": "/system/update/status"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "VFE",
      "endpoints": [
        {
          "endpoint": "/vfe/meters"
        },
        {
          "endpoint": "/vfe/version"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "Voice",
      "endpoints": [
        {
          "endpoint": "/voice/ready"
        },
        {
          "endpoint": "/voice/settings"
        },
        {
          "endpoint": "/voice/setup/start"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "VoicePromptsService",
      "endpoints": [
        {
          "endpoint": "/ui/ttsPrompt"
        },
        {
          "endpoint": "/ui/ttsPrompt/supportedLanguages"
        },
        {
          "endpoint": "/ui/ttsPrompt/verifyLicense"
        }
      ],
      "version": 1.0
    },
    {
      "apiGroup": "WanStatusNotify",
      "endpoints": [
        {
          "endpoint": "/network/wanStatus"
        }
      ],
      "version": 1.0
    }
  ]
}
```
