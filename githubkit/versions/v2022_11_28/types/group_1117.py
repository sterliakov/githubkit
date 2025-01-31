"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import TypedDict


class UserCodespacesSecretsGetResponse200Type(TypedDict):
    """UserCodespacesSecretsGetResponse200"""

    total_count: int
    secrets: list[CodespacesSecretType]


class CodespacesSecretType(TypedDict):
    """Codespaces Secret

    Secrets for a GitHub Codespace.
    """

    name: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: str


__all__ = (
    "CodespacesSecretType",
    "UserCodespacesSecretsGetResponse200Type",
)
