"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0424 import DiscussionType
from .group_0408 import EnterpriseWebhooksType
from .group_0409 import SimpleInstallationType
from .group_0411 import RepositoryWebhooksType
from .group_0412 import SimpleUserWebhooksType
from .group_0410 import OrganizationSimpleWebhooksType


class WebhookDiscussionCategoryChangedType(TypedDict):
    """discussion category changed event"""

    action: Literal["category_changed"]
    changes: WebhookDiscussionCategoryChangedPropChangesType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDiscussionCategoryChangedPropChangesType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChanges"""

    category: WebhookDiscussionCategoryChangedPropChangesPropCategoryType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategory"""

    from_: WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom"""

    created_at: datetime
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: NotRequired[str]
    repository_id: int
    slug: str
    updated_at: str


__all__ = (
    "WebhookDiscussionCategoryChangedType",
    "WebhookDiscussionCategoryChangedPropChangesType",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryType",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType",
)
