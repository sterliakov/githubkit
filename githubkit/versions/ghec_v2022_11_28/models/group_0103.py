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


class RepositoryRulePullRequestPropParameters(GitHubModel):
    """RepositoryRulePullRequestPropParameters"""

    allowed_merge_methods: Missing[builtins.list[str]] = Field(
        default=UNSET,
        description="When merging pull requests, you can allow any combination of merge commits, squashing, or rebasing. At least one option must be enabled.",
    )
    dismiss_stale_reviews_on_push: bool = Field(
        description="New, reviewable commits pushed will dismiss previous pull request review approvals."
    )
    require_code_owner_review: bool = Field(
        description="Require an approving review in pull requests that modify files that have a designated code owner."
    )
    require_last_push_approval: bool = Field(
        description="Whether the most recent reviewable push must be approved by someone other than the person who pushed it."
    )
    required_approving_review_count: int = Field(
        le=10.0,
        description="The number of approving reviews that are required before a pull request can be merged.",
    )
    required_review_thread_resolution: bool = Field(
        description="All conversations on code must be resolved before a pull request can be merged."
    )


model_rebuild(RepositoryRulePullRequestPropParameters)

__all__ = ("RepositoryRulePullRequestPropParameters",)
