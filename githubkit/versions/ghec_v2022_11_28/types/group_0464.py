"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class WebhooksProjectChangesType(TypedDict):
    """WebhooksProjectChanges"""

    archived_at: NotRequired[WebhooksProjectChangesPropArchivedAtType]


class WebhooksProjectChangesPropArchivedAtType(TypedDict):
    """WebhooksProjectChangesPropArchivedAt"""

    from_: NotRequired[Union[datetime, None]]
    to: NotRequired[Union[datetime, None]]


__all__ = (
    "WebhooksProjectChangesPropArchivedAtType",
    "WebhooksProjectChangesType",
)
