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


class CodespacesPublicKey(GitHubModel):
    """CodespacesPublicKey

    The public key used for setting Codespaces secrets.
    """

    key_id: str = Field(description="The identifier for the key.")
    key: str = Field(description="The Base64 encoded public key.")
    id: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)


model_rebuild(CodespacesPublicKey)

__all__ = ("CodespacesPublicKey",)
