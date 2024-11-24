"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0157 import RepositoryRuleMergeQueuePropParameters


class RepositoryRuleMergeQueue(GitHubModel):
    """merge_queue

    Merges must be performed via a merge queue.
    """

    type: Literal["merge_queue"] = Field()
    parameters: Missing[RepositoryRuleMergeQueuePropParameters] = Field(default=UNSET)


model_rebuild(RepositoryRuleMergeQueue)

__all__ = ("RepositoryRuleMergeQueue",)
