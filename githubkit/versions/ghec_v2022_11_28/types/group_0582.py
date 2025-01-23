"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0017 import InstallationType
from .group_0450 import EnterpriseWebhooksType
from .group_0452 import OrganizationSimpleWebhooksType
from .group_0453 import RepositoryWebhooksType
from .group_0463 import WebhooksUserType
from .group_0469 import WebhooksRepositoriesAddedItemsType


class WebhookInstallationRepositoriesRemovedType(TypedDict):
    """installation_repositories removed event"""

    action: Literal["removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: builtins.list[WebhooksRepositoriesAddedItemsType]
    repositories_removed: builtins.list[
        WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhooksUserType, None]
    sender: SimpleUserType


class WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


__all__ = (
    "WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType",
    "WebhookInstallationRepositoriesRemovedType",
)
