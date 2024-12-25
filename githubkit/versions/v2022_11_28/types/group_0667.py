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
from .group_0431 import PullRequestWebhookType


class WebhookPullRequestEditedType(TypedDict):
    """pull_request edited event"""

    action: Literal["edited"]
    changes: WebhookPullRequestEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: PullRequestWebhookType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


class WebhookPullRequestEditedPropChangesType(TypedDict):
    """WebhookPullRequestEditedPropChanges

    The changes to the comment if the action was `edited`.
    """

    base: NotRequired[WebhookPullRequestEditedPropChangesPropBaseType]
    body: NotRequired[WebhookPullRequestEditedPropChangesPropBodyType]
    title: NotRequired[WebhookPullRequestEditedPropChangesPropTitleType]


class WebhookPullRequestEditedPropChangesPropBodyType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBody"""

    from_: str


class WebhookPullRequestEditedPropChangesPropTitleType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropTitle"""

    from_: str


class WebhookPullRequestEditedPropChangesPropBaseType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBase"""

    ref: WebhookPullRequestEditedPropChangesPropBasePropRefType
    sha: WebhookPullRequestEditedPropChangesPropBasePropShaType


class WebhookPullRequestEditedPropChangesPropBasePropRefType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBasePropRef"""

    from_: str


class WebhookPullRequestEditedPropChangesPropBasePropShaType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBasePropSha"""

    from_: str


__all__ = (
    "WebhookPullRequestEditedPropChangesPropBasePropRefType",
    "WebhookPullRequestEditedPropChangesPropBasePropShaType",
    "WebhookPullRequestEditedPropChangesPropBaseType",
    "WebhookPullRequestEditedPropChangesPropBodyType",
    "WebhookPullRequestEditedPropChangesPropTitleType",
    "WebhookPullRequestEditedPropChangesType",
    "WebhookPullRequestEditedType",
)
