"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0371 import SearchResultTextMatchesItems


class LabelSearchResultItem(GitHubModel):
    """Label Search Result Item

    Label Search Result Item
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    name: str = Field()
    color: str = Field()
    default: bool = Field()
    description: Union[str, None] = Field()
    score: float = Field()
    text_matches: Missing[list[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )


class SearchLabelsGetResponse200(GitHubModel):
    """SearchLabelsGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: list[LabelSearchResultItem] = Field()


model_rebuild(LabelSearchResultItem)
model_rebuild(SearchLabelsGetResponse200)

__all__ = (
    "LabelSearchResultItem",
    "SearchLabelsGetResponse200",
)
