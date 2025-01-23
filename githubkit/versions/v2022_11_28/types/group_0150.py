"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0151 import RepositoryRuleTagNamePatternPropParametersType


class RepositoryRuleTagNamePatternType(TypedDict):
    """tag_name_pattern

    Parameters to be used for the tag_name_pattern rule
    """

    type: Literal["tag_name_pattern"]
    parameters: NotRequired[RepositoryRuleTagNamePatternPropParametersType]


__all__ = ("RepositoryRuleTagNamePatternType",)
