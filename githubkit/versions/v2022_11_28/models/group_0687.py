"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0371 import EnterpriseWebhooks
from .group_0372 import SimpleInstallation
from .group_0374 import RepositoryWebhooks
from .group_0375 import SimpleUserWebhooks
from .group_0373 import OrganizationSimpleWebhooks


class WebhookRepositoryEdited(GitHubModel):
    """repository edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookRepositoryEditedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookRepositoryEditedPropChanges(GitHubModel):
    """WebhookRepositoryEditedPropChanges"""

    default_branch: Missing[WebhookRepositoryEditedPropChangesPropDefaultBranch] = (
        Field(default=UNSET)
    )
    description: Missing[WebhookRepositoryEditedPropChangesPropDescription] = Field(
        default=UNSET
    )
    homepage: Missing[WebhookRepositoryEditedPropChangesPropHomepage] = Field(
        default=UNSET
    )
    topics: Missing[WebhookRepositoryEditedPropChangesPropTopics] = Field(default=UNSET)


class WebhookRepositoryEditedPropChangesPropDefaultBranch(GitHubModel):
    """WebhookRepositoryEditedPropChangesPropDefaultBranch"""

    from_: str = Field(alias="from")


class WebhookRepositoryEditedPropChangesPropDescription(GitHubModel):
    """WebhookRepositoryEditedPropChangesPropDescription"""

    from_: Union[str, None] = Field(alias="from")


class WebhookRepositoryEditedPropChangesPropHomepage(GitHubModel):
    """WebhookRepositoryEditedPropChangesPropHomepage"""

    from_: Union[str, None] = Field(alias="from")


class WebhookRepositoryEditedPropChangesPropTopics(GitHubModel):
    """WebhookRepositoryEditedPropChangesPropTopics"""

    from_: Missing[Union[List[str], None]] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryEdited)
model_rebuild(WebhookRepositoryEditedPropChanges)
model_rebuild(WebhookRepositoryEditedPropChangesPropDefaultBranch)
model_rebuild(WebhookRepositoryEditedPropChangesPropDescription)
model_rebuild(WebhookRepositoryEditedPropChangesPropHomepage)
model_rebuild(WebhookRepositoryEditedPropChangesPropTopics)

__all__ = (
    "WebhookRepositoryEdited",
    "WebhookRepositoryEditedPropChanges",
    "WebhookRepositoryEditedPropChangesPropDefaultBranch",
    "WebhookRepositoryEditedPropChangesPropDescription",
    "WebhookRepositoryEditedPropChangesPropHomepage",
    "WebhookRepositoryEditedPropChangesPropTopics",
)
