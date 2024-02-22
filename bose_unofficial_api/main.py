# Example usage
import asyncio
import logging

from bose_unofficial_api import auth
from bose_unofficial_api.speaker import BoseSpeaker
from bose_unofficial_api.variables import get_application_variables


async def main():
    logging.basicConfig(level=logging.WARN)

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
        log_messages=True,
    )

    # Example of sending a message and waiting for its response
    now_playing = await speaker.get_now_playing()
    print("Now playing: %s", now_playing)

    await speaker.connection.close()


def start():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
