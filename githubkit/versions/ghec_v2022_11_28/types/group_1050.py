"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import TypedDict

from .group_0220 import JobType


class ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200"""

    total_count: int
    jobs: builtins.list[JobType]


__all__ = ("ReposOwnerRepoActionsRunsRunIdAttemptsAttemptNumberJobsGetResponse200Type",)
