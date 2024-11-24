"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0017 import InstallationType
from .group_0427 import EnterpriseWebhooksType
from .group_0429 import OrganizationSimpleWebhooksType
from .group_0430 import RepositoryWebhooksType
from .group_0440 import WebhooksUserType
from .group_0446 import WebhooksRepositoriesAddedItemsType


class WebhookInstallationRepositoriesRemovedType(TypedDict):
    """installation_repositories removed event"""

    action: Literal["removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: list[WebhooksRepositoriesAddedItemsType]
    repositories_removed: list[
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
