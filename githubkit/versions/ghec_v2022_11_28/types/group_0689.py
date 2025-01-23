"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0452 import OrganizationSimpleWebhooksType
from .group_0453 import RepositoryWebhooksType
from .group_0690 import WebhookPingPropHookType


class WebhookPingType(TypedDict):
    """WebhookPing"""

    hook: NotRequired[WebhookPingPropHookType]
    hook_id: NotRequired[int]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]
    zen: NotRequired[str]


__all__ = ("WebhookPingType",)
