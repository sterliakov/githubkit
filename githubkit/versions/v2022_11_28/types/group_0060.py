"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class BillingUsageReportType(TypedDict):
    """BillingUsageReport"""

    usage_items: NotRequired[builtins.list[BillingUsageReportPropUsageItemsItemsType]]


class BillingUsageReportPropUsageItemsItemsType(TypedDict):
    """BillingUsageReportPropUsageItemsItems"""

    date: str
    product: str
    sku: str
    quantity: int
    unit_type: str
    price_per_unit: float
    gross_amount: float
    discount_amount: float
    net_amount: float
    organization_name: str
    repository_name: NotRequired[str]


__all__ = (
    "BillingUsageReportPropUsageItemsItemsType",
    "BillingUsageReportType",
)
