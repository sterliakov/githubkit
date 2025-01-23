"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0085 import TeamSimpleType


class UserRoleAssignmentType(TypedDict):
    """A Role Assignment for a User

    The Relationship a User has with a role.
    """

    assignment: NotRequired[Literal["direct", "indirect", "mixed"]]
    inherited_from: NotRequired[builtins.list[TeamSimpleType]]
    name: NotRequired[Union[str, None]]
    email: NotRequired[Union[str, None]]
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: Union[str, None]
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    starred_at: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = ("UserRoleAssignmentType",)
