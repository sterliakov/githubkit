"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0483 import ProjectsV2StatusUpdateType


class WebhookProjectsV2StatusUpdateEditedType(TypedDict):
    """Projects v2 Status Update Edited Event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookProjectsV2StatusUpdateEditedPropChangesType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_status_update: ProjectsV2StatusUpdateType
    sender: SimpleUserType


class WebhookProjectsV2StatusUpdateEditedPropChangesType(TypedDict):
    """WebhookProjectsV2StatusUpdateEditedPropChanges"""

    body: NotRequired[WebhookProjectsV2StatusUpdateEditedPropChangesPropBodyType]
    status: NotRequired[WebhookProjectsV2StatusUpdateEditedPropChangesPropStatusType]
    start_date: NotRequired[
        WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDateType
    ]
    target_date: NotRequired[
        WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDateType
    ]


class WebhookProjectsV2StatusUpdateEditedPropChangesPropBodyType(TypedDict):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropBody"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


class WebhookProjectsV2StatusUpdateEditedPropChangesPropStatusType(TypedDict):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropStatus"""

    from_: NotRequired[
        Union[None, Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"]]
    ]
    to: NotRequired[
        Union[None, Literal["INACTIVE", "ON_TRACK", "AT_RISK", "OFF_TRACK", "COMPLETE"]]
    ]


class WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDateType(TypedDict):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDate"""

    from_: NotRequired[Union[date, None]]
    to: NotRequired[Union[date, None]]


class WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDateType(TypedDict):
    """WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDate"""

    from_: NotRequired[Union[date, None]]
    to: NotRequired[Union[date, None]]


__all__ = (
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropBodyType",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropStartDateType",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropStatusType",
    "WebhookProjectsV2StatusUpdateEditedPropChangesPropTargetDateType",
    "WebhookProjectsV2StatusUpdateEditedPropChangesType",
    "WebhookProjectsV2StatusUpdateEditedType",
)
