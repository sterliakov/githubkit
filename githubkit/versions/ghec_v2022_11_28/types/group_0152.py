"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0153 import RepositoryRuleCommitterEmailPatternPropParametersType


class RepositoryRuleCommitterEmailPatternType(TypedDict):
    """committer_email_pattern

    Parameters to be used for the committer_email_pattern rule
    """

    type: Literal["committer_email_pattern"]
    parameters: NotRequired[RepositoryRuleCommitterEmailPatternPropParametersType]


__all__ = ("RepositoryRuleCommitterEmailPatternType",)
