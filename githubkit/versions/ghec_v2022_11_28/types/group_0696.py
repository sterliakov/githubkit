"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0444 import EnterpriseWebhooksType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType
from .group_0479 import WebhooksProjectColumnType


class WebhookProjectColumnEditedType(TypedDict):
    """project_column edited event"""

    action: Literal["edited"]
    changes: WebhookProjectColumnEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhooksProjectColumnType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


class WebhookProjectColumnEditedPropChangesType(TypedDict):
    """WebhookProjectColumnEditedPropChanges"""

    name: NotRequired[WebhookProjectColumnEditedPropChangesPropNameType]


class WebhookProjectColumnEditedPropChangesPropNameType(TypedDict):
    """WebhookProjectColumnEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookProjectColumnEditedPropChangesPropNameType",
    "WebhookProjectColumnEditedPropChangesType",
    "WebhookProjectColumnEditedType",
)
