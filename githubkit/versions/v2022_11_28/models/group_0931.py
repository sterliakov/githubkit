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


class ProjectsProjectIdDeleteResponse403(GitHubModel):
    """ProjectsProjectIdDeleteResponse403"""

    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)
    errors: Missing[builtins.list[str]] = Field(default=UNSET)


model_rebuild(ProjectsProjectIdDeleteResponse403)

__all__ = ("ProjectsProjectIdDeleteResponse403",)
