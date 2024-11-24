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


class GroupResponse(GitHubModel):
    """GroupResponse"""

    schemas: list[
        Literal[
            "urn:ietf:params:scim:schemas:core:2.0:Group",
            "urn:ietf:params:scim:api:messages:2.0:ListResponse",
        ]
    ] = Field(
        description="The URIs that are used to indicate the namespaces of the SCIM schemas."
    )
    external_id: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="externalId",
        description="A unique identifier for the resource as defined by the provisioning client.",
    )
    display_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="displayName",
        description="A human-readable name for a security group.",
    )
    members: Missing[list[GroupResponsePropMembersItems]] = Field(
        default=UNSET, description="The group members."
    )


class GroupResponsePropMembersItems(GitHubModel):
    """GroupResponsePropMembersItems"""

    value: str = Field(description="The local unique identifier for the member")
    ref: str = Field(alias="$ref")
    display: Missing[str] = Field(
        default=UNSET, description="The display name associated with the member"
    )


model_rebuild(GroupResponse)
model_rebuild(GroupResponsePropMembersItems)

__all__ = (
    "GroupResponse",
    "GroupResponsePropMembersItems",
)
