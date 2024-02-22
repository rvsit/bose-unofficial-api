### Example error:

```json
{
  "header": {
    "device": "<uuid>",
    "resource": "/system/error",
    "method": "NOTIFY",
    "version": 2.0,
    "status": 500
  },
  "error": {
    "GUID": "1",
    "code": 0,
    "subcode": 2005,
    "message": "Caught protobuf::FatalException - CHECK failed: IsInitialized(): Message of type \"FrontDoor.msg\" is missing required fields: header.device"
  }
}
```
