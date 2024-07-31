"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0408 import EnterpriseWebhooksType
from .group_0409 import SimpleInstallationType
from .group_0411 import RepositoryWebhooksType
from .group_0412 import SimpleUserWebhooksType
from .group_0440 import WebhooksMembershipType
from .group_0410 import OrganizationSimpleWebhooksType


class WebhookOrganizationMemberRemovedType(TypedDict):
    """organization member_removed event"""

    action: Literal["member_removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    membership: WebhooksMembershipType
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookOrganizationMemberRemovedType",)
