"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof2Type(TypedDict):
    """ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof2"""

    language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ]
    query_pack: str
    repositories: NotRequired[builtins.list[str]]
    repository_lists: NotRequired[builtins.list[str]]
    repository_owners: builtins.list[str]


__all__ = ("ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof2Type",)
