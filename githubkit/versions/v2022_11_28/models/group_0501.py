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


class WebhookForkPropForkeeAllof0PropPermissions(GitHubModel):
    """WebhookForkPropForkeeAllof0PropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)


model_rebuild(WebhookForkPropForkeeAllof0PropPermissions)

__all__ = ("WebhookForkPropForkeeAllof0PropPermissions",)
