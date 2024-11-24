"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser
from .group_0427 import EnterpriseWebhooks
from .group_0428 import SimpleInstallation
from .group_0429 import OrganizationSimpleWebhooks
from .group_0430 import RepositoryWebhooks
from .group_0431 import WebhooksRule


class WebhookBranchProtectionRuleEdited(GitHubModel):
    """branch protection rule edited event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookBranchProtectionRuleEditedPropChanges] = Field(
        default=UNSET,
        description="If the action was `edited`, the changes to the rule.",
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
    rule: WebhooksRule = Field(
        title="branch protection rule",
        description="The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/enterprise-cloud@latest//github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookBranchProtectionRuleEditedPropChanges(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced
    ] = Field(default=UNSET)
    authorized_actor_names: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames
    ] = Field(default=UNSET)
    authorized_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly
    ] = Field(default=UNSET)
    authorized_dismissal_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
    ] = Field(default=UNSET)
    linear_history_requirement_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
    ] = Field(default=UNSET)
    lock_branch_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel
    ] = Field(default=UNSET)
    lock_allows_fork_sync: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync
    ] = Field(default=UNSET)
    pull_request_reviews_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevel
    ] = Field(default=UNSET)
    require_last_push_approval: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval
    ] = Field(default=UNSET)
    required_status_checks: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks
    ] = Field(default=UNSET)
    required_status_checks_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
    ] = Field(default=UNSET)


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: list[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel"""

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLev
    el
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: list[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


model_rebuild(WebhookBranchProtectionRuleEdited)
model_rebuild(WebhookBranchProtectionRuleEditedPropChanges)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel
)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevel
)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
)

__all__ = (
    "WebhookBranchProtectionRuleEdited",
    "WebhookBranchProtectionRuleEditedPropChanges",
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel",
    "WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevel",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel",
)
