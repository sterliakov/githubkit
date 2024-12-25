"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0444 import EnterpriseWebhooks
from .group_0445 import SimpleInstallation
from .group_0446 import OrganizationSimpleWebhooks
from .group_0447 import RepositoryWebhooks


class WebhookCheckSuiteRerequested(GitHubModel):
    """check_suite rerequested event"""

    action: Literal["rerequested"] = Field()
    check_suite: WebhookCheckSuiteRerequestedPropCheckSuite = Field(
        description="The [check_suite](https://docs.github.com/enterprise-cloud@latest//rest/checks/suites#get-a-check-suite)."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
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


class WebhookCheckSuiteRerequestedPropCheckSuite(GitHubModel):
    """WebhookCheckSuiteRerequestedPropCheckSuite

    The [check_suite](https://docs.github.com/enterprise-
    cloud@latest//rest/checks/suites#get-a-check-suite).
    """

    after: Union[str, None] = Field()
    app: WebhookCheckSuiteRerequestedPropCheckSuitePropApp = Field(
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    before: Union[str, None] = Field()
    check_runs_url: str = Field()
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
        ],
    ] = Field(
        description="The summary conclusion for all check runs that are part of the check suite. This value will be `null` until the check run has completed."
    )
    created_at: datetime = Field()
    head_branch: Union[str, None] = Field(
        description="The head branch name the changes are on."
    )
    head_commit: WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommit = Field(
        title="SimpleCommit"
    )
    head_sha: str = Field(
        description="The SHA of the head commit that is being checked."
    )
    id: int = Field()
    latest_check_runs_count: int = Field()
    node_id: str = Field()
    pull_requests: list[
        WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItems
    ] = Field(
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_sha` and `head_branch`. When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty."
    )
    rerequestable: Missing[bool] = Field(default=UNSET)
    runs_rerequestable: Missing[bool] = Field(default=UNSET)
    status: Union[None, Literal["requested", "in_progress", "completed", "queued"]] = (
        Field(
            description="The summary status for all check runs that are part of the check suite. Can be `requested`, `in_progress`, or `completed`."
        )
    )
    updated_at: datetime = Field()
    url: str = Field(description="URL that points to the check suite API resource.")


class WebhookCheckSuiteRerequestedPropCheckSuitePropApp(GitHubModel):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[list[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    client_id: Missing[Union[str, None]] = Field(
        default=UNSET, description="The Client ID for the GitHub app"
    )
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropOwner, None] = (
        Field(title="User")
    )
    permissions: Missing[
        WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropOwner(GitHubModel):
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


class WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropPermissions(GitHubModel):
    """WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropPermissions

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
    repository_projects: Missing[Literal["read", "write", "admin"]] = Field(
        default=UNSET
    )
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommit(GitHubModel):
    """SimpleCommit"""

    author: WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropAuthor = Field(
        title="Committer",
        description="Metaproperties for Git author/committer information.",
    )
    committer: WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropCommitter = (
        Field(
            title="Committer",
            description="Metaproperties for Git author/committer information.",
        )
    )
    id: str = Field()
    message: str = Field()
    timestamp: str = Field()
    tree_id: str = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropAuthor(GitHubModel):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropCommitter(
    GitHubModel
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: Missing[datetime] = Field(default=UNSET)
    email: Union[str, None] = Field()
    name: str = Field(description="The git author's name.")
    username: Missing[str] = Field(default=UNSET)


class WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItems(GitHubModel):
    """Check Run Pull Request"""

    base: WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBase = (
        Field()
    )
    head: WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHead = (
        Field()
    )
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookCheckSuiteRerequested)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuite)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropApp)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropOwner)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropPermissions)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommit)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropAuthor)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropCommitter)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItems)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBase)
model_rebuild(
    WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo
)
model_rebuild(WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHead)
model_rebuild(
    WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookCheckSuiteRerequested",
    "WebhookCheckSuiteRerequestedPropCheckSuite",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropApp",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropOwner",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropAppPropPermissions",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommit",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropAuthor",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropHeadCommitPropCommitter",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItems",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBase",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropBasePropRepo",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHead",
    "WebhookCheckSuiteRerequestedPropCheckSuitePropPullRequestsItemsPropHeadPropRepo",
)
