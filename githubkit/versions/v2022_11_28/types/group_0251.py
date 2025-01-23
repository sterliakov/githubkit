"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0056 import MinimalRepositoryType


class CombinedCommitStatusType(TypedDict):
    """Combined Commit Status

    Combined Commit Status
    """

    state: str
    statuses: builtins.list[SimpleCommitStatusType]
    sha: str
    total_count: int
    repository: MinimalRepositoryType
    commit_url: str
    url: str


class SimpleCommitStatusType(TypedDict):
    """Simple Commit Status"""

    description: Union[str, None]
    id: int
    node_id: str
    state: str
    context: str
    target_url: Union[str, None]
    required: NotRequired[Union[bool, None]]
    avatar_url: Union[str, None]
    url: str
    created_at: datetime
    updated_at: datetime


__all__ = (
    "CombinedCommitStatusType",
    "SimpleCommitStatusType",
)
