"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrgsOrgActionsPermissionsPutBodyType(TypedDict):
    """OrgsOrgActionsPermissionsPutBody"""

    enabled_repositories: Literal["all", "none", "selected"]
    allowed_actions: NotRequired[Literal["all", "local_only", "selected"]]


__all__ = ("OrgsOrgActionsPermissionsPutBodyType",)
