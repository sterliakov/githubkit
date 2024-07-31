"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0453 import WebhooksReviewType
from .group_0408 import EnterpriseWebhooksType
from .group_0409 import SimpleInstallationType
from .group_0411 import RepositoryWebhooksType
from .group_0412 import SimpleUserWebhooksType
from .group_0410 import OrganizationSimpleWebhooksType


class WebhookPullRequestReviewEditedType(TypedDict):
    """pull_request_review edited event"""

    action: Literal["edited"]
    changes: WebhookPullRequestReviewEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewEditedPropPullRequestType
    repository: RepositoryWebhooksType
    review: WebhooksReviewType
    sender: SimpleUserWebhooksType


class WebhookPullRequestReviewEditedPropChangesType(TypedDict):
    """WebhookPullRequestReviewEditedPropChanges"""

    body: NotRequired[WebhookPullRequestReviewEditedPropChangesPropBodyType]


class WebhookPullRequestReviewEditedPropChangesPropBodyType(TypedDict):
    """WebhookPullRequestReviewEditedPropChangesPropBody"""

    from_: str


class WebhookPullRequestReviewEditedPropPullRequestType(TypedDict):
    """Simple Pull Request"""

    links: WebhookPullRequestReviewEditedPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: Union[WebhookPullRequestReviewEditedPropPullRequestPropAssigneeType, None]
    assignees: List[
        Union[WebhookPullRequestReviewEditedPropPullRequestPropAssigneesItemsType, None]
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
        WebhookPullRequestReviewEditedPropPullRequestPropAutoMergeType, None
    ]
    base: WebhookPullRequestReviewEditedPropPullRequestPropBaseType
    body: Union[str, None]
    closed_at: Union[str, None]
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewEditedPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[WebhookPullRequestReviewEditedPropPullRequestPropLabelsItemsType]
    locked: bool
    merge_commit_sha: Union[str, None]
    merged_at: Union[str, None]
    milestone: Union[
        WebhookPullRequestReviewEditedPropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: List[
        Union[
            WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Union[WebhookPullRequestReviewEditedPropPullRequestPropUserType, None]


class WebhookPullRequestReviewEditedPropPullRequestPropAssigneeType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropAssigneesItemsType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropAutoMergeType(TypedDict):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewEditedPropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewEditedPropPullRequestPropAutoMergePropEnabledByType(
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


class WebhookPullRequestReviewEditedPropPullRequestPropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewEditedPropPullRequestPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewEditedPropPullRequestPropMilestonePropCreatorType, None
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


class WebhookPullRequestReviewEditedPropPullRequestPropMilestonePropCreatorType(
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof0Type(
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropUserType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestReviewEditedPropPullRequestPropLinks"""

    comments: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommentsType
    commits: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommitsType
    html: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropIssueType
    review_comment: (
        WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentType
    )
    review_comments: (
        WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentsType
    )
    self_: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropSelfType
    statuses: WebhookPullRequestReviewEditedPropPullRequestPropLinksPropStatusesType


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommentsType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommitsType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropHtmlType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropIssueType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropSelfType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropLinksPropStatusesType(TypedDict):
    """Link"""

    href: str


class WebhookPullRequestReviewEditedPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestReviewEditedPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[WebhookPullRequestReviewEditedPropPullRequestPropBasePropUserType, None]


class WebhookPullRequestReviewEditedPropPullRequestPropBasePropUserType(TypedDict):
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


class WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoType(TypedDict):
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
        WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
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
        WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
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
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropOwnerType(
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


class WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewEditedPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestReviewEditedPropPullRequestPropHead"""

    label: str
    ref: str
    repo: Union[WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoType, None]
    sha: str
    user: Union[WebhookPullRequestReviewEditedPropPullRequestPropHeadPropUserType, None]


class WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoType(TypedDict):
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
        WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
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
        WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
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
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropOwnerType(
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


class WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewEditedPropPullRequestPropHeadPropUserType(TypedDict):
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


class WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1Type(
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
            WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1Pr
    opParent
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


class WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsPropParent"""

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
    "WebhookPullRequestReviewEditedType",
    "WebhookPullRequestReviewEditedPropChangesType",
    "WebhookPullRequestReviewEditedPropChangesPropBodyType",
    "WebhookPullRequestReviewEditedPropPullRequestType",
    "WebhookPullRequestReviewEditedPropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewEditedPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewEditedPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewEditedPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewEditedPropPullRequestPropUserType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewEditedPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBaseType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewEditedPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewEditedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewEditedPropPullRequestPropRequestedTeamsItemsPropParentType",
)
