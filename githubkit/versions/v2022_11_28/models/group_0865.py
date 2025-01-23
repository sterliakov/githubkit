"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedTeamsPostBody(GitHubModel):
    """OrgsOrgCopilotBillingSelectedTeamsPostBody"""

    selected_teams: builtins.list[str] = Field(
        min_length=1 if PYDANTIC_V2 else None,
        description="List of team names within the organization to which to grant access to GitHub Copilot.",
    )


model_rebuild(OrgsOrgCopilotBillingSelectedTeamsPostBody)

__all__ = ("OrgsOrgCopilotBillingSelectedTeamsPostBody",)
