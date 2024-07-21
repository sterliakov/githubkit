"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0137 import RepositoryRuleCodeScanningPropParametersType


class RepositoryRuleCodeScanningType(TypedDict):
    """code_scanning

    Choose which tools must provide code scanning results before the reference is
    updated. When configured, code scanning must be enabled and have results for
    both the commit and the reference being updated.
    """

    type: Literal["code_scanning"]
    parameters: NotRequired[RepositoryRuleCodeScanningPropParametersType]


__all__ = ("RepositoryRuleCodeScanningType",)
