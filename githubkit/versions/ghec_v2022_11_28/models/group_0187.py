"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser


class OrganizationProgrammaticAccessGrant(GitHubModel):
    """Organization Programmatic Access Grant

    Minimal representation of an organization programmatic access grant for
    enumerations
    """

    id: int = Field(
        description="Unique identifier of the fine-grained personal access token grant. The `pat_id` used to get details about an approved fine-grained personal access token."
    )
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    repository_selection: Literal["none", "all", "subset"] = Field(
        description="Type of repository selection requested."
    )
    repositories_url: str = Field(
        description="URL to the list of repositories the fine-grained personal access token can access. Only follow when `repository_selection` is `subset`."
    )
    permissions: OrganizationProgrammaticAccessGrantPropPermissions = Field(
        description="Permissions requested, categorized by type of permission."
    )
    access_granted_at: str = Field(
        description="Date and time when the fine-grained personal access token was approved to access the organization."
    )
    token_id: int = Field(
        description="Unique identifier of the user's token. This field can also be found in audit log events and the organization's settings for their PAT grants."
    )
    token_name: str = Field(
        description="The name given to the user's token. This field can also be found in an organization's settings page for Active Tokens."
    )
    token_expired: bool = Field(
        description="Whether the associated fine-grained personal access token has expired."
    )
    token_expires_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token expires."
    )
    token_last_used_at: Union[str, None] = Field(
        description="Date and time when the associated fine-grained personal access token was last used for authentication."
    )


class OrganizationProgrammaticAccessGrantPropPermissions(GitHubModel):
    """OrganizationProgrammaticAccessGrantPropPermissions

    Permissions requested, categorized by type of permission.
    """

    organization: Missing[
        OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization
    ] = Field(default=UNSET)
    repository: Missing[
        OrganizationProgrammaticAccessGrantPropPermissionsPropRepository
    ] = Field(default=UNSET)
    other: Missing[OrganizationProgrammaticAccessGrantPropPermissionsPropOther] = Field(
        default=UNSET
    )


class OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization(
    ExtraGitHubModel
):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization"""


class OrganizationProgrammaticAccessGrantPropPermissionsPropRepository(
    ExtraGitHubModel
):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropRepository"""


class OrganizationProgrammaticAccessGrantPropPermissionsPropOther(ExtraGitHubModel):
    """OrganizationProgrammaticAccessGrantPropPermissionsPropOther"""


model_rebuild(OrganizationProgrammaticAccessGrant)
model_rebuild(OrganizationProgrammaticAccessGrantPropPermissions)
model_rebuild(OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization)
model_rebuild(OrganizationProgrammaticAccessGrantPropPermissionsPropRepository)
model_rebuild(OrganizationProgrammaticAccessGrantPropPermissionsPropOther)

__all__ = (
    "OrganizationProgrammaticAccessGrant",
    "OrganizationProgrammaticAccessGrantPropPermissions",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropOrganization",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropOther",
    "OrganizationProgrammaticAccessGrantPropPermissionsPropRepository",
)
