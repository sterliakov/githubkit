"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class CustomPropertySetPayload(GitHubModel):
    """Custom Property Set Payload

    Custom property set payload
    """

    value_type: Literal["string", "single_select", "multi_select", "true_false"] = (
        Field(description="The type of the value for the property")
    )
    required: Missing[bool] = Field(
        default=UNSET, description="Whether the property is required."
    )
    default_value: Missing[Union[str, builtins.list[str], None]] = Field(
        default=UNSET, description="Default value of the property"
    )
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Short description of the property"
    )
    allowed_values: Missing[
        Union[
            Annotated[
                builtins.list[Annotated[str, Field(max_length=75)]],
                Field(max_length=200 if PYDANTIC_V2 else None),
            ],
            None,
        ]
    ] = Field(
        default=UNSET,
        description="An ordered list of the allowed values of the property.\nThe property can have up to 200 allowed values.",
    )


model_rebuild(CustomPropertySetPayload)

__all__ = ("CustomPropertySetPayload",)
