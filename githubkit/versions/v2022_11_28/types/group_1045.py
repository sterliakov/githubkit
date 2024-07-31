"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoReleasesReleaseIdPatchBodyType(TypedDict):
    """ReposOwnerRepoReleasesReleaseIdPatchBody"""

    tag_name: NotRequired[str]
    target_commitish: NotRequired[str]
    name: NotRequired[str]
    body: NotRequired[str]
    draft: NotRequired[bool]
    prerelease: NotRequired[bool]
    make_latest: NotRequired[Literal["true", "false", "legacy"]]
    discussion_category_name: NotRequired[str]


__all__ = ("ReposOwnerRepoReleasesReleaseIdPatchBodyType",)
