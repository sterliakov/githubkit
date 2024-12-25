"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class BranchShort(GitHubModel):
    """Branch Short

    Branch Short
    """

    name: str = Field()
    commit: BranchShortPropCommit = Field()
    protected: bool = Field()


class BranchShortPropCommit(GitHubModel):
    """BranchShortPropCommit"""

    sha: str = Field()
    url: str = Field()


model_rebuild(BranchShort)
model_rebuild(BranchShortPropCommit)

__all__ = (
    "BranchShort",
    "BranchShortPropCommit",
)
