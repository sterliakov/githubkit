"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Any, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0002 import SimpleUserType
from .group_0045 import GistHistoryType, GistSimplePropForkOfType


class GistSimpleType(TypedDict):
    """Gist Simple

    Gist Simple
    """

    forks: NotRequired[Union[builtins.list[GistSimplePropForksItemsType], None]]
    history: NotRequired[Union[builtins.list[GistHistoryType], None]]
    fork_of: NotRequired[Union[GistSimplePropForkOfType, None]]
    url: NotRequired[str]
    forks_url: NotRequired[str]
    commits_url: NotRequired[str]
    id: NotRequired[str]
    node_id: NotRequired[str]
    git_pull_url: NotRequired[str]
    git_push_url: NotRequired[str]
    html_url: NotRequired[str]
    files: NotRequired[GistSimplePropFilesType]
    public: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    description: NotRequired[Union[str, None]]
    comments: NotRequired[int]
    comments_enabled: NotRequired[bool]
    user: NotRequired[Union[str, None]]
    comments_url: NotRequired[str]
    owner: NotRequired[SimpleUserType]
    truncated: NotRequired[bool]


GistSimplePropFilesType: TypeAlias = dict[str, Any]
"""GistSimplePropFiles
"""


class GistSimplePropForksItemsType(TypedDict):
    """GistSimplePropForksItems"""

    id: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[PublicUserType]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class PublicUserType(TypedDict):
    """Public User

    Public User
    """

    login: str
    id: int
    user_view_type: NotRequired[str]
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
    name: Union[str, None]
    company: Union[str, None]
    blog: Union[str, None]
    location: Union[str, None]
    email: Union[str, None]
    notification_email: NotRequired[Union[str, None]]
    hireable: Union[bool, None]
    bio: Union[str, None]
    twitter_username: NotRequired[Union[str, None]]
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime
    plan: NotRequired[PublicUserPropPlanType]
    private_gists: NotRequired[int]
    total_private_repos: NotRequired[int]
    owned_private_repos: NotRequired[int]
    disk_usage: NotRequired[int]
    collaborators: NotRequired[int]


class PublicUserPropPlanType(TypedDict):
    """PublicUserPropPlan"""

    collaborators: int
    name: str
    space: int
    private_repos: int


__all__ = (
    "GistSimplePropFilesType",
    "GistSimplePropForksItemsType",
    "GistSimpleType",
    "PublicUserPropPlanType",
    "PublicUserType",
)
