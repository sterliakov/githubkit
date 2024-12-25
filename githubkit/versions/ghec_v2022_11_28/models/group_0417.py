"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0409 import Meta
from .group_0414 import UserEmailsResponseItems, UserNameResponse
from .group_0415 import UserRoleItems
from .group_0419 import ScimEnterpriseUserResponseAllof1PropGroupsItems


class ScimEnterpriseUserResponse(GitHubModel):
    """ScimEnterpriseUserResponse"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]] = Field(
        description="The URIs that are used to indicate the namespaces of the SCIM schemas."
    )
    external_id: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="externalId",
        description="A unique identifier for the resource as defined by the provisioning client.",
    )
    active: bool = Field(description="Whether the user active in the IdP.")
    user_name: Missing[str] = Field(
        default=UNSET, alias="userName", description="The username for the user."
    )
    name: Missing[UserNameResponse] = Field(default=UNSET)
    display_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="displayName",
        description="A human-readable name for the user.",
    )
    emails: list[UserEmailsResponseItems] = Field(
        description="The emails for the user."
    )
    roles: Missing[list[UserRoleItems]] = Field(
        default=UNSET, description="The roles assigned to the user."
    )
    id: str = Field(description="The internally generated id for the user object.")
    groups: Missing[list[ScimEnterpriseUserResponseAllof1PropGroupsItems]] = Field(
        default=UNSET,
        description="Provisioned SCIM groups that the user is a member of.",
    )
    meta: Meta = Field(
        description="The metadata associated with the creation/updates to the user."
    )


class ScimEnterpriseUserList(GitHubModel):
    """ScimEnterpriseUserList"""

    schemas: list[Literal["urn:ietf:params:scim:api:messages:2.0:ListResponse"]] = (
        Field(
            description="The URIs that are used to indicate the namespaces of the list SCIM schemas."
        )
    )
    total_results: int = Field(
        alias="totalResults", description="Number of results found"
    )
    resources: list[ScimEnterpriseUserResponse] = Field(
        alias="Resources", description="Information about each provisioned account."
    )
    start_index: int = Field(
        alias="startIndex", description="A starting index for the returned page"
    )
    items_per_page: int = Field(
        alias="itemsPerPage", description="Number of objects per page"
    )


model_rebuild(ScimEnterpriseUserResponse)
model_rebuild(ScimEnterpriseUserList)

__all__ = (
    "ScimEnterpriseUserList",
    "ScimEnterpriseUserResponse",
)
