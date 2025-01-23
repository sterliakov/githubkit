"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0113 import RepositoryRuleBranchNamePatternPropParameters


class RepositoryRuleBranchNamePattern(GitHubModel):
    """branch_name_pattern

    Parameters to be used for the branch_name_pattern rule
    """

    type: Literal["branch_name_pattern"] = Field()
    parameters: Missing[RepositoryRuleBranchNamePatternPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleBranchNamePattern)

__all__ = ("RepositoryRuleBranchNamePattern",)
