"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0251 import DependabotAlertType
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0386 import OrganizationSimpleWebhooksType
from .group_0387 import RepositoryWebhooksType


class WebhookDependabotAlertCreatedType(TypedDict):
    """Dependabot alert created event"""

    action: Literal["created"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDependabotAlertCreatedType",)
