"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0008 import IntegrationType
from .group_0074 import ReactionRollupType


class IssueCommentType(TypedDict):
    """Issue Comment

    Comments provide a way for people to collaborate on an issue.
    """

    id: int
    node_id: str
    url: str
    body: NotRequired[str]
    body_text: NotRequired[str]
    body_html: NotRequired[str]
    html_url: str
    user: Union[None, SimpleUserType]
    created_at: datetime
    updated_at: datetime
    issue_url: str
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
    performed_via_github_app: NotRequired[Union[None, IntegrationType, None]]
    reactions: NotRequired[ReactionRollupType]


__all__ = ("IssueCommentType",)
