"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class TeamsTeamIdTeamSyncGroupMappingsPatchBody(GitHubModel):
    """TeamsTeamIdTeamSyncGroupMappingsPatchBody"""

    groups: list[TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems] = Field(
        description="The IdP groups you want to connect to a GitHub team. When updating, the new `groups` object will replace the original one. You must include any existing groups that you don't want to remove."
    )
    synced_at: Missing[str] = Field(default=UNSET)


class TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems(GitHubModel):
    """TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems"""

    group_id: str = Field(description="ID of the IdP group.")
    group_name: str = Field(description="Name of the IdP group.")
    group_description: str = Field(description="Description of the IdP group.")
    id: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)


model_rebuild(TeamsTeamIdTeamSyncGroupMappingsPatchBody)
model_rebuild(TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems)

__all__ = (
    "TeamsTeamIdTeamSyncGroupMappingsPatchBody",
    "TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems",
)
