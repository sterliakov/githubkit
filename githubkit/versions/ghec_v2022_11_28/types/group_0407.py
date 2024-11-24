"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0091 import MinimalRepositoryType
from .group_0226 import GitUserType
from .group_0405 import SearchResultTextMatchesItemsType
from .group_0408 import CommitSearchResultItemPropCommitType


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
    parents: list[CommitSearchResultItemPropParentsItemsType]
    repository: MinimalRepositoryType
    score: float
    node_id: str
    text_matches: NotRequired[list[SearchResultTextMatchesItemsType]]


class CommitSearchResultItemPropParentsItemsType(TypedDict):
    """CommitSearchResultItemPropParentsItems"""

    url: NotRequired[str]
    html_url: NotRequired[str]
    sha: NotRequired[str]


class SearchCommitsGetResponse200Type(TypedDict):
    """SearchCommitsGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: list[CommitSearchResultItemType]


__all__ = (
    "CommitSearchResultItemPropParentsItemsType",
    "CommitSearchResultItemType",
    "SearchCommitsGetResponse200Type",
)
