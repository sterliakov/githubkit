"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0444 import EnterpriseWebhooksType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType


class WebhookSecretScanningScanCompletedType(TypedDict):
    """secret_scanning_scan completed event"""

    action: Literal["completed"]
    type: Literal["backfill", "custom-pattern-backfill", "pattern-version-backfill"]
    source: Literal["git", "issues", "pull-requests", "discussions", "wiki"]
    started_at: datetime
    completed_at: datetime
    secret_types: NotRequired[Union[list[str], None]]
    custom_pattern_name: NotRequired[Union[str, None]]
    custom_pattern_scope: NotRequired[
        Union[None, Literal["repository", "organization", "enterprise"]]
    ]
    repository: NotRequired[RepositoryWebhooksType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookSecretScanningScanCompletedType",)
