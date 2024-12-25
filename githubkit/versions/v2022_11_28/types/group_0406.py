"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class DiscussionType(TypedDict):
    """Discussion

    A Discussion in a repository.
    """

    active_lock_reason: Union[str, None]
    answer_chosen_at: Union[str, None]
    answer_chosen_by: Union[DiscussionPropAnswerChosenByType, None]
    answer_html_url: Union[str, None]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: str
    category: DiscussionPropCategoryType
    comments: int
    created_at: datetime
    html_url: str
    id: int
    locked: bool
    node_id: str
    number: int
    reactions: NotRequired[DiscussionPropReactionsType]
    repository_url: str
    state: Literal["open", "closed", "locked", "converting", "transferring"]
    state_reason: Union[None, Literal["resolved", "outdated", "duplicate", "reopened"]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    user: Union[DiscussionPropUserType, None]
    labels: NotRequired[list[LabelType]]


class LabelType(TypedDict):
    """Label

    Color-coded labels help you categorize and filter your issues (just like labels
    in Gmail).
    """

    id: int
    node_id: str
    url: str
    name: str
    description: Union[str, None]
    color: str
    default: bool


class DiscussionPropAnswerChosenByType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class DiscussionPropCategoryType(TypedDict):
    """DiscussionPropCategory"""

    created_at: datetime
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: NotRequired[str]
    repository_id: int
    slug: str
    updated_at: str


class DiscussionPropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class DiscussionPropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "DiscussionPropAnswerChosenByType",
    "DiscussionPropCategoryType",
    "DiscussionPropReactionsType",
    "DiscussionPropUserType",
    "DiscussionType",
    "LabelType",
)
