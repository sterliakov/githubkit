"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0393 import WebhooksChangesType
from .group_0373 import EnterpriseWebhooksType
from .group_0374 import SimpleInstallationType
from .group_0376 import RepositoryWebhooksType
from .group_0377 import SimpleUserWebhooksType
from .group_0392 import WebhooksIssueCommentType
from .group_0375 import OrganizationSimpleWebhooksType
from .group_0527 import WebhookIssueCommentEditedPropIssueType


class WebhookIssueCommentEditedType(TypedDict):
    """issue_comment edited event"""

    action: Literal["edited"]
    changes: WebhooksChangesType
    comment: WebhooksIssueCommentType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssueCommentEditedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookIssueCommentEditedType",)
