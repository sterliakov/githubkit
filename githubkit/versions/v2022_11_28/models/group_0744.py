"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0177 import Deployment
from .group_0373 import EnterpriseWebhooks
from .group_0374 import SimpleInstallation
from .group_0376 import RepositoryWebhooks
from .group_0377 import SimpleUserWebhooks
from .group_0375 import OrganizationSimpleWebhooks


class WebhookWorkflowJobInProgress(GitHubModel):
    """workflow_job in_progress event"""

    action: Literal["in_progress"] = Field()
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
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    workflow_job: WebhookWorkflowJobInProgressPropWorkflowJob = Field()
    deployment: Missing[Deployment] = Field(
        default=UNSET,
        title="Deployment",
        description="A request for a specific ref(branch,sha,tag) to be deployed",
    )


class WebhookWorkflowJobInProgressPropWorkflowJob(GitHubModel):
    """WebhookWorkflowJobInProgressPropWorkflowJob"""

    check_run_url: str = Field()
    completed_at: Union[Union[str, None], None] = Field()
    conclusion: Union[Literal["success", "failure", "cancelled", "neutral"], None] = (
        Field()
    )
    created_at: str = Field(description="The time that the job created.")
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: List[str] = Field(
        description='Custom labels for the job. Specified by the [`"runs-on"` attribute](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on) in the workflow YAML.'
    )
    name: str = Field()
    node_id: str = Field()
    run_attempt: int = Field()
    run_id: int = Field()
    run_url: str = Field()
    runner_group_id: Union[Union[int, None], None] = Field(
        description="The ID of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_group_name: Union[Union[str, None], None] = Field(
        description="The name of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_id: Union[Union[int, None], None] = Field(
        description="The ID of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    runner_name: Union[Union[str, None], None] = Field(
        description="The name of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`."
    )
    started_at: str = Field()
    status: Literal["queued", "in_progress", "completed"] = Field(
        description="The current status of the job. Can be `queued`, `in_progress`, or `completed`."
    )
    head_branch: Union[Union[str, None], None] = Field(
        description="The name of the current branch."
    )
    workflow_name: Union[Union[str, None], None] = Field(
        description="The name of the workflow."
    )
    steps: List[WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps] = Field()
    url: str = Field()


class WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps(GitHubModel):
    """WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps"""

    completed_at: Union[Union[str, None], None] = Field()
    conclusion: Union[Literal["failure", "skipped", "success", "cancelled"], None] = (
        Field()
    )
    name: str = Field()
    number: int = Field()
    started_at: Union[Union[str, None], None] = Field()
    status: Literal["in_progress", "completed", "queued", "pending"] = Field()


model_rebuild(WebhookWorkflowJobInProgress)
model_rebuild(WebhookWorkflowJobInProgressPropWorkflowJob)
model_rebuild(WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps)

__all__ = (
    "WebhookWorkflowJobInProgress",
    "WebhookWorkflowJobInProgressPropWorkflowJob",
    "WebhookWorkflowJobInProgressPropWorkflowJobMergedSteps",
)
