"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0406 import WebhooksProjectType
from .group_0373 import EnterpriseWebhooksType
from .group_0374 import SimpleInstallationType
from .group_0376 import RepositoryWebhooksType
from .group_0377 import SimpleUserWebhooksType
from .group_0375 import OrganizationSimpleWebhooksType


class WebhookProjectReopenedType(TypedDict):
    """project reopened event"""

    action: Literal["reopened"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhooksProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectReopenedType",)
