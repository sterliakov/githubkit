"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict


class HookDeliveryItemType(TypedDict):
    """Simple webhook delivery

    Delivery made by a webhook, without request and response information.
    """

    id: int
    guid: str
    delivered_at: datetime
    redelivery: bool
    duration: float
    status: str
    status_code: int
    event: str
    action: Union[str, None]
    installation_id: Union[int, None]
    repository_id: Union[int, None]
    throttled_at: NotRequired[Union[datetime, None]]


__all__ = ("HookDeliveryItemType",)
