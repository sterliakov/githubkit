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


class WebhookMemberEditedType(TypedDict):
    """member edited event"""

    action: Literal["edited"]
    changes: WebhookMemberEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    member: Union[WebhooksUserType, None]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookMemberEditedPropChangesType(TypedDict):
    """WebhookMemberEditedPropChanges

    The changes to the collaborator permissions
    """

    old_permission: NotRequired[WebhookMemberEditedPropChangesPropOldPermissionType]
    permission: NotRequired[WebhookMemberEditedPropChangesPropPermissionType]


class WebhookMemberEditedPropChangesPropOldPermissionType(TypedDict):
    """WebhookMemberEditedPropChangesPropOldPermission"""

    from_: str


class WebhookMemberEditedPropChangesPropPermissionType(TypedDict):
    """WebhookMemberEditedPropChangesPropPermission"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


__all__ = (
    "WebhookMemberEditedPropChangesPropOldPermissionType",
    "WebhookMemberEditedPropChangesPropPermissionType",
    "WebhookMemberEditedPropChangesType",
    "WebhookMemberEditedType",
)
