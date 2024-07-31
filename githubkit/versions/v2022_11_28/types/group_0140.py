"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class RepositoryRuleOneof18Type(TypedDict):
    """max_file_size

    > [!NOTE]
    > `max_file_size` is in beta and subject to change.

    Prevent commits that exceed a specified file size limit from being pushed to the
    commit.
    """

    type: Literal["max_file_size"]
    parameters: NotRequired[RepositoryRuleOneof18PropParametersType]


class RepositoryRuleOneof18PropParametersType(TypedDict):
    """RepositoryRuleOneof18PropParameters"""

    max_file_size: int


__all__ = (
    "RepositoryRuleOneof18Type",
    "RepositoryRuleOneof18PropParametersType",
)
