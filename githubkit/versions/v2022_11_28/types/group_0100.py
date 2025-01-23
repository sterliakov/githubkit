"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class InteractionLimitType(TypedDict):
    """Interaction Restrictions

    Limit interactions to a specific type of user for a specified duration
    """

    limit: Literal["existing_users", "contributors_only", "collaborators_only"]
    expiry: NotRequired[
        Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
    ]


__all__ = ("InteractionLimitType",)
