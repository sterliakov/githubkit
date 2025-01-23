"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0220 import Job


class ReposOwnerRepoActionsRunsRunIdJobsGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsRunsRunIdJobsGetResponse200"""

    total_count: int = Field()
    jobs: builtins.list[Job] = Field()


model_rebuild(ReposOwnerRepoActionsRunsRunIdJobsGetResponse200)

__all__ = ("ReposOwnerRepoActionsRunsRunIdJobsGetResponse200",)
