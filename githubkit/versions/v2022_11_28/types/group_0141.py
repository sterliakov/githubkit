"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class RepositoryRuleRequiredStatusChecksPropParametersType(TypedDict):
    """RepositoryRuleRequiredStatusChecksPropParameters"""

    do_not_enforce_on_create: NotRequired[bool]
    required_status_checks: builtins.list[
        RepositoryRuleParamsStatusCheckConfigurationType
    ]
    strict_required_status_checks_policy: bool


class RepositoryRuleParamsStatusCheckConfigurationType(TypedDict):
    """StatusCheckConfiguration

    Required status check
    """

    context: str
    integration_id: NotRequired[int]


__all__ = (
    "RepositoryRuleParamsStatusCheckConfigurationType",
    "RepositoryRuleRequiredStatusChecksPropParametersType",
)
