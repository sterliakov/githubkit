"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0450 import EnterpriseWebhooksType
from .group_0451 import SimpleInstallationType
from .group_0452 import OrganizationSimpleWebhooksType
from .group_0453 import RepositoryWebhooksType
from .group_0495 import WebhooksReleaseType


class WebhookReleaseReleasedType(TypedDict):
    """release released event"""

    action: Literal["released"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    release: WebhooksReleaseType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookReleaseReleasedType",)
