"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgCodespacesSecretsGetResponse200(GitHubModel):
    """OrgsOrgCodespacesSecretsGetResponse200"""

    total_count: int = Field()
    secrets: builtins.list[CodespacesOrgSecret] = Field()


class CodespacesOrgSecret(GitHubModel):
    """Codespaces Secret

    Secrets for a GitHub Codespace.
    """

    name: str = Field(description="The name of the secret")
    created_at: datetime = Field(
        description="The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    visibility: Literal["all", "private", "selected"] = Field(
        description="The type of repositories in the organization that the secret is visible to"
    )
    selected_repositories_url: Missing[str] = Field(
        default=UNSET,
        description="The API URL at which the list of repositories this secret is visible to can be retrieved",
    )


model_rebuild(OrgsOrgCodespacesSecretsGetResponse200)
model_rebuild(CodespacesOrgSecret)

__all__ = (
    "CodespacesOrgSecret",
    "OrgsOrgCodespacesSecretsGetResponse200",
)
