from datetime import datetime
import json

import jwt
import requests

from bose_unofficial_api.variables import ApplicationVariables

GIGYA_API_KEY = "3_7PoVX7ELjlWyppFZFGia1Wf1rNGZv_mqVgtqVmYl3Js-hQxZiFIU8uHxd8G6PyNz"
BOSE_CLIENT_ID = "67616C617061676F732D70726F642D6D61647269642D696F73"


def refresh_jwt_if_needed(variables: ApplicationVariables) -> None:
    """Refresh JWT if needed"""

    jwt_needs_refresh = False

    if variables["jwt_token"]:
        expiration_in_days = get_jwt_expiration_days_from_now(variables["jwt_token"])
        print("JWT expiration in days:", expiration_in_days)

        if expiration_in_days < 5:
            jwt_needs_refresh = True
    else:
        jwt_needs_refresh = True

    if jwt_needs_refresh:
        if variables["username"] and variables["password"]:
            variables["jwt_token"] = bose_api_login(
                variables["username"], variables["password"]
            )
        else:
            raise Exception(
                "JWT token is missing or expired, and no username/password provided"
            )


def get_jwt_expiration_days_from_now(token: str) -> int:
    """Get JWT expiration days from now"""

    # Decode the token without verification of signature
    decoded = jwt.decode(token, options={"verify_signature": False})

    # Extract expiration time
    exp_timestamp = decoded.get("exp")

    # Convert expiration timestamp to datetime
    exp_datetime = datetime.fromtimestamp(exp_timestamp)

    # Current datetime in UTC
    now_datetime = datetime.now()

    # Calculate difference in days
    expiration_in_days = (exp_datetime - now_datetime).days

    return expiration_in_days


def bose_api_login(username: str, password: str):
    """Login to Bose API and return token"""

    print("Logging in to Bose API...")

    (
        gigya_uid,
        gigya_uid_timestamp,
        gigya_uid_signature,
        gigya_token,
    ) = gigya_account_login(username, password)

    # print("UID:", gigya_uid)
    # print("UID timestamp:", gigya_uid_timestamp)
    # print("UID signature:", gigya_uid_signature)
    # print("Session:", gigya_token)

    gigya_jwt = gigya_get_jwt(gigya_token)

    # print("JWT:", gigya_jwt)

    bose_jwt = bose_get_jwt(
        gigya_jwt,
        gigya_uid,
        gigya_uid_timestamp,
        gigya_uid_signature,
    )

    print("Bose JWT (recommended to save):", bose_jwt)

    return bose_jwt


def gigya_account_login(login_id: str, password: str) -> (str, str):
    """Login to Bose API and return user_id + session_cookie_value"""

    request_body = {
        "loginID": login_id,
        "password": password,
        "apikey": GIGYA_API_KEY,
        "format": "json",
        "httpStatusCodes": "false",
        "include": "profile,data,emails,subscriptions,preferences,",
        "includeUserInfo": "true",
        "lang": "en",
        "loginMode": "standard",
        "sessionExpiration": 0,
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
    }

    # Gigya API endpoint
    url = "https://accounts.us1.gigya.com/accounts.login"

    # Send the request
    response = requests.post(url, data=request_body, headers=headers, timeout=10)

    data = response.json()

    if data["statusCode"] != 200 or data["errorCode"] != 0:
        raise Exception("Login failed: " + json.dumps(data, indent=2))

    if "sessionInfo" not in data or "cookieValue" not in data["sessionInfo"]:
        raise Exception(
            "Unexpected response (no sessionInfo): " + json.dumps(data, indent=2)
        )

    if "UID" not in data:
        raise Exception("Unexpected response (no UID): " + json.dumps(data, indent=2))

    uid = data["UID"]
    uid_signature = data["UIDSignature"]
    uid_timestamp = data["signatureTimestamp"]
    cookie_value = data["sessionInfo"]["cookieValue"]

    return uid, uid_timestamp, uid_signature, cookie_value


def gigya_get_jwt(session_token: str) -> str:
    """Get JWT token from Gigya"""

    request_body = {
        "login_token": session_token,
        "authMode": "cookie",
        "apikey": GIGYA_API_KEY,
        "format": "json",
        "httpStatusCodes": "false",
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
    }

    # Gigya API endpoint
    url = "https://accounts.us1.gigya.com/accounts.getJWT"

    # Send the request
    response = requests.post(url, data=request_body, headers=headers, timeout=10)

    # Log response
    data = response.json()

    if "id_token" not in data:
        raise Exception(
            "Unexpected response (no id_token): " + json.dumps(data, indent=2)
        )

    return data["id_token"]


def bose_get_jwt(
    gigya_jwt: str,
    uid: str,
    uid_timestamp: str,
    uid_signature: str,
) -> str:
    """Get JWT token from Bose"""

    request_body = {
        "scope": "openid",
        "grant_type": "id_token",
        "client_id": BOSE_CLIENT_ID,
        "id_token": gigya_jwt,
        "uid": uid,
        "uid_signature": uid_signature,
        "signature_timestamp": uid_timestamp,
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "*/*",
        "X-ApiKey": BOSE_CLIENT_ID,
        "X-Api-Version": "1",
    }

    # Bose API endpoint
    url = "https://id.api.bose.io/id-jwt-core/token"

    # Send the request
    response = requests.post(url, json=request_body, headers=headers, timeout=10)

    # Log response
    data = response.json()

    # the response has both an access_token and a refresh_token, we use the refresh_token as it is valid for a year and also works
    if "refresh_token" not in data:
        raise Exception(
            "Unexpected response (no refresh_token): " + json.dumps(data, indent=2)
        )

    return data["refresh_token"]
