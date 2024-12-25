"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType


class EnvironmentApprovalsType(TypedDict):
    """Environment Approval

    An entry in the reviews log for environment deployments
    """

    environments: list[EnvironmentApprovalsPropEnvironmentsItemsType]
    state: Literal["approved", "rejected", "pending"]
    user: SimpleUserType
    comment: str


class EnvironmentApprovalsPropEnvironmentsItemsType(TypedDict):
    """EnvironmentApprovalsPropEnvironmentsItems"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


__all__ = (
    "EnvironmentApprovalsPropEnvironmentsItemsType",
    "EnvironmentApprovalsType",
)
