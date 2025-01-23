"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoCheckSuitesPreferencesPatchBodyType(TypedDict):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBody"""

    auto_trigger_checks: NotRequired[
        builtins.list[
            ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
        ]
    ]


class ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType(
    TypedDict
):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems"""

    app_id: int
    setting: bool


__all__ = (
    "ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType",
    "ReposOwnerRepoCheckSuitesPreferencesPatchBodyType",
)
