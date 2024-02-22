from typing import TypedDict


class NotificationItem(TypedDict):
    # Example: /system/update/start
    resource: str
    # Example: 2
    # Only seen integers so far but the capabilities endpoint returns a float
    version: float
