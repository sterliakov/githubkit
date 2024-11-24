"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class OrgsOrgActionsVariablesGetResponse200(GitHubModel):
    """OrgsOrgActionsVariablesGetResponse200"""

    total_count: int = Field()
    variables: list[OrganizationActionsVariable] = Field()


class OrganizationActionsVariable(GitHubModel):
    """Actions Variable for an Organization

    Organization variable for GitHub Actions.
    """

    name: str = Field(description="The name of the variable.")
    value: str = Field(description="The value of the variable.")
    created_at: datetime = Field(
        description="The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    visibility: Literal["all", "private", "selected"] = Field(
        description="Visibility of a variable"
    )
    selected_repositories_url: Missing[str] = Field(default=UNSET)


model_rebuild(OrgsOrgActionsVariablesGetResponse200)
model_rebuild(OrganizationActionsVariable)

__all__ = (
    "OrganizationActionsVariable",
    "OrgsOrgActionsVariablesGetResponse200",
)
