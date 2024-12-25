"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType
from .group_0473 import MergeGroupType


class WebhookMergeGroupDestroyedType(TypedDict):
    """WebhookMergeGroupDestroyed"""

    action: Literal["destroyed"]
    reason: NotRequired[Literal["merged", "invalidated", "dequeued"]]
    installation: NotRequired[SimpleInstallationType]
    merge_group: MergeGroupType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookMergeGroupDestroyedType",)
