"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict

from .group_0002 import SimpleUserType
from .group_0008 import IntegrationType


class MilestonedIssueEventType(TypedDict):
    """Milestoned Issue Event

    Milestoned Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: SimpleUserType
    event: Literal["milestoned"]
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: str
    performed_via_github_app: Union[None, IntegrationType, None]
    milestone: MilestonedIssueEventPropMilestoneType


class MilestonedIssueEventPropMilestoneType(TypedDict):
    """MilestonedIssueEventPropMilestone"""

    title: str


__all__ = (
    "MilestonedIssueEventPropMilestoneType",
    "MilestonedIssueEventType",
)
