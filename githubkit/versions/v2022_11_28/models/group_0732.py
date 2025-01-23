"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0398 import EnterpriseWebhooks
from .group_0399 import SimpleInstallation
from .group_0400 import OrganizationSimpleWebhooks
from .group_0401 import RepositoryWebhooks


class WebhookRepositoryVulnerabilityAlertDismiss(GitHubModel):
    """repository_vulnerability_alert dismiss event"""

    action: Literal["dismiss"] = Field()
    alert: WebhookRepositoryVulnerabilityAlertDismissPropAlert = Field(
        title="Repository Vulnerability Alert Alert",
        description="The security alert of the vulnerable dependency.",
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
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookRepositoryVulnerabilityAlertDismissPropAlert(GitHubModel):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str = Field()
    affected_range: str = Field()
    created_at: str = Field()
    dismiss_comment: Missing[Union[str, None]] = Field(default=UNSET)
    dismiss_reason: str = Field()
    dismissed_at: str = Field()
    dismisser: Union[
        WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisser, None
    ] = Field(title="User")
    external_identifier: str = Field()
    external_reference: Union[str, None] = Field()
    fix_reason: Missing[str] = Field(default=UNSET)
    fixed_at: Missing[datetime] = Field(default=UNSET)
    fixed_in: Missing[str] = Field(default=UNSET)
    ghsa_id: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field()
    severity: str = Field()
    state: Literal["dismissed"] = Field()


class WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookRepositoryVulnerabilityAlertDismiss)
model_rebuild(WebhookRepositoryVulnerabilityAlertDismissPropAlert)
model_rebuild(WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisser)

__all__ = (
    "WebhookRepositoryVulnerabilityAlertDismiss",
    "WebhookRepositoryVulnerabilityAlertDismissPropAlert",
    "WebhookRepositoryVulnerabilityAlertDismissPropAlertPropDismisser",
)
