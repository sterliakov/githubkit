"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0074 import (
    EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType,
)
from .group_0078 import RepositoryRulesetConditionsPropRefNameType
from .group_0080 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType,
)


class EnterpriseRulesetConditionsOneof1Type(TypedDict):
    """organization_name_and_repository_property

    Conditions to target organizations by name and repositories by property
    """

    organization_name: (
        EnterpriseRulesetConditionsOrganizationNameTargetPropOrganizationNameType
    )
    repository_property: (
        RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType
    )
    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]


__all__ = ("EnterpriseRulesetConditionsOneof1Type",)
