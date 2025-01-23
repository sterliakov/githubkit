"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgPersonalAccessTokenRequestsPostBody(GitHubModel):
    """OrgsOrgPersonalAccessTokenRequestsPostBody"""

    pat_request_ids: Missing[builtins.list[int]] = Field(
        max_length=100 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        default=UNSET,
        description="Unique identifiers of the requests for access via fine-grained personal access token. Must be formed of between 1 and 100 `pat_request_id` values.",
    )
    action: Literal["approve", "deny"] = Field(
        description="Action to apply to the requests."
    )
    reason: Missing[Union[Annotated[str, Field(max_length=1024)], None]] = Field(
        default=UNSET,
        description="Reason for approving or denying the requests. Max 1024 characters.",
    )


model_rebuild(OrgsOrgPersonalAccessTokenRequestsPostBody)

__all__ = ("OrgsOrgPersonalAccessTokenRequestsPostBody",)
