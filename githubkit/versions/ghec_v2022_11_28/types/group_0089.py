"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0080 import (
    EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType,
)
from .group_0082 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType,
)
from .group_0084 import RepositoryRulesetConditionsPropRefNameType


class EnterpriseRulesetConditionsOneof0Type(TypedDict):
    """organization_name_and_repository_name

    Conditions to target organizations by name and all repositories
    """

    organization_name: (
        EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType
    )
    repository_name: (
        RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType
    )
    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]


__all__ = ("EnterpriseRulesetConditionsOneof0Type",)
