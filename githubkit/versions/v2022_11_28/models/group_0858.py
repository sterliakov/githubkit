"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgCodespacesAccessPutBody(GitHubModel):
    """OrgsOrgCodespacesAccessPutBody"""

    visibility: Literal[
        "disabled",
        "selected_members",
        "all_members",
        "all_members_and_outside_collaborators",
    ] = Field(
        description="Which users can access codespaces in the organization. `disabled` means that no users can access codespaces in the organization."
    )
    selected_usernames: Missing[builtins.list[str]] = Field(
        max_length=100 if PYDANTIC_V2 else None,
        default=UNSET,
        description="The usernames of the organization members who should have access to codespaces in the organization. Required when `visibility` is `selected_members`. The provided list of usernames will replace any existing value.",
    )


model_rebuild(OrgsOrgCodespacesAccessPutBody)

__all__ = ("OrgsOrgCodespacesAccessPutBody",)
