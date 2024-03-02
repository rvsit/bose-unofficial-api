import argparse
import os
from typing import TypedDict


class ApplicationVariables(TypedDict):
    ip_address: str
    username: str
    password: str
    jwt_token: str


def override_application_variables_from_cli(variables: ApplicationVariables) -> None:
    parser = argparse.ArgumentParser(description="Login credentials for Bose API")

    parser.add_argument(
        "--ip",
        dest="ip_address",
        required=False,
        help="IP address of the speaker",
    )

    parser.add_argument(
        "--user",
        dest="username",
        required=False,
        help="Username for Bose API, used if no JWT given or expired",
    )

    parser.add_argument(
        "--pass",
        dest="password",
        required=False,
        help="Password for Bose API, used if no JWT given or expired",
    )

    parser.add_argument(
        "--jwt",
        dest="jwt_token",
        required=False,
        help="JWT token for Bose API, optional if user and pass are given",
    )

    args = parser.parse_args()

    if args.ip_address:
        variables["ip_address"] = args.ip_address
    if args.username:
        variables["username"] = args.username
    if args.password:
        variables["password"] = args.password
    if args.jwt_token:
        variables["jwt_token"] = args.jwt_token


def get_application_variables(is_cli: bool) -> ApplicationVariables:
    ip_address = os.environ.get("BOSE_IP_ADDRESS")
    username = os.environ.get("BOSE_USERNAME")
    password = os.environ.get("BOSE_PASSWORD")
    jwt_token = os.environ.get("BOSE_JWT_TOKEN")

    variables = ApplicationVariables(
        ip_address=ip_address,
        username=username,
        password=password,
        jwt_token=jwt_token,
    )

    if is_cli:
        override_application_variables_from_cli(variables)

    return variables
