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
from .group_0014 import EnterpriseType
from .group_0016 import AppPermissionsType


class InstallationType(TypedDict):
    """Installation

    Installation
    """

    id: int
    account: Union[SimpleUserType, EnterpriseType, None]
    repository_selection: Literal["all", "selected"]
    access_tokens_url: str
    repositories_url: str
    html_url: str
    app_id: int
    target_id: int
    target_type: str
    permissions: AppPermissionsType
    events: list[str]
    created_at: datetime
    updated_at: datetime
    single_file_name: Union[str, None]
    has_multiple_single_files: NotRequired[bool]
    single_file_paths: NotRequired[list[str]]
    app_slug: str
    suspended_by: Union[None, SimpleUserType]
    suspended_at: Union[datetime, None]
    contact_email: NotRequired[Union[str, None]]


__all__ = ("InstallationType",)
