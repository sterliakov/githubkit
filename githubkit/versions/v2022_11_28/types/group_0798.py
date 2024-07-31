"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgCodeSecurityConfigurationsPostBodyType(TypedDict):
    """OrgsOrgCodeSecurityConfigurationsPostBody"""

    name: str
    description: str
    advanced_security: NotRequired[Literal["enabled", "disabled"]]
    dependency_graph: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_alerts: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_security_updates: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning_push_protection: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_validity_checks: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    private_vulnerability_reporting: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    enforcement: NotRequired[Literal["enforced", "unenforced"]]


__all__ = ("OrgsOrgCodeSecurityConfigurationsPostBodyType",)
