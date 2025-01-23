"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0398 import EnterpriseWebhooksType
from .group_0399 import SimpleInstallationType
from .group_0400 import OrganizationSimpleWebhooksType
from .group_0401 import RepositoryWebhooksType
from .group_0431 import WebhooksProjectColumnType


class WebhookProjectColumnMovedType(TypedDict):
    """project_column moved event"""

    action: Literal["moved"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhooksProjectColumnType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


__all__ = ("WebhookProjectColumnMovedType",)
