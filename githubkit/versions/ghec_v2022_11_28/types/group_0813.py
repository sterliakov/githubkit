"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0034 import RunnerType


class EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200Type(
    TypedDict
):
    """EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200"""

    total_count: float
    runners: List[RunnerType]


__all__ = (
    "EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdRunnersGetResponse200Type",
)
