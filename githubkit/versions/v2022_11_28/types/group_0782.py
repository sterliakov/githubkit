"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class GistsGistIdGetResponse403Type(TypedDict):
    """GistsGistIdGetResponse403"""

    block: NotRequired[GistsGistIdGetResponse403PropBlockType]
    message: NotRequired[str]
    documentation_url: NotRequired[str]


class GistsGistIdGetResponse403PropBlockType(TypedDict):
    """GistsGistIdGetResponse403PropBlock"""

    reason: NotRequired[str]
    created_at: NotRequired[str]
    html_url: NotRequired[Union[str, None]]


__all__ = (
    "GistsGistIdGetResponse403PropBlockType",
    "GistsGistIdGetResponse403Type",
)
