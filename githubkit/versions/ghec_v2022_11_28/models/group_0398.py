"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class UserRoleItems(GitHubModel):
    """UserRoleItems"""

    display: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    value: Literal[
        "user",
        "27d9891d-2c17-4f45-a262-781a0e55c80a",
        "guest_collaborator",
        "1ebc4a02-e56c-43a6-92a5-02ee09b90824",
        "enterprise_owner",
        "981df190-8801-4618-a08a-d91f6206c954",
        "ba4987ab-a1c3-412a-b58c-360fc407cb10",
        "billing_manager",
        "0e338b8c-cc7f-498a-928d-ea3470d7e7e3",
        "e6be2762-e4ad-4108-b72d-1bbe884a0f91",
    ] = Field(description="The role value representing a user role in GitHub.")
    primary: Missing[bool] = Field(
        default=UNSET, description="Is the role a primary role for the user."
    )


model_rebuild(UserRoleItems)

__all__ = ("UserRoleItems",)
