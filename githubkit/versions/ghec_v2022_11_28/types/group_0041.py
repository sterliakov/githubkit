"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any
from typing_extensions import NotRequired, TypeAlias, TypedDict


class AuditLogEventType(TypedDict):
    """AuditLogEvent"""

    timestamp: NotRequired[int]
    action: NotRequired[str]
    active: NotRequired[bool]
    active_was: NotRequired[bool]
    actor: NotRequired[str]
    actor_id: NotRequired[int]
    actor_location: NotRequired[AuditLogEventPropActorLocationType]
    data: NotRequired[AuditLogEventPropDataType]
    org_id: NotRequired[int]
    user_id: NotRequired[int]
    business_id: NotRequired[int]
    blocked_user: NotRequired[str]
    business: NotRequired[str]
    config: NotRequired[list[AuditLogEventPropConfigItemsType]]
    config_was: NotRequired[list[AuditLogEventPropConfigWasItemsType]]
    content_type: NotRequired[str]
    operation_type: NotRequired[str]
    created_at: NotRequired[int]
    deploy_key_fingerprint: NotRequired[str]
    document_id: NotRequired[str]
    emoji: NotRequired[str]
    events: NotRequired[list[AuditLogEventPropEventsItemsType]]
    events_were: NotRequired[list[AuditLogEventPropEventsWereItemsType]]
    explanation: NotRequired[str]
    fingerprint: NotRequired[str]
    hook_id: NotRequired[int]
    limited_availability: NotRequired[bool]
    message: NotRequired[str]
    name: NotRequired[str]
    old_user: NotRequired[str]
    openssh_public_key: NotRequired[str]
    org: NotRequired[str]
    previous_visibility: NotRequired[str]
    read_only: NotRequired[bool]
    repo: NotRequired[str]
    repository: NotRequired[str]
    repository_public: NotRequired[bool]
    target_login: NotRequired[str]
    team: NotRequired[str]
    transport_protocol: NotRequired[int]
    transport_protocol_name: NotRequired[str]
    user: NotRequired[str]
    visibility: NotRequired[str]


class AuditLogEventPropActorLocationType(TypedDict):
    """AuditLogEventPropActorLocation"""

    country_name: NotRequired[str]


AuditLogEventPropDataType: TypeAlias = dict[str, Any]
"""AuditLogEventPropData
"""


class AuditLogEventPropConfigItemsType(TypedDict):
    """AuditLogEventPropConfigItems"""


class AuditLogEventPropConfigWasItemsType(TypedDict):
    """AuditLogEventPropConfigWasItems"""


class AuditLogEventPropEventsItemsType(TypedDict):
    """AuditLogEventPropEventsItems"""


class AuditLogEventPropEventsWereItemsType(TypedDict):
    """AuditLogEventPropEventsWereItems"""


__all__ = (
    "AuditLogEventPropActorLocationType",
    "AuditLogEventPropConfigItemsType",
    "AuditLogEventPropConfigWasItemsType",
    "AuditLogEventPropDataType",
    "AuditLogEventPropEventsItemsType",
    "AuditLogEventPropEventsWereItemsType",
    "AuditLogEventType",
)
