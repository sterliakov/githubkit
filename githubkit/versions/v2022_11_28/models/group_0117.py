"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty(
    GitHubModel
):
    """RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty"""

    include: Missing[list[RepositoryRulesetConditionsRepositoryPropertySpec]] = Field(
        default=UNSET,
        description="The repository properties and values to include. All of these properties must match for the condition to pass.",
    )
    exclude: Missing[list[RepositoryRulesetConditionsRepositoryPropertySpec]] = Field(
        default=UNSET,
        description="The repository properties and values to exclude. The condition will not pass if any of these properties match.",
    )


class RepositoryRulesetConditionsRepositoryPropertySpec(GitHubModel):
    """Repository ruleset property targeting definition

    Parameters for a targeting a repository property
    """

    name: str = Field(description="The name of the repository property to target")
    property_values: list[str] = Field(
        description="The values to match for the repository property"
    )
    source: Missing[Literal["custom", "system"]] = Field(
        default=UNSET,
        description="The source of the repository property. Defaults to 'custom' if not specified.",
    )


model_rebuild(RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty)
model_rebuild(RepositoryRulesetConditionsRepositoryPropertySpec)

__all__ = (
    "RepositoryRulesetConditionsRepositoryPropertySpec",
    "RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryProperty",
)
