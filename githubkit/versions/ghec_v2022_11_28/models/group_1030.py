"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0217 import ActionsVariable


class ReposOwnerRepoActionsVariablesGetResponse200(GitHubModel):
    """ReposOwnerRepoActionsVariablesGetResponse200"""

    total_count: int = Field()
    variables: list[ActionsVariable] = Field()


model_rebuild(ReposOwnerRepoActionsVariablesGetResponse200)

__all__ = ("ReposOwnerRepoActionsVariablesGetResponse200",)
