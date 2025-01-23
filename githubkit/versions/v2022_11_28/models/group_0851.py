"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0028 import CodeScanningDefaultSetupOptions


class OrgsOrgCodeSecurityConfigurationsPostBody(GitHubModel):
    """OrgsOrgCodeSecurityConfigurationsPostBody"""

    name: str = Field(
        description="The name of the code security configuration. Must be unique within the organization."
    )
    description: str = Field(
        max_length=255, description="A description of the code security configuration"
    )
    advanced_security: Missing[Literal["enabled", "disabled"]] = Field(
        default=UNSET, description="The enablement status of GitHub Advanced Security"
    )
    dependency_graph: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of Dependency Graph"
    )
    dependency_graph_autosubmit_action: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of Automatic dependency submission",
    )
    dependency_graph_autosubmit_action_options: Missing[
        OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptions
    ] = Field(
        default=UNSET, description="Feature options for Automatic dependency submission"
    )
    dependabot_alerts: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of Dependabot alerts"
    )
    dependabot_security_updates: Missing[Literal["enabled", "disabled", "not_set"]] = (
        Field(
            default=UNSET,
            description="The enablement status of Dependabot security updates",
        )
    )
    code_scanning_default_setup: Missing[Literal["enabled", "disabled", "not_set"]] = (
        Field(
            default=UNSET,
            description="The enablement status of code scanning default setup",
        )
    )
    code_scanning_default_setup_options: Missing[
        Union[CodeScanningDefaultSetupOptions, None]
    ] = Field(
        default=UNSET, description="Feature options for code scanning default setup"
    )
    secret_scanning: Missing[Literal["enabled", "disabled", "not_set"]] = Field(
        default=UNSET, description="The enablement status of secret scanning"
    )
    secret_scanning_push_protection: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning push protection",
    )
    secret_scanning_delegated_bypass: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning delegated bypass",
    )
    secret_scanning_delegated_bypass_options: Missing[
        OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptions
    ] = Field(
        default=UNSET,
        description="Feature options for secret scanning delegated bypass",
    )
    secret_scanning_validity_checks: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning validity checks",
    )
    secret_scanning_non_provider_patterns: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of secret scanning non provider patterns",
    )
    private_vulnerability_reporting: Missing[
        Literal["enabled", "disabled", "not_set"]
    ] = Field(
        default=UNSET,
        description="The enablement status of private vulnerability reporting",
    )
    enforcement: Missing[Literal["enforced", "unenforced"]] = Field(
        default=UNSET, description="The enforcement status for a security configuration"
    )


class OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptions(
    GitHubModel
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOpti
    ons

    Feature options for Automatic dependency submission
    """

    labeled_runners: Missing[bool] = Field(
        default=UNSET,
        description="Whether to use runners labeled with 'dependency-submission' or standard GitHub runners.",
    )


class OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptions(
    GitHubModel
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOption
    s

    Feature options for secret scanning delegated bypass
    """

    reviewers: Missing[
        builtins.list[
            OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItems
        ]
    ] = Field(
        default=UNSET,
        description="The bypass reviewers for secret scanning delegated bypass",
    )


class OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItems(
    GitHubModel
):
    """OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOption
    sPropReviewersItems
    """

    reviewer_id: int = Field(
        description="The ID of the team or role selected as a bypass reviewer"
    )
    reviewer_type: Literal["TEAM", "ROLE"] = Field(
        description="The type of the bypass reviewer"
    )


model_rebuild(OrgsOrgCodeSecurityConfigurationsPostBody)
model_rebuild(
    OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptions
)
model_rebuild(
    OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptions
)
model_rebuild(
    OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItems
)

__all__ = (
    "OrgsOrgCodeSecurityConfigurationsPostBody",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropDependencyGraphAutosubmitActionOptions",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptions",
    "OrgsOrgCodeSecurityConfigurationsPostBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItems",
)
