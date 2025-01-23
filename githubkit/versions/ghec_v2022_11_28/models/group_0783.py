"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0784 import WebhookRepositoryRulesetEditedPropChangesPropConditions
from .group_0786 import WebhookRepositoryRulesetEditedPropChangesPropRules


class WebhookRepositoryRulesetEditedPropChanges(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChanges"""

    name: Missing[WebhookRepositoryRulesetEditedPropChangesPropName] = Field(
        default=UNSET
    )
    enforcement: Missing[WebhookRepositoryRulesetEditedPropChangesPropEnforcement] = (
        Field(default=UNSET)
    )
    conditions: Missing[WebhookRepositoryRulesetEditedPropChangesPropConditions] = (
        Field(default=UNSET)
    )
    rules: Missing[WebhookRepositoryRulesetEditedPropChangesPropRules] = Field(
        default=UNSET
    )


class WebhookRepositoryRulesetEditedPropChangesPropName(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropName"""

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropEnforcement(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropEnforcement"""

    from_: Missing[str] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryRulesetEditedPropChanges)
model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropName)
model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropEnforcement)

__all__ = (
    "WebhookRepositoryRulesetEditedPropChanges",
    "WebhookRepositoryRulesetEditedPropChangesPropEnforcement",
    "WebhookRepositoryRulesetEditedPropChangesPropName",
)
