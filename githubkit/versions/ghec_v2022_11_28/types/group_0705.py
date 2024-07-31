"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0408 import EnterpriseWebhooksType
from .group_0409 import SimpleInstallationType
from .group_0411 import RepositoryWebhooksType
from .group_0412 import SimpleUserWebhooksType
from .group_0410 import OrganizationSimpleWebhooksType


class WebhookPullRequestReviewThreadResolvedType(TypedDict):
    """pull_request_review_thread resolved event"""

    action: Literal["resolved"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewThreadResolvedPropPullRequestType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]
    thread: WebhookPullRequestReviewThreadResolvedPropThreadType


class WebhookPullRequestReviewThreadResolvedPropPullRequestType(TypedDict):
    """Simple Pull Request"""

    links: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneeType, None
    ]
    assignees: List[
        Union[
            WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneesItemsType,
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
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergeType, None
    ]
    base: WebhookPullRequestReviewThreadResolvedPropPullRequestPropBaseType
    body: Union[str, None]
    closed_at: Union[str, None]
    comments_url: str
    commits_url: str
    created_at: str
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropLabelsItemsType
    ]
    locked: bool
    merge_commit_sha: Union[str, None]
    merged_at: Union[str, None]
    milestone: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    requested_reviewers: List[
        Union[
            WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: str
    url: str
    user: Union[WebhookPullRequestReviewThreadResolvedPropPullRequestPropUserType, None]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneeType(TypedDict):
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneesItemsType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergeType(TypedDict):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergePropEnabledByType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLabelsItemsType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestonePropCreatorType,
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestonePropCreatorType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof0Type(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropUserType(TypedDict):
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinks"""

    comments: (
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommentsType
    )
    commits: (
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommitsType
    )
    html: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentsType
    self_: WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropSelfType
    statuses: (
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropStatusesType
    )


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropUserType, None
    ]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropUserType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoType(
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
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropLicenseType,
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
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropPermissionsType
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
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropOwnerType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropPermiss
    ions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropHead"""

    label: Union[str, None]
    ref: str
    repo: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoType, None
    ]
    sha: str
    user: Union[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropUserType, None
    ]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoType(
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
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropLicenseType,
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
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropPermissionsType
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
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropOwnerType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropPermiss
    ions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropUserType(
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1Type(
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
            WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItems
    Oneof1PropParent
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


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsType(
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
            WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsProp
    Parent
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


class WebhookPullRequestReviewThreadResolvedPropThreadType(TypedDict):
    """WebhookPullRequestReviewThreadResolvedPropThread"""

    comments: List[
        WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsType
    ]
    node_id: str


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsType(TypedDict):
    """Pull Request Review Comment

    The [comment](https://docs.github.com/enterprise-
    cloud@latest//rest/pulls/comments#get-a-review-comment-for-a-pull-request)
    itself.
    """

    links: (
        WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksType
    )
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
    commit_id: str
    created_at: datetime
    diff_hunk: str
    html_url: str
    id: int
    in_reply_to_id: NotRequired[int]
    line: Union[int, None]
    node_id: str
    original_commit_id: str
    original_line: Union[int, None]
    original_position: int
    original_start_line: Union[int, None]
    path: str
    position: Union[int, None]
    pull_request_review_id: Union[int, None]
    pull_request_url: str
    reactions: WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropReactionsType
    side: Literal["LEFT", "RIGHT"]
    start_line: Union[int, None]
    start_side: Union[None, Literal["LEFT", "RIGHT"]]
    subject_type: NotRequired[Literal["line", "file"]]
    updated_at: datetime
    url: str
    user: Union[
        WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropUserType,
        None,
    ]


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropReactionsType(
    TypedDict
):
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


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropUserType(
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


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksType(
    TypedDict
):
    """WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinks"""

    html: WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropHtmlType
    pull_request: WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType
    self_: WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropSelfType


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


__all__ = (
    "WebhookPullRequestReviewThreadResolvedType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropUserType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBaseType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewThreadResolvedPropPullRequestPropRequestedTeamsItemsPropParentType",
    "WebhookPullRequestReviewThreadResolvedPropThreadType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropReactionsType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropUserType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropHtmlType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropPullRequestType",
    "WebhookPullRequestReviewThreadResolvedPropThreadPropCommentsItemsPropLinksPropSelfType",
)
