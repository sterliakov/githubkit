"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0117 import RepositoryRulesetBypassActorType
from .group_0126 import OrgRulesetConditionsOneof0Type
from .group_0127 import OrgRulesetConditionsOneof1Type
from .group_0128 import OrgRulesetConditionsOneof2Type
from .group_0129 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0130 import RepositoryRuleUpdateType
from .group_0132 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0133 import RepositoryRuleMergeQueueType
from .group_0135 import RepositoryRuleRequiredDeploymentsType
from .group_0138 import RepositoryRulePullRequestType
from .group_0140 import RepositoryRuleRequiredStatusChecksType
from .group_0142 import RepositoryRuleCommitMessagePatternType
from .group_0144 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0146 import RepositoryRuleCommitterEmailPatternType
from .group_0148 import RepositoryRuleBranchNamePatternType
from .group_0150 import RepositoryRuleTagNamePatternType
from .group_0153 import RepositoryRuleWorkflowsType
from .group_0155 import RepositoryRuleCodeScanningType
from .group_0157 import RepositoryRuleOneof18Type


class OrgsOrgRulesetsRulesetIdPutBodyType(TypedDict):
    """OrgsOrgRulesetsRulesetIdPutBody"""

    name: NotRequired[str]
    target: NotRequired[Literal["branch", "tag", "push", "repository"]]
    enforcement: NotRequired[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[builtins.list[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[
        Union[
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
        ]
    ]
    rules: NotRequired[
        builtins.list[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleMergeQueueType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]


__all__ = ("OrgsOrgRulesetsRulesetIdPutBodyType",)
