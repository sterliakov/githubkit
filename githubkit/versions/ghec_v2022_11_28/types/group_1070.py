"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import TypedDict


class ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0Type(
    TypedDict
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0

    Examples:
        {'contexts': ['contexts']}
    """

    contexts: builtins.list[str]


__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredStatusChecksContextsPutBodyOneof0Type",
)
