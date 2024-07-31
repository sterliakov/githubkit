"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0386 import SearchResultTextMatchesItemsType


class TopicSearchResultItemType(TypedDict):
    """Topic Search Result Item

    Topic Search Result Item
    """

    name: str
    display_name: Union[str, None]
    short_description: Union[str, None]
    description: Union[str, None]
    created_by: Union[str, None]
    released: Union[str, None]
    created_at: datetime
    updated_at: datetime
    featured: bool
    curated: bool
    score: float
    repository_count: NotRequired[Union[int, None]]
    logo_url: NotRequired[Union[str, None]]
    text_matches: NotRequired[List[SearchResultTextMatchesItemsType]]
    related: NotRequired[Union[List[TopicSearchResultItemPropRelatedItemsType], None]]
    aliases: NotRequired[Union[List[TopicSearchResultItemPropAliasesItemsType], None]]


class TopicSearchResultItemPropRelatedItemsType(TypedDict):
    """TopicSearchResultItemPropRelatedItems"""

    topic_relation: NotRequired[
        TopicSearchResultItemPropRelatedItemsPropTopicRelationType
    ]


class TopicSearchResultItemPropRelatedItemsPropTopicRelationType(TypedDict):
    """TopicSearchResultItemPropRelatedItemsPropTopicRelation"""

    id: NotRequired[int]
    name: NotRequired[str]
    topic_id: NotRequired[int]
    relation_type: NotRequired[str]


class TopicSearchResultItemPropAliasesItemsType(TypedDict):
    """TopicSearchResultItemPropAliasesItems"""

    topic_relation: NotRequired[
        TopicSearchResultItemPropAliasesItemsPropTopicRelationType
    ]


class TopicSearchResultItemPropAliasesItemsPropTopicRelationType(TypedDict):
    """TopicSearchResultItemPropAliasesItemsPropTopicRelation"""

    id: NotRequired[int]
    name: NotRequired[str]
    topic_id: NotRequired[int]
    relation_type: NotRequired[str]


class SearchTopicsGetResponse200Type(TypedDict):
    """SearchTopicsGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: List[TopicSearchResultItemType]


__all__ = (
    "TopicSearchResultItemType",
    "TopicSearchResultItemPropRelatedItemsType",
    "TopicSearchResultItemPropRelatedItemsPropTopicRelationType",
    "TopicSearchResultItemPropAliasesItemsType",
    "TopicSearchResultItemPropAliasesItemsPropTopicRelationType",
    "SearchTopicsGetResponse200Type",
)
