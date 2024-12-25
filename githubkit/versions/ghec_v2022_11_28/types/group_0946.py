"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0150 import OrganizationCustomRepositoryRoleType


class OrgsOrgCustomRepositoryRolesGetResponse200Type(TypedDict):
    """OrgsOrgCustomRepositoryRolesGetResponse200"""

    total_count: NotRequired[int]
    custom_roles: NotRequired[list[OrganizationCustomRepositoryRoleType]]


__all__ = ("OrgsOrgCustomRepositoryRolesGetResponse200Type",)
