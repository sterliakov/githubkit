"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0191 import CommitType
from .group_0186 import BranchProtectionType


class BranchWithProtectionType(TypedDict):
    """Branch With Protection

    Branch With Protection
    """

    name: str
    commit: CommitType
    links: BranchWithProtectionPropLinksType
    protected: bool
    protection: BranchProtectionType
    protection_url: str
    pattern: NotRequired[str]
    required_approving_review_count: NotRequired[int]


class BranchWithProtectionPropLinksType(TypedDict):
    """BranchWithProtectionPropLinks"""

    html: str
    self_: str


__all__ = (
    "BranchWithProtectionType",
    "BranchWithProtectionPropLinksType",
)
