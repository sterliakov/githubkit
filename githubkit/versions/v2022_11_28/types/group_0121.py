"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType(TypedDict):
    """RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryName"""

    include: NotRequired[builtins.list[str]]
    exclude: NotRequired[builtins.list[str]]
    protected: NotRequired[bool]


__all__ = ("RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType",)
