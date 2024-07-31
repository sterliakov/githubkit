"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict

from .group_0377 import SimpleUserWebhooksType


class WebhookGithubAppAuthorizationRevokedType(TypedDict):
    """github_app_authorization revoked event"""

    action: Literal["revoked"]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookGithubAppAuthorizationRevokedType",)
