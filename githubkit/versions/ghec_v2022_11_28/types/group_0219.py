"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing_extensions import NotRequired, TypedDict


class ActionsCacheListType(TypedDict):
    """Repository actions caches

    Repository actions caches
    """

    total_count: int
    actions_caches: builtins.list[ActionsCacheListPropActionsCachesItemsType]


class ActionsCacheListPropActionsCachesItemsType(TypedDict):
    """ActionsCacheListPropActionsCachesItems"""

    id: NotRequired[int]
    ref: NotRequired[str]
    key: NotRequired[str]
    version: NotRequired[str]
    last_accessed_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    size_in_bytes: NotRequired[int]


__all__ = (
    "ActionsCacheListPropActionsCachesItemsType",
    "ActionsCacheListType",
)
