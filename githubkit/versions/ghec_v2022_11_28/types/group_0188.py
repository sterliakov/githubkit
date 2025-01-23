"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrganizationCustomOrganizationRoleUpdateSchemaType(TypedDict):
    """OrganizationCustomOrganizationRoleUpdateSchema"""

    name: NotRequired[str]
    description: NotRequired[str]
    permissions: NotRequired[builtins.list[str]]
    base_role: NotRequired[
        Literal["none", "read", "triage", "write", "maintain", "admin"]
    ]


__all__ = ("OrganizationCustomOrganizationRoleUpdateSchemaType",)
