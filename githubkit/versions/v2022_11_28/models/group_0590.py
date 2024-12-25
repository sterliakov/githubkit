"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0393 import EnterpriseWebhooks
from .group_0394 import SimpleInstallation
from .group_0395 import OrganizationSimpleWebhooks
from .group_0396 import RepositoryWebhooks
from .group_0417 import WebhooksMarketplacePurchase


class WebhookMarketplacePurchasePendingChange(GitHubModel):
    """marketplace_purchase pending_change event"""

    action: Literal["pending_change"] = Field()
    effective_date: str = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    marketplace_purchase: WebhooksMarketplacePurchase = Field(
        title="Marketplace Purchase"
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    previous_marketplace_purchase: Missing[
        WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchase
    ] = Field(default=UNSET, title="Marketplace Purchase")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchase(
    GitHubModel
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccount = Field()
    billing_cycle: str = Field()
    free_trial_ends_on: Union[str, None] = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan = Field()
    unit_count: int = Field()


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccoun
    t
    """

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan"""

    bullets: list[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhookMarketplacePurchasePendingChange)
model_rebuild(WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchase)
model_rebuild(
    WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccount
)
model_rebuild(
    WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan
)

__all__ = (
    "WebhookMarketplacePurchasePendingChange",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchase",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccount",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan",
)
