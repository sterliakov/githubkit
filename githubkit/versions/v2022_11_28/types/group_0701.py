"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0371 import EnterpriseWebhooksType
from .group_0372 import SimpleInstallationType
from .group_0374 import RepositoryWebhooksType
from .group_0375 import SimpleUserWebhooksType
from .group_0373 import OrganizationSimpleWebhooksType


class WebhookRepositoryUnarchivedType(TypedDict):
    """repository unarchived event"""

    action: Literal["unarchived"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryUnarchivedType",)
