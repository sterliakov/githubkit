"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0162 import RepositoryRuleCodeScanningPropParametersType


class RepositoryRuleDetailedOneof16Type(TypedDict):
    """RepositoryRuleDetailedOneof16"""

    type: Literal["code_scanning"]
    parameters: NotRequired[RepositoryRuleCodeScanningPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof16Type",)
