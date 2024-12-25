"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0053 import CodeSecurityConfiguration


class EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200(
    GitHubModel
):
    """EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutRespons
    e200
    """

    default_for_new_repos: Missing[
        Literal["all", "none", "private_and_internal", "public"]
    ] = Field(
        default=UNSET,
        description="Specifies which types of repository this security configuration is applied to by default.",
    )
    configuration: Missing[CodeSecurityConfiguration] = Field(
        default=UNSET, description="A code security configuration"
    )


model_rebuild(
    EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200
)

__all__ = (
    "EnterprisesEnterpriseCodeSecurityConfigurationsConfigurationIdDefaultsPutResponse200",
)
