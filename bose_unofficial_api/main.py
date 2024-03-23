# Example usage
import asyncio
import logging

from bose_unofficial_api import auth
from bose_unofficial_api.speaker import BoseSpeaker
from bose_unofficial_api.variables import get_application_variables
from bose_unofficial_api.event.observer import Observer


class LogNotifyObserver(Observer):
    def on_message(self, message: dict) -> None:
        logging.info("NOTIFY Received message: %s", message.get("body", {}))


async def main():
    logging.basicConfig(level=logging.INFO)

    variables = get_application_variables(is_cli=True)

    if not variables["ip_address"]:
        raise ValueError(
            "Please set the BOSE_IP_ADDRESS environment variable or the --ip flag"
        )

    auth.refresh_jwt_if_needed(variables)

    if not variables["jwt_token"]:
        raise ValueError(
            "Please set the BOSE_JWT_TOKEN environment variable or the --jwt flag"
        )

    speaker = await BoseSpeaker.connect(
        ip_address=variables["ip_address"],
        jwt_token=variables["jwt_token"],
        log_messages=False,
    )
    speaker.connection.add_notify_observer(LogNotifyObserver())

    # Example of sending a message and waiting for its response
    now_playing = await speaker.api.get_now_playing()
    print("Now playing: %s", now_playing)

    # Await future to sleep 500s
    await asyncio.sleep(500)

    await speaker.connection.close()


def start():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
