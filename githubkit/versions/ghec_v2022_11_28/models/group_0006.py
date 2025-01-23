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


class ValidationErrorSimple(GitHubModel):
    """Validation Error Simple

    Validation Error Simple
    """

    message: str = Field()
    documentation_url: str = Field()
    errors: Missing[builtins.list[str]] = Field(default=UNSET)


model_rebuild(ValidationErrorSimple)

__all__ = ("ValidationErrorSimple",)
