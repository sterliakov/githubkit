"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser


class ReposOwnerRepoCodespacesNewGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesNewGetResponse200"""

    billable_owner: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )
    defaults: Missing[ReposOwnerRepoCodespacesNewGetResponse200PropDefaults] = Field(
        default=UNSET
    )


class ReposOwnerRepoCodespacesNewGetResponse200PropDefaults(GitHubModel):
    """ReposOwnerRepoCodespacesNewGetResponse200PropDefaults"""

    location: str = Field()
    devcontainer_path: Union[str, None] = Field()


model_rebuild(ReposOwnerRepoCodespacesNewGetResponse200)
model_rebuild(ReposOwnerRepoCodespacesNewGetResponse200PropDefaults)

__all__ = (
    "ReposOwnerRepoCodespacesNewGetResponse200",
    "ReposOwnerRepoCodespacesNewGetResponse200PropDefaults",
)
