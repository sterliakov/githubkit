"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0427 import EnterpriseWebhooksType
from .group_0428 import SimpleInstallationType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0430 import RepositoryWebhooksType


class WebhookPullRequestReviewRequestRemovedOneof0Type(TypedDict):
    """WebhookPullRequestReviewRequestRemovedOneof0"""

    action: Literal["review_request_removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestType
    repository: RepositoryWebhooksType
    requested_reviewer: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropRequestedReviewerType, None
    ]
    sender: SimpleUserType


class WebhookPullRequestReviewRequestRemovedOneof0PropRequestedReviewerType(TypedDict):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestType(TypedDict):
    """Pull Request"""

    links: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    additions: NotRequired[int]
    assignee: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneeType,
        None,
    ]
    assignees: list[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneesItemsType,
            None,
        ]
    ]
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
    auto_merge: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergeType,
        None,
    ]
    base: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBaseType
    body: Union[str, None]
    changed_files: NotRequired[int]
    closed_at: Union[datetime, None]
    comments: NotRequired[int]
    comments_url: str
    commits: NotRequired[int]
    commits_url: str
    created_at: datetime
    deletions: NotRequired[int]
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: list[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLabelsItemsType
    ]
    locked: bool
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Union[str, None]
    mergeable: NotRequired[Union[bool, None]]
    mergeable_state: NotRequired[str]
    merged: NotRequired[Union[bool, None]]
    merged_at: Union[datetime, None]
    merged_by: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMergedByType,
            None,
        ]
    ]
    milestone: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestoneType,
        None,
    ]
    node_id: str
    number: int
    patch_url: str
    rebaseable: NotRequired[Union[bool, None]]
    requested_reviewers: list[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: list[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments: NotRequired[int]
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: datetime
    url: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropUserType, None
    ]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneeType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneesItemsType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergeType(
    TypedDict
):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergePropEnabledByType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLabelsItemsType(
    TypedDict
):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMergedByType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestoneType(
    TypedDict
):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestonePropCreatorType,
        None,
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestonePropCreatorType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinks"""

    comments: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommentsType
    commits: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommitsType
    html: (
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropHtmlType
    )
    issue: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentsType
    self_: (
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropSelfType
    )
    statuses: WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropStatusesType


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBaseType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBase"""

    label: str
    ref: str
    repo: (
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoType
    )
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropUserType,
        None,
    ]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropP
    ermissions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHead"""

    label: str
    ref: str
    repo: (
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoType
    )
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropUserType,
        None,
    ]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropP
    ermissions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewer
    sItemsOneof1PropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsIte
    msPropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropBaseType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropHeadType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropLinksType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMergedByType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestPropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropPullRequestType",
    "WebhookPullRequestReviewRequestRemovedOneof0PropRequestedReviewerType",
    "WebhookPullRequestReviewRequestRemovedOneof0Type",
)
