"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0018 import LicenseSimpleType
from .group_0192 import CodeOfConductSimpleType


class CommunityProfilePropFilesType(TypedDict):
    """CommunityProfilePropFiles"""

    code_of_conduct: Union[None, CodeOfConductSimpleType]
    code_of_conduct_file: Union[None, CommunityHealthFileType]
    license_: Union[None, LicenseSimpleType]
    contributing: Union[None, CommunityHealthFileType]
    readme: Union[None, CommunityHealthFileType]
    issue_template: Union[None, CommunityHealthFileType]
    pull_request_template: Union[None, CommunityHealthFileType]


class CommunityHealthFileType(TypedDict):
    """Community Health File"""

    url: str
    html_url: str


class CommunityProfileType(TypedDict):
    """Community Profile

    Community Profile
    """

    health_percentage: int
    description: Union[str, None]
    documentation: Union[str, None]
    files: CommunityProfilePropFilesType
    updated_at: Union[datetime, None]
    content_reports_enabled: NotRequired[bool]


__all__ = (
    "CommunityHealthFileType",
    "CommunityProfilePropFilesType",
    "CommunityProfileType",
)
