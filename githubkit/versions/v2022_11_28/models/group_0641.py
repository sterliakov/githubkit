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

from .group_0037 import Milestone
from .group_0371 import EnterpriseWebhooks
from .group_0374 import RepositoryWebhooks
from .group_0375 import SimpleUserWebhooks
from .group_0412 import WebhooksPullRequest5
from .group_0373 import OrganizationSimpleWebhooks


class WebhookPullRequestDemilestoned(GitHubModel):
    """pull_request demilestoned event"""

    action: Literal["demilestoned"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    milestone: Missing[Milestone] = Field(
        default=UNSET,
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    number: int = Field(description="The pull request number.")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    pull_request: WebhooksPullRequest5 = Field(title="Pull Request")
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookPullRequestDemilestoned)

__all__ = ("WebhookPullRequestDemilestoned",)
