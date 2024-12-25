"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0059 import OrganizationSimpleType
from .group_0082 import TeamType


class CopilotSeatDetailsType(TypedDict):
    """Copilot Business Seat Detail

    Information about a Copilot Business seat assignment for a user, team, or
    organization.
    """

    assignee: SimpleUserType
    organization: NotRequired[Union[None, OrganizationSimpleType]]
    assigning_team: NotRequired[Union[TeamType, EnterpriseTeamType, None]]
    pending_cancellation_date: NotRequired[Union[date, None]]
    last_activity_at: NotRequired[Union[datetime, None]]
    last_activity_editor: NotRequired[Union[str, None]]
    created_at: datetime
    updated_at: NotRequired[datetime]
    plan_type: NotRequired[Literal["business", "enterprise", "unknown"]]


class EnterpriseTeamType(TypedDict):
    """Enterprise Team

    Group of enterprise owners and/or members
    """

    id: int
    name: str
    slug: str
    url: str
    sync_to_organizations: str
    group_id: NotRequired[Union[str, None]]
    html_url: str
    members_url: str
    created_at: datetime
    updated_at: datetime


class OrgsOrgCopilotBillingSeatsGetResponse200Type(TypedDict):
    """OrgsOrgCopilotBillingSeatsGetResponse200"""

    total_seats: NotRequired[int]
    seats: NotRequired[list[CopilotSeatDetailsType]]


__all__ = (
    "CopilotSeatDetailsType",
    "EnterpriseTeamType",
    "OrgsOrgCopilotBillingSeatsGetResponse200Type",
)
