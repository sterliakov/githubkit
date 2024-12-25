"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0137 import RepositoryRuleRequiredStatusChecksPropParametersType


class RepositoryRuleRequiredStatusChecksType(TypedDict):
    """required_status_checks

    Choose which status checks must pass before the ref is updated. When enabled,
    commits must first be pushed to another ref where the checks pass.
    """

    type: Literal["required_status_checks"]
    parameters: NotRequired[RepositoryRuleRequiredStatusChecksPropParametersType]


__all__ = ("RepositoryRuleRequiredStatusChecksType",)
