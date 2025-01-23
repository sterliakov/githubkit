"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0035 import OrganizationSimple
from .group_0064 import Team


class CopilotSeatDetails(GitHubModel):
    """Copilot Business Seat Detail

    Information about a Copilot Business seat assignment for a user, team, or
    organization.
    """

    assignee: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    organization: Missing[Union[None, OrganizationSimple]] = Field(default=UNSET)
    assigning_team: Missing[Union[Team, EnterpriseTeam, None]] = Field(
        default=UNSET,
        description="The team through which the assignee is granted access to GitHub Copilot, if applicable.",
    )
    pending_cancellation_date: Missing[Union[date, None]] = Field(
        default=UNSET,
        description="The pending cancellation date for the seat, in `YYYY-MM-DD` format. This will be null unless the assignee's Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization's next billing cycle.",
    )
    last_activity_at: Missing[Union[datetime, None]] = Field(
        default=UNSET,
        description="Timestamp of user's last GitHub Copilot activity, in ISO 8601 format.",
    )
    last_activity_editor: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="Last editor that was used by the user for a GitHub Copilot completion.",
    )
    created_at: datetime = Field(
        description="Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format."
    )
    updated_at: Missing[datetime] = Field(
        default=UNSET,
        description="**Closing down notice:** This field is no longer relevant and is closing down. Use the `created_at` field to determine when the assignee was last granted access to GitHub Copilot. Timestamp of when the assignee's GitHub Copilot access was last updated, in ISO 8601 format.",
    )
    plan_type: Missing[Literal["business", "enterprise", "unknown"]] = Field(
        default=UNSET,
        description="The Copilot plan of the organization, or the parent enterprise, when applicable.",
    )


class EnterpriseTeam(GitHubModel):
    """Enterprise Team

    Group of enterprise owners and/or members
    """

    id: int = Field()
    name: str = Field()
    slug: str = Field()
    url: str = Field()
    sync_to_organizations: str = Field()
    group_id: Missing[Union[str, None]] = Field(default=UNSET)
    group_name: Missing[Union[str, None]] = Field(default=UNSET)
    html_url: str = Field()
    members_url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(CopilotSeatDetails)
model_rebuild(EnterpriseTeam)

__all__ = (
    "CopilotSeatDetails",
    "EnterpriseTeam",
)
