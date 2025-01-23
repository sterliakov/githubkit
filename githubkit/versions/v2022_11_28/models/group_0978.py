"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsDeleteBodyOneof0(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsDeleteBodyOneof0

    Examples:
        {'teams': ['my-team']}
    """

    teams: builtins.list[str] = Field(description="The slug values for teams")


model_rebuild(ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsDeleteBodyOneof0)

__all__ = ("ReposOwnerRepoBranchesBranchProtectionRestrictionsTeamsDeleteBodyOneof0",)
