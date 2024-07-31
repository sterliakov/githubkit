"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0379 import UserRoleItemsType
from .group_0378 import UserNameResponseType, UserEmailsResponseItemsType


class UserResponseType(TypedDict):
    """UserResponse"""

    schemas: List[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]]
    external_id: NotRequired[Union[str, None]]
    active: bool
    user_name: NotRequired[str]
    name: NotRequired[UserNameResponseType]
    display_name: NotRequired[Union[str, None]]
    emails: List[UserEmailsResponseItemsType]
    roles: NotRequired[List[UserRoleItemsType]]


__all__ = ("UserResponseType",)
