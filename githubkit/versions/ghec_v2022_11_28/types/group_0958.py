"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0188 import ActionsVariableType


class ReposOwnerRepoActionsOrganizationVariablesGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsOrganizationVariablesGetResponse200"""

    total_count: int
    variables: List[ActionsVariableType]


__all__ = ("ReposOwnerRepoActionsOrganizationVariablesGetResponse200Type",)
