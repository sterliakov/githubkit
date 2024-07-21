"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class OrgCustomPropertyType(TypedDict):
    """Organization Custom Property

    Custom property defined on an organization
    """

    property_name: str
    value_type: Literal["string", "single_select", "multi_select", "true_false"]
    required: NotRequired[bool]
    default_value: NotRequired[Union[str, List[str], None]]
    description: NotRequired[Union[str, None]]
    allowed_values: NotRequired[Union[List[str], None]]
    values_editable_by: NotRequired[
        Union[None, Literal["org_actors", "org_and_repo_actors"]]
    ]


__all__ = ("OrgCustomPropertyType",)
