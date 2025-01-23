"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class TeamsTeamIdTeamSyncGroupMappingsPatchBodyType(TypedDict):
    """TeamsTeamIdTeamSyncGroupMappingsPatchBody"""

    groups: builtins.list[TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItemsType]
    synced_at: NotRequired[str]


class TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItemsType(TypedDict):
    """TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItems"""

    group_id: str
    group_name: str
    group_description: str
    id: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]


__all__ = (
    "TeamsTeamIdTeamSyncGroupMappingsPatchBodyPropGroupsItemsType",
    "TeamsTeamIdTeamSyncGroupMappingsPatchBodyType",
)
