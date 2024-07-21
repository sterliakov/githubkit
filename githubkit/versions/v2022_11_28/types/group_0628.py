"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0408 import ProjectsV2ItemType
from .group_0372 import SimpleInstallationType
from .group_0375 import SimpleUserWebhooksType
from .group_0373 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemEditedType(TypedDict):
    """Projects v2 Item Edited Event"""

    action: Literal["edited"]
    changes: NotRequired[
        Union[
            WebhookProjectsV2ItemEditedPropChangesOneof0Type,
            WebhookProjectsV2ItemEditedPropChangesOneof1Type,
        ]
    ]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


class WebhookProjectsV2ItemEditedPropChangesOneof0Type(TypedDict):
    """WebhookProjectsV2ItemEditedPropChangesOneof0"""

    field_value: WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValueType


class WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValueType(TypedDict):
    """WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValue"""

    field_node_id: NotRequired[str]
    field_type: NotRequired[str]
    field_name: NotRequired[str]
    project_number: NotRequired[int]
    from_: NotRequired[
        Union[
            str,
            int,
            ProjectsV2SingleSelectOptionType,
            ProjectsV2IterationSettingType,
            None,
        ]
    ]
    to: NotRequired[
        Union[
            str,
            int,
            ProjectsV2SingleSelectOptionType,
            ProjectsV2IterationSettingType,
            None,
        ]
    ]


class ProjectsV2SingleSelectOptionType(TypedDict):
    """Projects v2 Single Select Option

    An option for a single select field
    """

    id: str
    name: str
    color: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]


class ProjectsV2IterationSettingType(TypedDict):
    """Projects v2 Iteration Setting

    An iteration setting for an iteration field
    """

    id: str
    title: str
    duration: NotRequired[Union[float, None]]
    start_date: NotRequired[Union[str, None]]


class WebhookProjectsV2ItemEditedPropChangesOneof1Type(TypedDict):
    """WebhookProjectsV2ItemEditedPropChangesOneof1"""

    body: WebhookProjectsV2ItemEditedPropChangesOneof1PropBodyType


class WebhookProjectsV2ItemEditedPropChangesOneof1PropBodyType(TypedDict):
    """WebhookProjectsV2ItemEditedPropChangesOneof1PropBody"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


__all__ = (
    "WebhookProjectsV2ItemEditedType",
    "WebhookProjectsV2ItemEditedPropChangesOneof0Type",
    "WebhookProjectsV2ItemEditedPropChangesOneof0PropFieldValueType",
    "ProjectsV2SingleSelectOptionType",
    "ProjectsV2IterationSettingType",
    "WebhookProjectsV2ItemEditedPropChangesOneof1Type",
    "WebhookProjectsV2ItemEditedPropChangesOneof1PropBodyType",
)
