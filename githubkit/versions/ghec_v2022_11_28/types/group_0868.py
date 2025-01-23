"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdPatchBodyType(TypedDict):
    """EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdPatchBody"""

    name: NotRequired[str]
    visibility: NotRequired[Literal["selected", "all"]]
    allows_public_repositories: NotRequired[bool]
    restricted_to_workflows: NotRequired[bool]
    selected_workflows: NotRequired[builtins.list[str]]
    network_configuration_id: NotRequired[Union[str, None]]


__all__ = ("EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdPatchBodyType",)
