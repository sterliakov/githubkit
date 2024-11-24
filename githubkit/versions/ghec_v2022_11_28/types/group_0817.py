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
from .group_0437 import WebhooksWorkflowType


class WebhookWorkflowRunRequestedType(TypedDict):
    """workflow_run requested event"""

    action: Literal["requested"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow: Union[WebhooksWorkflowType, None]
    workflow_run: WebhookWorkflowRunRequestedPropWorkflowRunType


class WebhookWorkflowRunRequestedPropWorkflowRunType(TypedDict):
    """Workflow Run"""

    actor: Union[WebhookWorkflowRunRequestedPropWorkflowRunPropActorType, None]
    artifacts_url: str
    cancel_url: str
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: str
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
            "startup_failure",
        ],
    ]
    created_at: datetime
    event: str
    head_branch: Union[str, None]
    head_commit: WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitType
    head_repository: WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryType
    head_sha: str
    html_url: str
    id: int
    jobs_url: str
    logs_url: str
    name: Union[str, None]
    node_id: str
    path: str
    previous_attempt_url: Union[str, None]
    pull_requests: list[
        WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            list[
                WebhookWorkflowRunRequestedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryType
    rerun_url: str
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "pending", "waiting"
    ]
    triggering_actor: Union[
        WebhookWorkflowRunRequestedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: str
    display_title: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropActorType(TypedDict):
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


class WebhookWorkflowRunRequestedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookWorkflowRunRequestedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropTriggeringActorType(TypedDict):
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


class WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitType(TypedDict):
    """SimpleCommit"""

    author: WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropAuthorType
    committer: WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropCommitterType
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropCommitterType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType(
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


class WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryType(TypedDict):
    """Repository Lite"""

    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    description: Union[str, None]
    downloads_url: str
    events_url: str
    fork: bool
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    hooks_url: str
    html_url: str
    id: int
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    name: str
    node_id: str
    notifications_url: str
    owner: Union[
        WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryPropOwnerType, None
    ]
    private: bool
    pulls_url: str
    releases_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    url: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryPropOwnerType(TypedDict):
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


class WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsType(TypedDict):
    """WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItems"""

    base: WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType
    id: float
    number: float
    url: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookWorkflowRunRequestedPropWorkflowRunPropActorType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropAuthorType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitPropCommitterType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropHeadCommitType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropHeadRepositoryType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropRepositoryType",
    "WebhookWorkflowRunRequestedPropWorkflowRunPropTriggeringActorType",
    "WebhookWorkflowRunRequestedPropWorkflowRunType",
    "WebhookWorkflowRunRequestedType",
)
