"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


class SshSigningKeyType(TypedDict):
    """SSH Signing Key

    A public SSH key used to sign Git commits
    """

    key: str
    id: int
    title: str
    created_at: datetime


__all__ = ("SshSigningKeyType",)
