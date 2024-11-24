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

from .group_0019 import Repository


class UserInstallationsInstallationIdRepositoriesGetResponse200(GitHubModel):
    """UserInstallationsInstallationIdRepositoriesGetResponse200"""

    total_count: int = Field()
    repository_selection: Missing[str] = Field(default=UNSET)
    repositories: list[Repository] = Field()


model_rebuild(UserInstallationsInstallationIdRepositoriesGetResponse200)

__all__ = ("UserInstallationsInstallationIdRepositoriesGetResponse200",)
