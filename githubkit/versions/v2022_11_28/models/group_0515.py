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
from .group_0017 import Installation
from .group_0393 import EnterpriseWebhooks
from .group_0395 import OrganizationSimpleWebhooks
from .group_0396 import RepositoryWebhooks
from .group_0409 import WebhooksRepositoriesItems


class WebhookInstallationDeleted(GitHubModel):
    """installation deleted event"""

    action: Literal["deleted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Installation = Field(title="Installation", description="Installation")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repositories: Missing[list[WebhooksRepositoriesItems]] = Field(
        default=UNSET,
        description="An array of repository objects that the installation can access.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    requester: Missing[None] = Field(default=UNSET)
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(WebhookInstallationDeleted)

__all__ = ("WebhookInstallationDeleted",)
