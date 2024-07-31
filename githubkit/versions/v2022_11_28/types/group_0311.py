"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0038 import ReactionRollupType
from .group_0312 import ReviewCommentPropLinksType


class ReviewCommentType(TypedDict):
    """Legacy Review Comment

    Legacy Review Comment
    """

    url: str
    pull_request_review_id: Union[int, None]
    id: int
    node_id: str
    diff_hunk: str
    path: str
    position: Union[int, None]
    original_position: int
    commit_id: str
    original_commit_id: str
    in_reply_to_id: NotRequired[int]
    user: Union[None, SimpleUserType]
    body: str
    created_at: datetime
    updated_at: datetime
    html_url: str
    pull_request_url: str
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    links: ReviewCommentPropLinksType
    body_text: NotRequired[str]
    body_html: NotRequired[str]
    reactions: NotRequired[ReactionRollupType]
    side: NotRequired[Literal["LEFT", "RIGHT"]]
    start_side: NotRequired[Union[None, Literal["LEFT", "RIGHT"]]]
    line: NotRequired[int]
    original_line: NotRequired[int]
    start_line: NotRequired[Union[int, None]]
    original_start_line: NotRequired[Union[int, None]]


__all__ = ("ReviewCommentType",)
