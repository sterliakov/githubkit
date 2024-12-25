"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0444 import EnterpriseWebhooksType
from .group_0445 import SimpleInstallationType
from .group_0446 import OrganizationSimpleWebhooksType
from .group_0447 import RepositoryWebhooksType


class WebhookIssuesDeletedType(TypedDict):
    """issues deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    issue: WebhookIssuesDeletedPropIssueType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookIssuesDeletedPropIssueType(TypedDict):
    """Issue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    assignee: NotRequired[Union[WebhookIssuesDeletedPropIssuePropAssigneeType, None]]
    assignees: list[Union[WebhookIssuesDeletedPropIssuePropAssigneesItemsType, None]]
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
    body: Union[str, None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: NotRequired[list[WebhookIssuesDeletedPropIssuePropLabelsItemsType]]
    labels_url: str
    locked: NotRequired[bool]
    milestone: Union[WebhookIssuesDeletedPropIssuePropMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[WebhookIssuesDeletedPropIssuePropPullRequestType]
    reactions: WebhookIssuesDeletedPropIssuePropReactionsType
    repository_url: str
    sub_issues_summary: NotRequired[
        WebhookIssuesDeletedPropIssuePropSubIssuesSummaryType
    ]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: Union[WebhookIssuesDeletedPropIssuePropUserType, None]


class WebhookIssuesDeletedPropIssuePropAssigneeType(TypedDict):
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


class WebhookIssuesDeletedPropIssuePropAssigneesItemsType(TypedDict):
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


class WebhookIssuesDeletedPropIssuePropLabelsItemsType(TypedDict):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookIssuesDeletedPropIssuePropMilestoneType(TypedDict):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[WebhookIssuesDeletedPropIssuePropMilestonePropCreatorType, None]
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


class WebhookIssuesDeletedPropIssuePropMilestonePropCreatorType(TypedDict):
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


class WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppType(TypedDict):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    name: str
    node_id: str
    owner: Union[
        WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropOwnerType, None
    ]
    permissions: NotRequired[
        WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropOwnerType(TypedDict):
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


class WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropPermissionsType(
    TypedDict
):
    """WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class WebhookIssuesDeletedPropIssuePropPullRequestType(TypedDict):
    """WebhookIssuesDeletedPropIssuePropPullRequest"""

    diff_url: NotRequired[str]
    html_url: NotRequired[str]
    merged_at: NotRequired[Union[datetime, None]]
    patch_url: NotRequired[str]
    url: NotRequired[str]


class WebhookIssuesDeletedPropIssuePropReactionsType(TypedDict):
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


class WebhookIssuesDeletedPropIssuePropSubIssuesSummaryType(TypedDict):
    """Sub-issues Summary"""

    total: int
    completed: int
    percent_completed: int


class WebhookIssuesDeletedPropIssuePropUserType(TypedDict):
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
    "WebhookIssuesDeletedPropIssuePropAssigneeType",
    "WebhookIssuesDeletedPropIssuePropAssigneesItemsType",
    "WebhookIssuesDeletedPropIssuePropLabelsItemsType",
    "WebhookIssuesDeletedPropIssuePropMilestonePropCreatorType",
    "WebhookIssuesDeletedPropIssuePropMilestoneType",
    "WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropOwnerType",
    "WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppPropPermissionsType",
    "WebhookIssuesDeletedPropIssuePropPerformedViaGithubAppType",
    "WebhookIssuesDeletedPropIssuePropPullRequestType",
    "WebhookIssuesDeletedPropIssuePropReactionsType",
    "WebhookIssuesDeletedPropIssuePropSubIssuesSummaryType",
    "WebhookIssuesDeletedPropIssuePropUserType",
    "WebhookIssuesDeletedPropIssueType",
    "WebhookIssuesDeletedType",
)
