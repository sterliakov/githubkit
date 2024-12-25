"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0141 import RepositoryRuleCommitAuthorEmailPatternPropParametersType


class RepositoryRuleCommitAuthorEmailPatternType(TypedDict):
    """commit_author_email_pattern

    Parameters to be used for the commit_author_email_pattern rule
    """

    type: Literal["commit_author_email_pattern"]
    parameters: NotRequired[RepositoryRuleCommitAuthorEmailPatternPropParametersType]


__all__ = ("RepositoryRuleCommitAuthorEmailPatternType",)
