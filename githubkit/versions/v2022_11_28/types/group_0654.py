"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0394 import SimpleInstallationType
from .group_0395 import OrganizationSimpleWebhooksType
from .group_0428 import WebhooksProjectChangesType
from .group_0429 import ProjectsV2ItemType


class WebhookProjectsV2ItemRestoredType(TypedDict):
    """Projects v2 Item Restored Event"""

    action: Literal["restored"]
    changes: WebhooksProjectChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2ItemRestoredType",)
