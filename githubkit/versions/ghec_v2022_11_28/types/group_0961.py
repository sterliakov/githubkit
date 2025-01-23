"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict

from .group_0065 import CopilotSeatDetailsType


class OrgsOrgCopilotBillingSeatsGetResponse200Type(TypedDict):
    """OrgsOrgCopilotBillingSeatsGetResponse200"""

    total_seats: NotRequired[int]
    seats: NotRequired[builtins.list[CopilotSeatDetailsType]]


__all__ = ("OrgsOrgCopilotBillingSeatsGetResponse200Type",)
