"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0383 import WebhooksUserType
from .group_0371 import EnterpriseWebhooksType
from .group_0372 import SimpleInstallationType
from .group_0374 import RepositoryWebhooksType
from .group_0375 import SimpleUserWebhooksType
from .group_0373 import OrganizationSimpleWebhooksType


class WebhookOrgBlockUnblockedType(TypedDict):
    """org_block unblocked event"""

    action: Literal["unblocked"]
    blocked_user: Union[WebhooksUserType, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookOrgBlockUnblockedType",)
