"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
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


class WebhookGollum(GitHubModel):
    """gollum event"""

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
    pages: builtins.list[WebhookGollumPropPagesItems] = Field(
        description="The pages that were updated."
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookGollumPropPagesItems(GitHubModel):
    """WebhookGollumPropPagesItems"""

    action: Literal["created", "edited"] = Field(
        description="The action that was performed on the page. Can be `created` or `edited`."
    )
    html_url: str = Field(description="Points to the HTML wiki page.")
    page_name: str = Field(description="The name of the page.")
    sha: str = Field(description="The latest commit SHA of the page.")
    summary: Union[str, None] = Field()
    title: str = Field(description="The current page title.")


model_rebuild(WebhookGollum)
model_rebuild(WebhookGollumPropPagesItems)

__all__ = (
    "WebhookGollum",
    "WebhookGollumPropPagesItems",
)
