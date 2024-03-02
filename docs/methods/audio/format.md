# GET /audio/volume

Response:

```json
{
  "channels": "2.0",
  // Seen values: Dolby Digital, LPCM
  "format": "Dolby Digital",
  // Seen values: AUDIO_FORMAT_AC3, AUDIO_FORMAT_PCM
  "type": "AUDIO_FORMAT_AC3"
}
```

In case of no signal:

```json
{
  "channels": "0.1",
  "format": "LPCM",
  "type": "AUDIO_FORMAT_PCM"
}
```
