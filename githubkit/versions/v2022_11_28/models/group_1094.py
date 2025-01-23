"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoPullsPullNumberRequestedReviewersPostBodyAnyof0(GitHubModel):
    """ReposOwnerRepoPullsPullNumberRequestedReviewersPostBodyAnyof0"""

    reviewers: builtins.list[str] = Field(
        description="An array of user `login`s that will be requested."
    )
    team_reviewers: Missing[builtins.list[str]] = Field(
        default=UNSET, description="An array of team `slug`s that will be requested."
    )


model_rebuild(ReposOwnerRepoPullsPullNumberRequestedReviewersPostBodyAnyof0)

__all__ = ("ReposOwnerRepoPullsPullNumberRequestedReviewersPostBodyAnyof0",)
