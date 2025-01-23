"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0001 import CvssSeveritiesType
from .group_0033 import DependabotAlertSecurityVulnerabilityType


class DependabotAlertSecurityAdvisoryType(TypedDict):
    """DependabotAlertSecurityAdvisory

    Details for the GitHub Security Advisory.
    """

    ghsa_id: str
    cve_id: Union[str, None]
    summary: str
    description: str
    vulnerabilities: builtins.list[DependabotAlertSecurityVulnerabilityType]
    severity: Literal["low", "medium", "high", "critical"]
    cvss: DependabotAlertSecurityAdvisoryPropCvssType
    cvss_severities: NotRequired[Union[CvssSeveritiesType, None]]
    cwes: builtins.list[DependabotAlertSecurityAdvisoryPropCwesItemsType]
    identifiers: builtins.list[DependabotAlertSecurityAdvisoryPropIdentifiersItemsType]
    references: builtins.list[DependabotAlertSecurityAdvisoryPropReferencesItemsType]
    published_at: datetime
    updated_at: datetime
    withdrawn_at: Union[datetime, None]


class DependabotAlertSecurityAdvisoryPropCvssType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropCvss

    Details for the advisory pertaining to the Common Vulnerability Scoring System.
    """

    score: float
    vector_string: Union[str, None]


class DependabotAlertSecurityAdvisoryPropCwesItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropCwesItems

    A CWE weakness assigned to the advisory.
    """

    cwe_id: str
    name: str


class DependabotAlertSecurityAdvisoryPropIdentifiersItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropIdentifiersItems

    An advisory identifier.
    """

    type: Literal["CVE", "GHSA"]
    value: str


class DependabotAlertSecurityAdvisoryPropReferencesItemsType(TypedDict):
    """DependabotAlertSecurityAdvisoryPropReferencesItems

    A link to additional advisory information.
    """

    url: str


__all__ = (
    "DependabotAlertSecurityAdvisoryPropCvssType",
    "DependabotAlertSecurityAdvisoryPropCwesItemsType",
    "DependabotAlertSecurityAdvisoryPropIdentifiersItemsType",
    "DependabotAlertSecurityAdvisoryPropReferencesItemsType",
    "DependabotAlertSecurityAdvisoryType",
)
