"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class ApiInsightsUserStatsItems(GitHubModel):
    """ApiInsightsUserStatsItems"""

    actor_type: Missing[str] = Field(default=UNSET)
    actor_name: Missing[str] = Field(default=UNSET)
    actor_id: Missing[int] = Field(default=UNSET)
    integration_id: Missing[Union[int, None]] = Field(default=UNSET)
    oauth_application_id: Missing[Union[int, None]] = Field(default=UNSET)
    total_request_count: Missing[int] = Field(default=UNSET)
    rate_limited_request_count: Missing[int] = Field(default=UNSET)
    last_rate_limited_timestamp: Missing[Union[str, None]] = Field(default=UNSET)
    last_request_timestamp: Missing[str] = Field(default=UNSET)


model_rebuild(ApiInsightsUserStatsItems)

__all__ = ("ApiInsightsUserStatsItems",)
