"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ProjectsColumnsCardsCardIdMovesPostResponse503(GitHubModel):
    """ProjectsColumnsCardsCardIdMovesPostResponse503"""

    code: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)
    errors: Missing[
        builtins.list[ProjectsColumnsCardsCardIdMovesPostResponse503PropErrorsItems]
    ] = Field(default=UNSET)


class ProjectsColumnsCardsCardIdMovesPostResponse503PropErrorsItems(GitHubModel):
    """ProjectsColumnsCardsCardIdMovesPostResponse503PropErrorsItems"""

    code: Missing[str] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)


model_rebuild(ProjectsColumnsCardsCardIdMovesPostResponse503)
model_rebuild(ProjectsColumnsCardsCardIdMovesPostResponse503PropErrorsItems)

__all__ = (
    "ProjectsColumnsCardsCardIdMovesPostResponse503",
    "ProjectsColumnsCardsCardIdMovesPostResponse503PropErrorsItems",
)
