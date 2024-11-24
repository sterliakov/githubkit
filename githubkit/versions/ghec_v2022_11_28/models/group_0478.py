"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class WebhooksChanges8(GitHubModel):
    """WebhooksChanges8"""

    tier: WebhooksChanges8PropTier = Field()


class WebhooksChanges8PropTier(GitHubModel):
    """WebhooksChanges8PropTier"""

    from_: WebhooksChanges8PropTierPropFrom = Field(
        alias="from",
        title="Sponsorship Tier",
        description="The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.",
    )


class WebhooksChanges8PropTierPropFrom(GitHubModel):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str = Field()
    description: str = Field()
    is_custom_ammount: Missing[bool] = Field(default=UNSET)
    is_custom_amount: Missing[bool] = Field(default=UNSET)
    is_one_time: bool = Field()
    monthly_price_in_cents: int = Field()
    monthly_price_in_dollars: int = Field()
    name: str = Field()
    node_id: str = Field()


model_rebuild(WebhooksChanges8)
model_rebuild(WebhooksChanges8PropTier)
model_rebuild(WebhooksChanges8PropTierPropFrom)

__all__ = (
    "WebhooksChanges8",
    "WebhooksChanges8PropTier",
    "WebhooksChanges8PropTierPropFrom",
)
