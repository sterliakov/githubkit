"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0399 import SimpleInstallationType
from .group_0400 import OrganizationSimpleWebhooksType
from .group_0434 import ProjectsV2ItemType


class WebhookProjectsV2ItemConvertedType(TypedDict):
    """Projects v2 Item Converted Event"""

    action: Literal["converted"]
    changes: WebhookProjectsV2ItemConvertedPropChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserType


class WebhookProjectsV2ItemConvertedPropChangesType(TypedDict):
    """WebhookProjectsV2ItemConvertedPropChanges"""

    content_type: NotRequired[
        WebhookProjectsV2ItemConvertedPropChangesPropContentTypeType
    ]


class WebhookProjectsV2ItemConvertedPropChangesPropContentTypeType(TypedDict):
    """WebhookProjectsV2ItemConvertedPropChangesPropContentType"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[str]


__all__ = (
    "WebhookProjectsV2ItemConvertedPropChangesPropContentTypeType",
    "WebhookProjectsV2ItemConvertedPropChangesType",
    "WebhookProjectsV2ItemConvertedType",
)
