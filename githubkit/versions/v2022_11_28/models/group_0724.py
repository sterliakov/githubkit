"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0423 import WebhooksChanges8
from .group_0373 import EnterpriseWebhooks
from .group_0374 import SimpleInstallation
from .group_0376 import RepositoryWebhooks
from .group_0377 import SimpleUserWebhooks
from .group_0422 import WebhooksSponsorship
from .group_0375 import OrganizationSimpleWebhooks


class WebhookSponsorshipPendingTierChange(GitHubModel):
    """sponsorship pending_tier_change event"""

    action: Literal["pending_tier_change"] = Field()
    changes: WebhooksChanges8 = Field()
    effective_date: Missing[str] = Field(
        default=UNSET,
        description="The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.",
    )
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
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    sponsorship: WebhooksSponsorship = Field()


model_rebuild(WebhookSponsorshipPendingTierChange)

__all__ = ("WebhookSponsorshipPendingTierChange",)
