import json

import requests

GIGYA_API_KEY = "3_7PoVX7ELjlWyppFZFGia1Wf1rNGZv_mqVgtqVmYl3Js-hQxZiFIU8uHxd8G6PyNz"


def bose_api_login(loginID: str, password: str):
    """Login to Bose API and return token"""

    gigya_uid, gigya_session = gigya_account_login(loginID, password)

    # TODO
    # gigya_jwt = gigya_get_jwt(gigya_uid, gigya_session)


def gigya_account_login(loginID: str, password: str) -> (str, str):
    """Login to Bose API and return user_id + session_cookie_value"""

    request_body = {
        "loginID": loginID,
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
    response = requests.post(url, data=request_body, headers=headers)

    # Log response
    data = response.json()

    if data["statusCode"] != 200 or data["errorCode"] != 0:
        raise Exception("Login failed: " + json.dumps(data, indent=2))

    if "sessionInfo" not in data or "cookieValue" not in data["sessionInfo"]:
        raise Exception(
            "Unexpected response (no sessionInfo): " + json.dumps(data, indent=2)
        )

    if "UID" not in data:
        raise Exception("Unexpected response (no UID): " + json.dumps(data, indent=2))

    user_id = data["UID"]
    session_cookie_value = data["sessionInfo"]["cookieValue"]

    return user_id, session_cookie_value
