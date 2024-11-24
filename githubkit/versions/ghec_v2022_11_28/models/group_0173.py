"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0174 import RepositoryRuleTagNamePatternPropParameters


class RepositoryRuleTagNamePattern(GitHubModel):
    """tag_name_pattern

    Parameters to be used for the tag_name_pattern rule
    """

    type: Literal["tag_name_pattern"] = Field()
    parameters: Missing[RepositoryRuleTagNamePatternPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleTagNamePattern)

__all__ = ("RepositoryRuleTagNamePattern",)
