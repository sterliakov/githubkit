"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0145 import RepositoryRuleBranchNamePatternPropParametersType


class RepositoryRuleDetailedOneof13Type(TypedDict):
    """RepositoryRuleDetailedOneof13"""

    type: Literal["branch_name_pattern"]
    parameters: NotRequired[RepositoryRuleBranchNamePatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof13Type",)
