"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0393 import EnterpriseWebhooksType
from .group_0394 import SimpleInstallationType
from .group_0395 import OrganizationSimpleWebhooksType
from .group_0396 import RepositoryWebhooksType
from .group_0404 import WebhooksUserType
from .group_0413 import WebhooksIssueType


class WebhookIssuesAssignedType(TypedDict):
    """issues assigned event"""

    action: Literal["assigned"]
    assignee: NotRequired[Union[WebhooksUserType, None]]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhooksIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookIssuesAssignedType",)
