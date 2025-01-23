"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0065 import ActionsHostedRunnerImage


class OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200(GitHubModel):
    """OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200"""

    total_count: int = Field()
    images: builtins.list[ActionsHostedRunnerImage] = Field()


model_rebuild(OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200)

__all__ = ("OrgsOrgActionsHostedRunnersImagesPartnerGetResponse200",)
