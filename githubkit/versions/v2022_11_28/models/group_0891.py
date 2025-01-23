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


class OrgsOrgPersonalAccessTokensPostBody(GitHubModel):
    """OrgsOrgPersonalAccessTokensPostBody"""

    action: Literal["revoke"] = Field(
        description="Action to apply to the fine-grained personal access token."
    )
    pat_ids: builtins.list[int] = Field(
        max_length=100 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        description="The IDs of the fine-grained personal access tokens.",
    )


model_rebuild(OrgsOrgPersonalAccessTokensPostBody)

__all__ = ("OrgsOrgPersonalAccessTokensPostBody",)
