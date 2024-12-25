"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0393 import EnterpriseWebhooksType
from .group_0394 import SimpleInstallationType
from .group_0395 import OrganizationSimpleWebhooksType
from .group_0396 import RepositoryWebhooksType
from .group_0406 import DiscussionType
from .group_0407 import WebhooksCommentType


class WebhookDiscussionCommentEditedType(TypedDict):
    """discussion_comment edited event"""

    action: Literal["edited"]
    changes: WebhookDiscussionCommentEditedPropChangesType
    comment: WebhooksCommentType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookDiscussionCommentEditedPropChangesType(TypedDict):
    """WebhookDiscussionCommentEditedPropChanges"""

    body: WebhookDiscussionCommentEditedPropChangesPropBodyType


class WebhookDiscussionCommentEditedPropChangesPropBodyType(TypedDict):
    """WebhookDiscussionCommentEditedPropChangesPropBody"""

    from_: str


__all__ = (
    "WebhookDiscussionCommentEditedPropChangesPropBodyType",
    "WebhookDiscussionCommentEditedPropChangesType",
    "WebhookDiscussionCommentEditedType",
)
