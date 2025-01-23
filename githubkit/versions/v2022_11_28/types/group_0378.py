"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0056 import MinimalRepositoryType
from .group_0206 import GitUserType
from .group_0376 import SearchResultTextMatchesItemsType
from .group_0379 import CommitSearchResultItemPropCommitType


class CommitSearchResultItemType(TypedDict):
    """Commit Search Result Item

    Commit Search Result Item
    """

    url: str
    sha: str
    html_url: str
    comments_url: str
    commit: CommitSearchResultItemPropCommitType
    author: Union[None, SimpleUserType]
    committer: Union[None, GitUserType]
    parents: builtins.list[CommitSearchResultItemPropParentsItemsType]
    repository: MinimalRepositoryType
    score: float
    node_id: str
    text_matches: NotRequired[builtins.list[SearchResultTextMatchesItemsType]]


class CommitSearchResultItemPropParentsItemsType(TypedDict):
    """CommitSearchResultItemPropParentsItems"""

    url: NotRequired[str]
    html_url: NotRequired[str]
    sha: NotRequired[str]


class SearchCommitsGetResponse200Type(TypedDict):
    """SearchCommitsGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: builtins.list[CommitSearchResultItemType]


__all__ = (
    "CommitSearchResultItemPropParentsItemsType",
    "CommitSearchResultItemType",
    "SearchCommitsGetResponse200Type",
)
