"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing


class UserCodespacesCodespaceNamePublishPostBody(GitHubModel):
    """UserCodespacesCodespaceNamePublishPostBody"""

    name: Missing[str] = Field(
        default=UNSET, description="A name for the new repository."
    )
    private: Missing[bool] = Field(
        default=UNSET, description="Whether the new repository should be private."
    )


model_rebuild(UserCodespacesCodespaceNamePublishPostBody)

__all__ = ("UserCodespacesCodespaceNamePublishPostBody",)
