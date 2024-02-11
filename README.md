# Bose Unofficial API

Work in progress. This is not an official API, nor affiliated with Bose.

## Development setup

```
poetry install
poetry run start
```

## Supported devices

This API has been tested with the following devices:

- Bose Portable Home Speaker (codename: `TAYLOR`)

This may work on the following devices (please report if working):

- Bose NC 700 Headphones (codename: `GOODYEAR`)
- Bose Home Speaker 500 (codename: `EDDIE`)
- Bose Soundbar 500 (codename: `PROFESSOR`)
- Bose Soundbar 700 (codename: `GINGER_CHEEVERS`)
- Bose Home Speaker 300 (codename: `FLIPPER`)
- Bose Home Speaker 450 (codename: `EDDIE_CLUB`)
- Bose Soundbar 300 (codename: `SAN_DIEGO`)
- Bose L1 Pro (codename: `FERRARI`)
- Bose L1 Pro (codename: `LOTUS`)
- Bose L1 Pro (codename: `MCLAREN`)
- Bose Smart Soundbar 900 (codename: `ANGUS`)
- Bose Zakim (codename: `ZAKIM`)
- Bose Smart Soundbar 600 (codename: `MALCOLM`)
- Bose Soundbar 550 (codename: `MALCOLM_CLUB`)

## Workings

When connected to wifi, the devices will open a secured websocket port on 8082. (`wss://<device_ip>:8082`)

### Endpoints

The following functions are available (checked if implemented):

- [x] `/system/info` (GET request, `load_device_info()`)
- [x] `/system/power/control` (GET&POST request, `get_system_power_control(), set_system_power_control(power: 'ON' | 'OFF')`)
- [x] `/content/nowPlaying` (GET, `get_now_playing()`)
- [ ] `/content/playbackRequest`
- [ ] `/homekit/info`
- [ ] `/cloudSync` (Req type pq2)
- [ ] `/audio/zone`
- [x] `/audio/volume` (GET, `get_audio_volume()`)
- [ ] `/content/transportControl` (Req type pq2)
- [ ] `/accessories`
- [ ] `/accessories/playTones`
- [ ] `/system/sources`
- [ ] `/system/sources/status`
- [ ] `/system/productSettings`
- [ ] `/clock`
- [ ] `/system/reset`
- [ ] `/bluetooth/sink/pairable`
- [ ] `/bluetooth/sink/status`
- [ ] `/system/update/status`
- [ ] `/system/update/start`
- [ ] `/bluetooth/sink/list`
- [ ] `/bluetooth/sink/connect`
- [ ] `/bluetooth/sink/disconnect`
- [ ] `/bluetooth/sink/connectionStatus`
- [ ] `/bluetooth/sink/remove`
- [ ] `/system/activated`
- [ ] `/system/challenge`
- [ ] `/system/setup`
- [ ] `/adaptiq`
- [ ] `/network/status`
- [ ] `/network/wifi/status`
- [ ] `/bluetooth/sink/macAddr`
- [ ] `/remote/integration`
- [ ] `/remote/integration/brandList`
- [ ] `/remote/integration/tvBrand`
- [ ] `/remote/integration/directEntry`
- [ ] `/remote`
- [ ] `/voice/settings`
- [ ] `/voice/setup/start`
- [ ] `/cec`
- [ ] `/content/nowPlaying/shuffle`
- [ ] `/content/nowPlaying/repeat`
- [ ] `/content/nowPlaying/rating`
- [ ] `/content/nowPlaying/favorite`
- [ ] `/subscription`
- [ ] `/audio/dualMonoSelect`
- [ ] `/audio/avSync`
- [ ] `/audio/rebroadcastLatency/mode`
- [ ] `/audio/mountOrientation`
- [ ] `/audio/eqSelect`
- [ ] `/system/power/timeouts`
- [ ] `/system/power/macro`
- [ ] `/system/power/mode/opticalAutoWake`
- [ ] `/audio/bass`
- [ ] `/audio/height`
- [ ] `/audio/format`
- [ ] `/audio/treble`
- [ ] `/audio/center`
- [ ] `/audio/surround`
- [ ] `/audio/subwooferGain`
- [ ] `/ui/lcd/brightness`
- [ ] `/audio/mode`
- [ ] `/system/battery`
- [ ] `/bluetooth/source/list`
- [ ] `/bluetooth/source/status`
- [ ] `/bluetooth/source/pair`
- [ ] `/bluetooth/source/pairStatus`
- [ ] `/bluetooth/source/connect`
- [ ] `/bluetooth/source/scan`
- [ ] `/bluetooth/source/scanResult`
- [ ] `/bluetooth/source/stopScan`
- [ ] `/bluetooth/source/connectionStatus`
- [ ] `/bluetooth/source/disconnect`
- [ ] `/bluetooth/source/remove`
- [ ] `/bluetooth/source/volume`
- [ ] `/ui/ttsPrompt/supportedLanguages`
- [ ] `/device/configuredDevices`
- [ ] `/device/configure`
- [ ] `/device/setup`
- [ ] `/device/assumed/TVs`
- [ ] `/device/assumed/sources`
- [ ] `/cast/setup`
- [ ] `/cast/settings`
- [ ] `/cast/teardown`
