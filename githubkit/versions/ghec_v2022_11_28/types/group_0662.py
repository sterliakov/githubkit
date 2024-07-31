"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0443 import WebhooksProjectType
from .group_0408 import EnterpriseWebhooksType
from .group_0409 import SimpleInstallationType
from .group_0411 import RepositoryWebhooksType
from .group_0412 import SimpleUserWebhooksType
from .group_0410 import OrganizationSimpleWebhooksType


class WebhookProjectEditedType(TypedDict):
    """project edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookProjectEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhooksProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookProjectEditedPropChangesType(TypedDict):
    """WebhookProjectEditedPropChanges

    The changes to the project if the action was `edited`.
    """

    body: NotRequired[WebhookProjectEditedPropChangesPropBodyType]
    name: NotRequired[WebhookProjectEditedPropChangesPropNameType]


class WebhookProjectEditedPropChangesPropBodyType(TypedDict):
    """WebhookProjectEditedPropChangesPropBody"""

    from_: str


class WebhookProjectEditedPropChangesPropNameType(TypedDict):
    """WebhookProjectEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookProjectEditedType",
    "WebhookProjectEditedPropChangesType",
    "WebhookProjectEditedPropChangesPropBodyType",
    "WebhookProjectEditedPropChangesPropNameType",
)
