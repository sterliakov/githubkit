"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0245 import LinkType


class ReviewCommentPropLinksType(TypedDict):
    """ReviewCommentPropLinks"""

    self_: LinkType
    html: LinkType
    pull_request: LinkType


__all__ = ("ReviewCommentPropLinksType",)
