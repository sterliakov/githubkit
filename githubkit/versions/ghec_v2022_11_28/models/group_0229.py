"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser
from .group_0228 import DiffEntry
from .group_0230 import CommitPropCommit


class Commit(GitHubModel):
    """Commit

    Commit
    """

    url: str = Field()
    sha: str = Field()
    node_id: str = Field()
    html_url: str = Field()
    comments_url: str = Field()
    commit: CommitPropCommit = Field()
    author: Union[SimpleUser, EmptyObject, None] = Field()
    committer: Union[SimpleUser, EmptyObject, None] = Field()
    parents: list[CommitPropParentsItems] = Field()
    stats: Missing[CommitPropStats] = Field(default=UNSET)
    files: Missing[list[DiffEntry]] = Field(default=UNSET)


class EmptyObject(GitHubModel):
    """Empty Object

    An object without any properties.
    """


class CommitPropParentsItems(GitHubModel):
    """CommitPropParentsItems"""

    sha: str = Field()
    url: str = Field()
    html_url: Missing[str] = Field(default=UNSET)


class CommitPropStats(GitHubModel):
    """CommitPropStats"""

    additions: Missing[int] = Field(default=UNSET)
    deletions: Missing[int] = Field(default=UNSET)
    total: Missing[int] = Field(default=UNSET)


model_rebuild(Commit)
model_rebuild(EmptyObject)
model_rebuild(CommitPropParentsItems)
model_rebuild(CommitPropStats)

__all__ = (
    "Commit",
    "CommitPropParentsItems",
    "CommitPropStats",
    "EmptyObject",
)
