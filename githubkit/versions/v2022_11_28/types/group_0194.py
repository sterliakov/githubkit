"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0026 import TeamType
from .group_0001 import SimpleUserType
from .group_0006 import IntegrationType


class ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType(
    TypedDict
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions"""

    url: str
    users_url: str
    teams_url: str
    users: List[SimpleUserType]
    teams: List[TeamType]
    apps: NotRequired[List[Union[IntegrationType, None]]]


class ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType(
    TypedDict
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances"""

    users: List[SimpleUserType]
    teams: List[TeamType]
    apps: NotRequired[List[Union[IntegrationType, None]]]


__all__ = (
    "ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType",
    "ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType",
)
