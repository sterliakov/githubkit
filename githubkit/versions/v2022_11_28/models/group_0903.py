"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgSettingsNetworkConfigurationsGetResponse200(GitHubModel):
    """OrgsOrgSettingsNetworkConfigurationsGetResponse200"""

    total_count: int = Field()
    network_configurations: builtins.list[NetworkConfiguration] = Field()


class NetworkConfiguration(GitHubModel):
    """Hosted compute network configuration

    A hosted compute network configuration.
    """

    id: str = Field(description="The unique identifier of the network configuration.")
    name: str = Field(description="The name of the network configuration.")
    compute_service: Missing[Literal["none", "actions", "codespaces"]] = Field(
        default=UNSET,
        description="The hosted compute service the network configuration supports.",
    )
    network_settings_ids: Missing[builtins.list[str]] = Field(
        default=UNSET,
        description="The unique identifier of each network settings in the configuration.",
    )
    created_on: Union[datetime, None] = Field(
        description="The time at which the network configuration was created, in ISO 8601 format."
    )


model_rebuild(OrgsOrgSettingsNetworkConfigurationsGetResponse200)
model_rebuild(NetworkConfiguration)

__all__ = (
    "NetworkConfiguration",
    "OrgsOrgSettingsNetworkConfigurationsGetResponse200",
)
