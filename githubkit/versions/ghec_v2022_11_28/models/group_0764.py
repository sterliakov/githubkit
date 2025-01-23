"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0450 import EnterpriseWebhooks
from .group_0451 import SimpleInstallation
from .group_0452 import OrganizationSimpleWebhooks
from .group_0453 import RepositoryWebhooks
from .group_0495 import WebhooksRelease


class WebhookReleaseEdited(GitHubModel):
    """release edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookReleaseEditedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    release: WebhooksRelease = Field(
        title="Release",
        description="The [release](https://docs.github.com/enterprise-cloud@latest//rest/releases/releases/#get-a-release) object.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


class WebhookReleaseEditedPropChanges(GitHubModel):
    """WebhookReleaseEditedPropChanges"""

    body: Missing[WebhookReleaseEditedPropChangesPropBody] = Field(default=UNSET)
    name: Missing[WebhookReleaseEditedPropChangesPropName] = Field(default=UNSET)
    make_latest: Missing[WebhookReleaseEditedPropChangesPropMakeLatest] = Field(
        default=UNSET
    )


class WebhookReleaseEditedPropChangesPropBody(GitHubModel):
    """WebhookReleaseEditedPropChangesPropBody"""

    from_: str = Field(
        alias="from",
        description="The previous version of the body if the action was `edited`.",
    )


class WebhookReleaseEditedPropChangesPropName(GitHubModel):
    """WebhookReleaseEditedPropChangesPropName"""

    from_: str = Field(
        alias="from",
        description="The previous version of the name if the action was `edited`.",
    )


class WebhookReleaseEditedPropChangesPropMakeLatest(GitHubModel):
    """WebhookReleaseEditedPropChangesPropMakeLatest"""

    to: bool = Field(
        description="Whether this release was explicitly `edited` to be the latest."
    )


model_rebuild(WebhookReleaseEdited)
model_rebuild(WebhookReleaseEditedPropChanges)
model_rebuild(WebhookReleaseEditedPropChangesPropBody)
model_rebuild(WebhookReleaseEditedPropChangesPropName)
model_rebuild(WebhookReleaseEditedPropChangesPropMakeLatest)

__all__ = (
    "WebhookReleaseEdited",
    "WebhookReleaseEditedPropChanges",
    "WebhookReleaseEditedPropChangesPropBody",
    "WebhookReleaseEditedPropChangesPropMakeLatest",
    "WebhookReleaseEditedPropChangesPropName",
)
