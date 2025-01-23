"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import TypedDict

from .group_0409 import TrafficType


class ViewTrafficType(TypedDict):
    """View Traffic

    View Traffic
    """

    count: int
    uniques: int
    views: builtins.list[TrafficType]


__all__ = ("ViewTrafficType",)
