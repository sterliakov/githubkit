"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0006 import IntegrationType
from .group_0171 import SimpleCommitType
from .group_0055 import MinimalRepositoryType
from .group_0170 import PullRequestMinimalType


class CheckSuiteType(TypedDict):
    """CheckSuite

    A suite of checks performed on the code of a given code change
    """

    id: int
    node_id: str
    head_branch: Union[str, None]
    head_sha: str
    status: Union[
        None,
        Literal[
            "queued", "in_progress", "completed", "waiting", "requested", "pending"
        ],
    ]
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
            "startup_failure",
            "stale",
        ],
    ]
    url: Union[str, None]
    before: Union[str, None]
    after: Union[str, None]
    pull_requests: Union[List[PullRequestMinimalType], None]
    app: Union[None, IntegrationType, None]
    repository: MinimalRepositoryType
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    head_commit: SimpleCommitType
    latest_check_runs_count: int
    check_runs_url: str
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]


class ReposOwnerRepoCommitsRefCheckSuitesGetResponse200Type(TypedDict):
    """ReposOwnerRepoCommitsRefCheckSuitesGetResponse200"""

    total_count: int
    check_suites: List[CheckSuiteType]


__all__ = (
    "CheckSuiteType",
    "ReposOwnerRepoCommitsRefCheckSuitesGetResponse200Type",
)
