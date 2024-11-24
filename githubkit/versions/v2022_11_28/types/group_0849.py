"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class OrgsOrgHooksHookIdPatchBodyType(TypedDict):
    """OrgsOrgHooksHookIdPatchBody"""

    config: NotRequired[OrgsOrgHooksHookIdPatchBodyPropConfigType]
    events: NotRequired[list[str]]
    active: NotRequired[bool]
    name: NotRequired[str]


class OrgsOrgHooksHookIdPatchBodyPropConfigType(TypedDict):
    """OrgsOrgHooksHookIdPatchBodyPropConfig

    Key/value pairs to provide settings for this webhook.
    """

    url: str
    content_type: NotRequired[str]
    secret: NotRequired[str]
    insecure_ssl: NotRequired[Union[str, float]]


__all__ = (
    "OrgsOrgHooksHookIdPatchBodyPropConfigType",
    "OrgsOrgHooksHookIdPatchBodyType",
)
