"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookForkPropForkeeAllof1Type(TypedDict):
    """WebhookForkPropForkeeAllof1"""

    allow_forking: NotRequired[bool]
    archive_url: NotRequired[str]
    archived: NotRequired[bool]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    clone_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    created_at: NotRequired[str]
    default_branch: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[Union[str, None]]
    disabled: NotRequired[bool]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[Literal[True]]
    forks: NotRequired[int]
    forks_count: NotRequired[int]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    git_url: NotRequired[str]
    has_downloads: NotRequired[bool]
    has_issues: NotRequired[bool]
    has_pages: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    homepage: NotRequired[Union[str, None]]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    is_template: NotRequired[bool]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    language: NotRequired[None]
    languages_url: NotRequired[str]
    license_: NotRequired[Union[WebhookForkPropForkeeAllof1PropLicenseType, None]]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    mirror_url: NotRequired[None]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    open_issues: NotRequired[int]
    open_issues_count: NotRequired[int]
    owner: NotRequired[WebhookForkPropForkeeAllof1PropOwnerType]
    private: NotRequired[bool]
    public: NotRequired[bool]
    pulls_url: NotRequired[str]
    pushed_at: NotRequired[str]
    releases_url: NotRequired[str]
    size: NotRequired[int]
    ssh_url: NotRequired[str]
    stargazers_count: NotRequired[int]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    svn_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    topics: NotRequired[list[Union[str, None]]]
    trees_url: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    visibility: NotRequired[str]
    watchers: NotRequired[int]
    watchers_count: NotRequired[int]


class WebhookForkPropForkeeAllof1PropLicenseType(TypedDict):
    """WebhookForkPropForkeeAllof1PropLicense"""


class WebhookForkPropForkeeAllof1PropOwnerType(TypedDict):
    """WebhookForkPropForkeeAllof1PropOwner"""

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


__all__ = (
    "WebhookForkPropForkeeAllof1PropLicenseType",
    "WebhookForkPropForkeeAllof1PropOwnerType",
    "WebhookForkPropForkeeAllof1Type",
)
