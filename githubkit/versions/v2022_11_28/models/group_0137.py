"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleParamsRequiredReviewerConfiguration(GitHubModel):
    """RequiredReviewerConfiguration

    A reviewing team, and file patterns describing which files they must approve
    changes to.
    """

    file_patterns: builtins.list[str] = Field(
        description="Array of file patterns. Pull requests which change matching files must be approved by the specified team. File patterns use the same syntax as `.gitignore` files."
    )
    minimum_approvals: int = Field(
        description="Minimum number of approvals required from the specified team. If set to zero, the team will be added to the pull request but approval is optional."
    )
    reviewer_id: str = Field(
        description="Node ID of the team which must review changes to matching files."
    )


model_rebuild(RepositoryRuleParamsRequiredReviewerConfiguration)

__all__ = ("RepositoryRuleParamsRequiredReviewerConfiguration",)
