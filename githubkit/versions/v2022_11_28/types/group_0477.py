"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0258 import DependabotAlertType
from .group_0393 import EnterpriseWebhooksType
from .group_0394 import SimpleInstallationType
from .group_0395 import OrganizationSimpleWebhooksType
from .group_0396 import RepositoryWebhooksType


class WebhookDependabotAlertFixedType(TypedDict):
    """Dependabot alert fixed event"""

    action: Literal["fixed"]
    alert: DependabotAlertType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookDependabotAlertFixedType",)
