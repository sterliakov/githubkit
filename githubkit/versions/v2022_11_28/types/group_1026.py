"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPullsPullNumberCommentsPostBodyType(TypedDict):
    """ReposOwnerRepoPullsPullNumberCommentsPostBody"""

    body: str
    commit_id: str
    path: str
    position: NotRequired[int]
    side: NotRequired[Literal["LEFT", "RIGHT"]]
    line: NotRequired[int]
    start_line: NotRequired[int]
    start_side: NotRequired[Literal["LEFT", "RIGHT", "side"]]
    in_reply_to: NotRequired[int]
    subject_type: NotRequired[Literal["line", "file"]]


__all__ = ("ReposOwnerRepoPullsPullNumberCommentsPostBodyType",)
