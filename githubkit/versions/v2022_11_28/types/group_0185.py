"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0029 import TeamType


class PendingDeploymentPropReviewersItemsType(TypedDict):
    """PendingDeploymentPropReviewersItems"""

    type: NotRequired[Literal["User", "Team"]]
    reviewer: NotRequired[Union[SimpleUserType, TeamType]]


class PendingDeploymentType(TypedDict):
    """Pending Deployment

    Details of a deployment that is waiting for protection rules to pass
    """

    environment: PendingDeploymentPropEnvironmentType
    wait_timer: int
    wait_timer_started_at: Union[datetime, None]
    current_user_can_approve: bool
    reviewers: list[PendingDeploymentPropReviewersItemsType]


class PendingDeploymentPropEnvironmentType(TypedDict):
    """PendingDeploymentPropEnvironment"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]


__all__ = (
    "PendingDeploymentPropEnvironmentType",
    "PendingDeploymentPropReviewersItemsType",
    "PendingDeploymentType",
)
