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

from .group_0447 import ProjectsV2Item
from .group_0409 import SimpleInstallation
from .group_0412 import SimpleUserWebhooks
from .group_0446 import WebhooksProjectChanges
from .group_0410 import OrganizationSimpleWebhooks


class WebhookProjectsV2ItemRestored(GitHubModel):
    """Projects v2 Item Restored Event"""

    action: Literal["restored"] = Field()
    changes: WebhooksProjectChanges = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    projects_v2_item: ProjectsV2Item = Field(
        title="Projects v2 Item", description="An item belonging to a project"
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookProjectsV2ItemRestored)

__all__ = ("WebhookProjectsV2ItemRestored",)
