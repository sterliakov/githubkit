"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict

from .group_0415 import MetaType
from .group_0425 import ScimEnterpriseUserResponseAllof1PropGroupsItemsType


class ScimEnterpriseUserResponseAllof1Type(TypedDict):
    """ScimEnterpriseUserResponseAllof1"""

    id: str
    groups: NotRequired[
        builtins.list[ScimEnterpriseUserResponseAllof1PropGroupsItemsType]
    ]
    meta: MetaType


__all__ = ("ScimEnterpriseUserResponseAllof1Type",)
