"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_1056 import (
    ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType,
    ReposOwnerRepoCheckRunsPostBodyPropOutputType,
)


class ReposOwnerRepoCheckRunsPostBodyOneof1Type(TypedDict):
    """ReposOwnerRepoCheckRunsPostBodyOneof1"""

    name: str
    head_sha: str
    details_url: NotRequired[str]
    external_id: NotRequired[str]
    status: NotRequired[
        Literal["queued", "in_progress", "waiting", "requested", "pending"]
    ]
    started_at: NotRequired[datetime]
    conclusion: NotRequired[
        Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ]
    ]
    completed_at: NotRequired[datetime]
    output: NotRequired[ReposOwnerRepoCheckRunsPostBodyPropOutputType]
    actions: NotRequired[list[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]]


__all__ = ("ReposOwnerRepoCheckRunsPostBodyOneof1Type",)
