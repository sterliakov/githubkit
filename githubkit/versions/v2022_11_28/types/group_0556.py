"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookIssuesClosedPropIssueAllof1Type(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1"""

    active_lock_reason: NotRequired[Union[str, None]]
    assignee: NotRequired[
        Union[WebhookIssuesClosedPropIssueAllof1PropAssigneeType, None]
    ]
    assignees: NotRequired[
        list[Union[WebhookIssuesClosedPropIssueAllof1PropAssigneesItemsType, None]]
    ]
    author_association: NotRequired[str]
    body: NotRequired[Union[str, None]]
    closed_at: Union[str, None]
    comments: NotRequired[int]
    comments_url: NotRequired[str]
    created_at: NotRequired[str]
    events_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    labels: NotRequired[
        list[Union[WebhookIssuesClosedPropIssueAllof1PropLabelsItemsType, None]]
    ]
    labels_url: NotRequired[str]
    locked: NotRequired[bool]
    milestone: NotRequired[
        Union[WebhookIssuesClosedPropIssueAllof1PropMilestoneType, None]
    ]
    node_id: NotRequired[str]
    number: NotRequired[int]
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubAppType, None]
    ]
    reactions: NotRequired[WebhookIssuesClosedPropIssueAllof1PropReactionsType]
    repository_url: NotRequired[str]
    state: Literal["closed", "open"]
    timeline_url: NotRequired[str]
    title: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    user: NotRequired[WebhookIssuesClosedPropIssueAllof1PropUserType]


class WebhookIssuesClosedPropIssueAllof1PropAssigneeType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropAssignee"""


class WebhookIssuesClosedPropIssueAllof1PropAssigneesItemsType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesClosedPropIssueAllof1PropLabelsItemsType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesClosedPropIssueAllof1PropMilestoneType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropMilestone"""


class WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubAppType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesClosedPropIssueAllof1PropReactionsType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropReactions"""

    plus_one: NotRequired[int]
    minus_one: NotRequired[int]
    confused: NotRequired[int]
    eyes: NotRequired[int]
    heart: NotRequired[int]
    hooray: NotRequired[int]
    laugh: NotRequired[int]
    rocket: NotRequired[int]
    total_count: NotRequired[int]
    url: NotRequired[str]


class WebhookIssuesClosedPropIssueAllof1PropUserType(TypedDict):
    """WebhookIssuesClosedPropIssueAllof1PropUser"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookIssuesClosedPropIssueAllof1PropAssigneeType",
    "WebhookIssuesClosedPropIssueAllof1PropAssigneesItemsType",
    "WebhookIssuesClosedPropIssueAllof1PropLabelsItemsType",
    "WebhookIssuesClosedPropIssueAllof1PropMilestoneType",
    "WebhookIssuesClosedPropIssueAllof1PropPerformedViaGithubAppType",
    "WebhookIssuesClosedPropIssueAllof1PropReactionsType",
    "WebhookIssuesClosedPropIssueAllof1PropUserType",
    "WebhookIssuesClosedPropIssueAllof1Type",
)
