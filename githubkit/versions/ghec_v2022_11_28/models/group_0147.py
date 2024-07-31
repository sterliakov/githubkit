"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleRequiredStatusChecksPropParameters(GitHubModel):
    """RepositoryRuleRequiredStatusChecksPropParameters"""

    do_not_enforce_on_create: Missing[bool] = Field(
        default=UNSET,
        description="Allow repositories and branches to be created if a check would otherwise prohibit it.",
    )
    required_status_checks: List[RepositoryRuleParamsStatusCheckConfiguration] = Field(
        description="Status checks that are required."
    )
    strict_required_status_checks_policy: bool = Field(
        description="Whether pull requests targeting a matching branch must be tested with the latest code. This setting will not take effect unless at least one status check is enabled."
    )


class RepositoryRuleParamsStatusCheckConfiguration(GitHubModel):
    """StatusCheckConfiguration

    Required status check
    """

    context: str = Field(
        description="The status check context name that must be present on the commit."
    )
    integration_id: Missing[int] = Field(
        default=UNSET,
        description="The optional integration ID that this status check must originate from.",
    )


model_rebuild(RepositoryRuleRequiredStatusChecksPropParameters)
model_rebuild(RepositoryRuleParamsStatusCheckConfiguration)

__all__ = (
    "RepositoryRuleRequiredStatusChecksPropParameters",
    "RepositoryRuleParamsStatusCheckConfiguration",
)
