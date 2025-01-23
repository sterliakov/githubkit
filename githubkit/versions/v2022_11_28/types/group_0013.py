"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Union
from typing_extensions import NotRequired, TypedDict


class ValidationErrorType(TypedDict):
    """Validation Error

    Validation Error
    """

    message: str
    documentation_url: str
    errors: NotRequired[builtins.list[ValidationErrorPropErrorsItemsType]]


class ValidationErrorPropErrorsItemsType(TypedDict):
    """ValidationErrorPropErrorsItems"""

    resource: NotRequired[str]
    field: NotRequired[str]
    message: NotRequired[str]
    code: str
    index: NotRequired[int]
    value: NotRequired[Union[str, None, int, None, builtins.list[str], None]]


__all__ = (
    "ValidationErrorPropErrorsItemsType",
    "ValidationErrorType",
)
