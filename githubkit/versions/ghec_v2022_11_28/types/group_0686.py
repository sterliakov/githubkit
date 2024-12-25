"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0444 import EnterpriseWebhooksType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType
from .group_0477 import WebhooksProjectCardType


class WebhookProjectCardConvertedType(TypedDict):
    """project_card converted event"""

    action: Literal["converted"]
    changes: WebhookProjectCardConvertedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhooksProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookProjectCardConvertedPropChangesType(TypedDict):
    """WebhookProjectCardConvertedPropChanges"""

    note: WebhookProjectCardConvertedPropChangesPropNoteType


class WebhookProjectCardConvertedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardConvertedPropChangesPropNote"""

    from_: str


__all__ = (
    "WebhookProjectCardConvertedPropChangesPropNoteType",
    "WebhookProjectCardConvertedPropChangesType",
    "WebhookProjectCardConvertedType",
)
