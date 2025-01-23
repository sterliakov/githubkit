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
from .group_0451 import SimpleInstallation
from .group_0452 import OrganizationSimpleWebhooks
from .group_0486 import ProjectsV2


class WebhookProjectsV2ProjectEdited(GitHubModel):
    """Projects v2 Project Edited Event"""

    action: Literal["edited"] = Field()
    changes: WebhookProjectsV2ProjectEditedPropChanges = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    projects_v2: ProjectsV2 = Field(
        title="Projects v2 Project", description="A projects v2 project"
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookProjectsV2ProjectEditedPropChanges(GitHubModel):
    """WebhookProjectsV2ProjectEditedPropChanges"""

    description: Missing[WebhookProjectsV2ProjectEditedPropChangesPropDescription] = (
        Field(default=UNSET)
    )
    public: Missing[WebhookProjectsV2ProjectEditedPropChangesPropPublic] = Field(
        default=UNSET
    )
    short_description: Missing[
        WebhookProjectsV2ProjectEditedPropChangesPropShortDescription
    ] = Field(default=UNSET)
    title: Missing[WebhookProjectsV2ProjectEditedPropChangesPropTitle] = Field(
        default=UNSET
    )


class WebhookProjectsV2ProjectEditedPropChangesPropDescription(GitHubModel):
    """WebhookProjectsV2ProjectEditedPropChangesPropDescription"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[str, None]] = Field(default=UNSET)


class WebhookProjectsV2ProjectEditedPropChangesPropPublic(GitHubModel):
    """WebhookProjectsV2ProjectEditedPropChangesPropPublic"""

    from_: Missing[bool] = Field(default=UNSET, alias="from")
    to: Missing[bool] = Field(default=UNSET)


class WebhookProjectsV2ProjectEditedPropChangesPropShortDescription(GitHubModel):
    """WebhookProjectsV2ProjectEditedPropChangesPropShortDescription"""

    from_: Missing[Union[str, None]] = Field(default=UNSET, alias="from")
    to: Missing[Union[str, None]] = Field(default=UNSET)


class WebhookProjectsV2ProjectEditedPropChangesPropTitle(GitHubModel):
    """WebhookProjectsV2ProjectEditedPropChangesPropTitle"""

    from_: Missing[str] = Field(default=UNSET, alias="from")
    to: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectsV2ProjectEdited)
model_rebuild(WebhookProjectsV2ProjectEditedPropChanges)
model_rebuild(WebhookProjectsV2ProjectEditedPropChangesPropDescription)
model_rebuild(WebhookProjectsV2ProjectEditedPropChangesPropPublic)
model_rebuild(WebhookProjectsV2ProjectEditedPropChangesPropShortDescription)
model_rebuild(WebhookProjectsV2ProjectEditedPropChangesPropTitle)

__all__ = (
    "WebhookProjectsV2ProjectEdited",
    "WebhookProjectsV2ProjectEditedPropChanges",
    "WebhookProjectsV2ProjectEditedPropChangesPropDescription",
    "WebhookProjectsV2ProjectEditedPropChangesPropPublic",
    "WebhookProjectsV2ProjectEditedPropChangesPropShortDescription",
    "WebhookProjectsV2ProjectEditedPropChangesPropTitle",
)
