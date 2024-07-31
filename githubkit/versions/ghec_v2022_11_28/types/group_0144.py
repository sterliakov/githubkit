"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0145 import RepositoryRulePullRequestPropParametersType


class RepositoryRulePullRequestType(TypedDict):
    """pull_request

    Require all commits be made to a non-target branch and submitted via a pull
    request before they can be merged.
    """

    type: Literal["pull_request"]
    parameters: NotRequired[RepositoryRulePullRequestPropParametersType]


__all__ = ("RepositoryRulePullRequestType",)
