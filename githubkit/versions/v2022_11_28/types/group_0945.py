"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoActionsRunnersGenerateJitconfigPostBodyType(TypedDict):
    """ReposOwnerRepoActionsRunnersGenerateJitconfigPostBody"""

    name: str
    runner_group_id: int
    labels: builtins.list[str]
    work_folder: NotRequired[str]


__all__ = ("ReposOwnerRepoActionsRunnersGenerateJitconfigPostBodyType",)
