"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0247 import DeploymentBranchPolicySettingsType
from .group_0249 import EnvironmentPropProtectionRulesItemsAnyof1Type


class EnvironmentType(TypedDict):
    """Environment

    Details of a deployment environment
    """

    id: int
    node_id: str
    name: str
    url: str
    html_url: str
    created_at: datetime
    updated_at: datetime
    protection_rules: NotRequired[
        List[
            Union[
                EnvironmentPropProtectionRulesItemsAnyof0Type,
                EnvironmentPropProtectionRulesItemsAnyof1Type,
                EnvironmentPropProtectionRulesItemsAnyof2Type,
            ]
        ]
    ]
    deployment_branch_policy: NotRequired[
        Union[DeploymentBranchPolicySettingsType, None]
    ]


class EnvironmentPropProtectionRulesItemsAnyof0Type(TypedDict):
    """EnvironmentPropProtectionRulesItemsAnyof0"""

    id: int
    node_id: str
    type: str
    wait_timer: NotRequired[int]


class EnvironmentPropProtectionRulesItemsAnyof2Type(TypedDict):
    """EnvironmentPropProtectionRulesItemsAnyof2"""

    id: int
    node_id: str
    type: str


class ReposOwnerRepoEnvironmentsGetResponse200Type(TypedDict):
    """ReposOwnerRepoEnvironmentsGetResponse200"""

    total_count: NotRequired[int]
    environments: NotRequired[List[EnvironmentType]]


__all__ = (
    "EnvironmentType",
    "EnvironmentPropProtectionRulesItemsAnyof0Type",
    "EnvironmentPropProtectionRulesItemsAnyof2Type",
    "ReposOwnerRepoEnvironmentsGetResponse200Type",
)
