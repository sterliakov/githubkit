"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class OrgsOrgActionsVariablesGetResponse200Type(TypedDict):
    """OrgsOrgActionsVariablesGetResponse200"""

    total_count: int
    variables: list[OrganizationActionsVariableType]


class OrganizationActionsVariableType(TypedDict):
    """Actions Variable for an Organization

    Organization variable for GitHub Actions.
    """

    name: str
    value: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: NotRequired[str]


__all__ = (
    "OrganizationActionsVariableType",
    "OrgsOrgActionsVariablesGetResponse200Type",
)
