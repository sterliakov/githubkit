"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0419 import WebhooksAlertType
from .group_0373 import EnterpriseWebhooksType
from .group_0374 import SimpleInstallationType
from .group_0376 import RepositoryWebhooksType
from .group_0377 import SimpleUserWebhooksType
from .group_0375 import OrganizationSimpleWebhooksType


class WebhookRepositoryVulnerabilityAlertCreateType(TypedDict):
    """repository_vulnerability_alert create event"""

    action: Literal["create"]
    alert: WebhooksAlertType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookRepositoryVulnerabilityAlertCreateType",)
