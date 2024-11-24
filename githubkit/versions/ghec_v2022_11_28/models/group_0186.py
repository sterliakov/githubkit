"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class GroupMapping(GitHubModel):
    """GroupMapping

    External Groups to be mapped to a team for membership
    """

    groups: Missing[list[GroupMappingPropGroupsItems]] = Field(
        default=UNSET, description="Array of groups to be mapped to this team"
    )


class GroupMappingPropGroupsItems(GitHubModel):
    """GroupMappingPropGroupsItems"""

    group_id: str = Field(description="The ID of the group")
    group_name: str = Field(description="The name of the group")
    group_description: str = Field(description="a description of the group")
    status: Missing[str] = Field(
        default=UNSET, description="synchronization status for this group mapping"
    )
    synced_at: Missing[Union[str, None]] = Field(
        default=UNSET, description="the time of the last sync for this group-mapping"
    )


model_rebuild(GroupMapping)
model_rebuild(GroupMappingPropGroupsItems)

__all__ = (
    "GroupMapping",
    "GroupMappingPropGroupsItems",
)
