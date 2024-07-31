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

from .group_0408 import EnterpriseWebhooks
from .group_0409 import SimpleInstallation
from .group_0412 import SimpleUserWebhooks
from .group_0410 import OrganizationSimpleWebhooks
from .group_0441 import PersonalAccessTokenRequest


class WebhookPersonalAccessTokenRequestCancelled(GitHubModel):
    """personal_access_token_request cancelled event"""

    action: Literal["cancelled"] = Field()
    personal_access_token_request: PersonalAccessTokenRequest = Field(
        title="Personal Access Token Request",
        description="Details of a Personal Access Token Request.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    installation: SimpleInstallation = Field(
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )


model_rebuild(WebhookPersonalAccessTokenRequestCancelled)

__all__ = ("WebhookPersonalAccessTokenRequestCancelled",)
