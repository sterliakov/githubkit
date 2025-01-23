"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoDependabotSecretsGetResponse200(GitHubModel):
    """ReposOwnerRepoDependabotSecretsGetResponse200"""

    total_count: int = Field()
    secrets: builtins.list[DependabotSecret] = Field()


class DependabotSecret(GitHubModel):
    """Dependabot Secret

    Set secrets for Dependabot.
    """

    name: str = Field(description="The name of the secret.")
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(ReposOwnerRepoDependabotSecretsGetResponse200)
model_rebuild(DependabotSecret)

__all__ = (
    "DependabotSecret",
    "ReposOwnerRepoDependabotSecretsGetResponse200",
)
