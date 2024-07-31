"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0066 import Runner


class ReposOwnerRepoActionsRunnersGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsRunnersGetResponse200"""

    total_count: int = Field()
    runners: List[Runner] = Field()


model_rebuild(ReposOwnerRepoActionsRunnersGetResponse200)

__all__ = ("ReposOwnerRepoActionsRunnersGetResponse200",)
