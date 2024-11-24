"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild
from githubkit.typing import Missing


class HookDelivery(GitHubModel):
    """Webhook delivery

    Delivery made by a webhook.
    """

    id: int = Field(description="Unique identifier of the delivery.")
    guid: str = Field(
        description="Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event)."
    )
    delivered_at: datetime = Field(description="Time when the delivery was delivered.")
    redelivery: bool = Field(description="Whether the delivery is a redelivery.")
    duration: float = Field(description="Time spent delivering.")
    status: str = Field(
        description="Description of the status of the attempted delivery"
    )
    status_code: int = Field(description="Status code received when delivery was made.")
    event: str = Field(description="The event that triggered the delivery.")
    action: Union[str, None] = Field(
        description="The type of activity for the event that triggered the delivery."
    )
    installation_id: Union[int, None] = Field(
        description="The id of the GitHub App installation associated with this event."
    )
    repository_id: Union[int, None] = Field(
        description="The id of the repository associated with this event."
    )
    throttled_at: Missing[Union[datetime, None]] = Field(
        default=UNSET, description="Time when the webhook delivery was throttled."
    )
    url: Missing[str] = Field(
        default=UNSET, description="The URL target of the delivery."
    )
    request: HookDeliveryPropRequest = Field()
    response: HookDeliveryPropResponse = Field()


class HookDeliveryPropRequest(GitHubModel):
    """HookDeliveryPropRequest"""

    headers: Union[HookDeliveryPropRequestPropHeaders, None] = Field(
        description="The request headers sent with the webhook delivery."
    )
    payload: Union[HookDeliveryPropRequestPropPayload, None] = Field(
        description="The webhook payload."
    )


class HookDeliveryPropRequestPropHeaders(ExtraGitHubModel):
    """HookDeliveryPropRequestPropHeaders

    The request headers sent with the webhook delivery.
    """


class HookDeliveryPropRequestPropPayload(ExtraGitHubModel):
    """HookDeliveryPropRequestPropPayload

    The webhook payload.
    """


class HookDeliveryPropResponse(GitHubModel):
    """HookDeliveryPropResponse"""

    headers: Union[HookDeliveryPropResponsePropHeaders, None] = Field(
        description="The response headers received when the delivery was made."
    )
    payload: Union[str, None] = Field(description="The response payload received.")


class HookDeliveryPropResponsePropHeaders(ExtraGitHubModel):
    """HookDeliveryPropResponsePropHeaders

    The response headers received when the delivery was made.
    """


model_rebuild(HookDelivery)
model_rebuild(HookDeliveryPropRequest)
model_rebuild(HookDeliveryPropRequestPropHeaders)
model_rebuild(HookDeliveryPropRequestPropPayload)
model_rebuild(HookDeliveryPropResponse)
model_rebuild(HookDeliveryPropResponsePropHeaders)

__all__ = (
    "HookDelivery",
    "HookDeliveryPropRequest",
    "HookDeliveryPropRequestPropHeaders",
    "HookDeliveryPropRequestPropPayload",
    "HookDeliveryPropResponse",
    "HookDeliveryPropResponsePropHeaders",
)
