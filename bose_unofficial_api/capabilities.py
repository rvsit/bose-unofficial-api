from bose_unofficial_api.types.speaker.system_capabilities import GetSystemCapabilities


class SpeakerCapabilities:
    def __init__(self, raw_response: GetSystemCapabilities) -> None:
        self.raw_response = raw_response

    def get_raw(self) -> GetSystemCapabilities:
        return self.raw_response

    def get_groups(self) -> list[dict]:
        return self.raw_response["group"]
