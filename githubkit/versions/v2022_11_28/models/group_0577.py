"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0398 import EnterpriseWebhooks
from .group_0399 import SimpleInstallation
from .group_0400 import OrganizationSimpleWebhooks
from .group_0401 import RepositoryWebhooks
from .group_0419 import WebhooksMilestone


class WebhookIssuesDemilestoned(GitHubModel):
    """issues demilestoned event"""

    action: Literal["demilestoned"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    issue: WebhookIssuesDemilestonedPropIssue = Field(
        title="Issue",
        description="The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.",
    )
    milestone: Missing[WebhooksMilestone] = Field(
        default=UNSET,
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookIssuesDemilestonedPropIssue(GitHubModel):
    """Issue

    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ] = Field()
    assignee: Missing[Union[WebhookIssuesDemilestonedPropIssuePropAssignee, None]] = (
        Field(default=UNSET, title="User")
    )
    assignees: builtins.list[
        Union[WebhookIssuesDemilestonedPropIssuePropAssigneesItems, None]
    ] = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[str, None] = Field(description="Contents of the issue")
    closed_at: Union[datetime, None] = Field()
    comments: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    draft: Missing[bool] = Field(default=UNSET)
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: Missing[
        builtins.list[Union[WebhookIssuesDemilestonedPropIssuePropLabelsItems, None]]
    ] = Field(default=UNSET)
    labels_url: str = Field()
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Union[WebhookIssuesDemilestonedPropIssuePropMilestone, None] = Field(
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    node_id: str = Field()
    number: int = Field()
    performed_via_github_app: Missing[
        Union[WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubApp, None]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    pull_request: Missing[WebhookIssuesDemilestonedPropIssuePropPullRequest] = Field(
        default=UNSET
    )
    reactions: WebhookIssuesDemilestonedPropIssuePropReactions = Field(
        title="Reactions"
    )
    repository_url: str = Field()
    sub_issues_summary: Missing[
        WebhookIssuesDemilestonedPropIssuePropSubIssuesSummary
    ] = Field(default=UNSET, title="Sub-issues Summary")
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET, description="State of the issue; either 'open' or 'closed'"
    )
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field(description="Title of the issue")
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue")
    user: Union[WebhookIssuesDemilestonedPropIssuePropUser, None] = Field(title="User")


class WebhookIssuesDemilestonedPropIssuePropAssignee(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropAssigneesItems(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropLabelsItems(GitHubModel):
    """Label"""

    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()
    description: Union[str, None] = Field()
    id: int = Field()
    name: str = Field(description="The name of the label.")
    node_id: str = Field()
    url: str = Field(description="URL for the label")


class WebhookIssuesDemilestonedPropIssuePropMilestone(GitHubModel):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None] = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    creator: Union[WebhookIssuesDemilestonedPropIssuePropMilestonePropCreator, None] = (
        Field(title="User")
    )
    description: Union[str, None] = Field()
    due_on: Union[datetime, None] = Field()
    html_url: str = Field()
    id: int = Field()
    labels_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    open_issues: int = Field()
    state: Literal["open", "closed"] = Field(description="The state of the milestone.")
    title: str = Field(description="The title of the milestone.")
    updated_at: datetime = Field()
    url: str = Field()


class WebhookIssuesDemilestonedPropIssuePropMilestonePropCreator(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubApp(GitHubModel):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[builtins.list[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropOwner, None
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropOwner(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropPermissions(
    GitHubModel
):
    """WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    administration: Missing[Literal["read", "write"]] = Field(default=UNSET)
    checks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    content_references: Missing[Literal["read", "write"]] = Field(default=UNSET)
    contents: Missing[Literal["read", "write"]] = Field(default=UNSET)
    deployments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    emails: Missing[Literal["read", "write"]] = Field(default=UNSET)
    environments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    issues: Missing[Literal["read", "write"]] = Field(default=UNSET)
    keys: Missing[Literal["read", "write"]] = Field(default=UNSET)
    members: Missing[Literal["read", "write"]] = Field(default=UNSET)
    metadata: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_administration: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_plan: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_projects: Missing[Literal["read", "write", "admin"]] = Field(
        default=UNSET
    )
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropPullRequest(GitHubModel):
    """WebhookIssuesDemilestonedPropIssuePropPullRequest"""

    diff_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    merged_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    patch_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssuePropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookIssuesDemilestonedPropIssuePropSubIssuesSummary(GitHubModel):
    """Sub-issues Summary"""

    total: int = Field()
    completed: int = Field()
    percent_completed: int = Field()


class WebhookIssuesDemilestonedPropIssuePropUser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesDemilestoned)
model_rebuild(WebhookIssuesDemilestonedPropIssue)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropAssignee)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropAssigneesItems)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropLabelsItems)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropMilestone)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropMilestonePropCreator)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubApp)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropOwner)
model_rebuild(
    WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropPermissions
)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropPullRequest)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropReactions)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropSubIssuesSummary)
model_rebuild(WebhookIssuesDemilestonedPropIssuePropUser)

__all__ = (
    "WebhookIssuesDemilestoned",
    "WebhookIssuesDemilestonedPropIssue",
    "WebhookIssuesDemilestonedPropIssuePropAssignee",
    "WebhookIssuesDemilestonedPropIssuePropAssigneesItems",
    "WebhookIssuesDemilestonedPropIssuePropLabelsItems",
    "WebhookIssuesDemilestonedPropIssuePropMilestone",
    "WebhookIssuesDemilestonedPropIssuePropMilestonePropCreator",
    "WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubApp",
    "WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropOwner",
    "WebhookIssuesDemilestonedPropIssuePropPerformedViaGithubAppPropPermissions",
    "WebhookIssuesDemilestonedPropIssuePropPullRequest",
    "WebhookIssuesDemilestonedPropIssuePropReactions",
    "WebhookIssuesDemilestonedPropIssuePropSubIssuesSummary",
    "WebhookIssuesDemilestonedPropIssuePropUser",
)
