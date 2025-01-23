"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict


class HookDeliveryType(TypedDict):
    """Webhook delivery

    Delivery made by a webhook.
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
    url: NotRequired[str]
    request: HookDeliveryPropRequestType
    response: HookDeliveryPropResponseType


class HookDeliveryPropRequestType(TypedDict):
    """HookDeliveryPropRequest"""

    headers: Union[HookDeliveryPropRequestPropHeadersType, None]
    payload: Union[HookDeliveryPropRequestPropPayloadType, None]


HookDeliveryPropRequestPropHeadersType: TypeAlias = dict[str, Any]
"""HookDeliveryPropRequestPropHeaders

The request headers sent with the webhook delivery.
"""


HookDeliveryPropRequestPropPayloadType: TypeAlias = dict[str, Any]
"""HookDeliveryPropRequestPropPayload

The webhook payload.
"""


class HookDeliveryPropResponseType(TypedDict):
    """HookDeliveryPropResponse"""

    headers: Union[HookDeliveryPropResponsePropHeadersType, None]
    payload: Union[str, None]


HookDeliveryPropResponsePropHeadersType: TypeAlias = dict[str, Any]
"""HookDeliveryPropResponsePropHeaders

The response headers received when the delivery was made.
"""


__all__ = (
    "HookDeliveryPropRequestPropHeadersType",
    "HookDeliveryPropRequestPropPayloadType",
    "HookDeliveryPropRequestType",
    "HookDeliveryPropResponsePropHeadersType",
    "HookDeliveryPropResponseType",
    "HookDeliveryType",
)
