"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0778 import WebhookRepositoryRulesetEditedPropChangesPropConditionsType
from .group_0780 import WebhookRepositoryRulesetEditedPropChangesPropRulesType


class WebhookRepositoryRulesetEditedPropChangesType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChanges"""

    name: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropNameType]
    enforcement: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropEnforcementType
    ]
    conditions: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropConditionsType]
    rules: NotRequired[WebhookRepositoryRulesetEditedPropChangesPropRulesType]


class WebhookRepositoryRulesetEditedPropChangesPropNameType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropName"""

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropEnforcementType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropEnforcement"""

    from_: NotRequired[str]


__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropEnforcementType",
    "WebhookRepositoryRulesetEditedPropChangesPropNameType",
    "WebhookRepositoryRulesetEditedPropChangesType",
)
