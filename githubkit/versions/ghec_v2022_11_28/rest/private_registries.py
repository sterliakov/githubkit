"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional, overload
from weakref import ref

from pydantic import BaseModel

from githubkit.compat import model_dump, type_validate_python
from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from typing import Literal, Union

    from githubkit import GitHubCore
    from githubkit.response import Response
    from githubkit.typing import Missing
    from githubkit.utils import UNSET

    from ..models import (
        OrgPrivateRegistryConfiguration,
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgsOrgPrivateRegistriesGetResponse200,
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200,
    )
    from ..types import (
        OrgPrivateRegistryConfigurationType,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
        OrgsOrgPrivateRegistriesGetResponse200Type,
        OrgsOrgPrivateRegistriesPostBodyType,
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200Type,
        OrgsOrgPrivateRegistriesSecretNamePatchBodyType,
    )


class PrivateRegistriesClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def list_org_private_registries(
        self,
        org: str,
        *,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[
        OrgsOrgPrivateRegistriesGetResponse200,
        OrgsOrgPrivateRegistriesGetResponse200Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#list-private-registries-for-an-organization"""

        from ..models import BasicError, OrgsOrgPrivateRegistriesGetResponse200

        url = f"/orgs/{org}/private-registries"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrgsOrgPrivateRegistriesGetResponse200,
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_org_private_registries(
        self,
        org: str,
        *,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[
        OrgsOrgPrivateRegistriesGetResponse200,
        OrgsOrgPrivateRegistriesGetResponse200Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#list-private-registries-for-an-organization"""

        from ..models import BasicError, OrgsOrgPrivateRegistriesGetResponse200

        url = f"/orgs/{org}/private-registries"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=OrgsOrgPrivateRegistriesGetResponse200,
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_org_private_registry(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: OrgsOrgPrivateRegistriesPostBodyType,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]: ...

    @overload
    def create_org_private_registry(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        registry_type: Literal["maven_repository"],
        username: Missing[Union[str, None]] = UNSET,
        encrypted_value: str,
        key_id: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Missing[list[int]] = UNSET,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]: ...

    def create_org_private_registry(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[OrgsOrgPrivateRegistriesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#create-a-private-registry-for-an-organization"""

        from ..models import (
            BasicError,
            OrgPrivateRegistryConfigurationWithSelectedRepositories,
            OrgsOrgPrivateRegistriesPostBody,
            ValidationError,
        )

        url = f"/orgs/{org}/private-registries"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(OrgsOrgPrivateRegistriesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgPrivateRegistryConfigurationWithSelectedRepositories,
            error_models={
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_org_private_registry(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: OrgsOrgPrivateRegistriesPostBodyType,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]: ...

    @overload
    async def async_create_org_private_registry(
        self,
        org: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        registry_type: Literal["maven_repository"],
        username: Missing[Union[str, None]] = UNSET,
        encrypted_value: str,
        key_id: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Missing[list[int]] = UNSET,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]: ...

    async def async_create_org_private_registry(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[OrgsOrgPrivateRegistriesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[
        OrgPrivateRegistryConfigurationWithSelectedRepositories,
        OrgPrivateRegistryConfigurationWithSelectedRepositoriesType,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#create-a-private-registry-for-an-organization"""

        from ..models import (
            BasicError,
            OrgPrivateRegistryConfigurationWithSelectedRepositories,
            OrgsOrgPrivateRegistriesPostBody,
            ValidationError,
        )

        url = f"/orgs/{org}/private-registries"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(OrgsOrgPrivateRegistriesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=OrgPrivateRegistryConfigurationWithSelectedRepositories,
            error_models={
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def get_org_public_key(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200,
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization"""

        from ..models import BasicError, OrgsOrgPrivateRegistriesPublicKeyGetResponse200

        url = f"/orgs/{org}/private-registries/public-key"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OrgsOrgPrivateRegistriesPublicKeyGetResponse200,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_org_public_key(
        self,
        org: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200,
        OrgsOrgPrivateRegistriesPublicKeyGetResponse200Type,
    ]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization"""

        from ..models import BasicError, OrgsOrgPrivateRegistriesPublicKeyGetResponse200

        url = f"/orgs/{org}/private-registries/public-key"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OrgsOrgPrivateRegistriesPublicKeyGetResponse200,
            error_models={
                "404": BasicError,
            },
        )

    def get_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[OrgPrivateRegistryConfiguration, OrgPrivateRegistryConfigurationType]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#get-a-private-registry-for-an-organization"""

        from ..models import BasicError, OrgPrivateRegistryConfiguration

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OrgPrivateRegistryConfiguration,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[OrgPrivateRegistryConfiguration, OrgPrivateRegistryConfigurationType]:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#get-a-private-registry-for-an-organization"""

        from ..models import BasicError, OrgPrivateRegistryConfiguration

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OrgPrivateRegistryConfiguration,
            error_models={
                "404": BasicError,
            },
        )

    def delete_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#delete-a-private-registry-for-an-organization"""

        from ..models import BasicError

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    async def async_delete_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#delete-a-private-registry-for-an-organization"""

        from ..models import BasicError

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            headers=exclude_unset(headers),
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: OrgsOrgPrivateRegistriesSecretNamePatchBodyType,
    ) -> Response: ...

    @overload
    def update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        registry_type: Missing[Literal["maven_repository"]] = UNSET,
        username: Missing[Union[str, None]] = UNSET,
        encrypted_value: Missing[str] = UNSET,
        key_id: Missing[str] = UNSET,
        visibility: Missing[Literal["all", "private", "selected"]] = UNSET,
        selected_repository_ids: Missing[list[int]] = UNSET,
    ) -> Response: ...

    def update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[OrgsOrgPrivateRegistriesSecretNamePatchBodyType] = UNSET,
        **kwargs,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgPrivateRegistriesSecretNamePatchBody,
            ValidationError,
        )

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                OrgsOrgPrivateRegistriesSecretNamePatchBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            error_models={
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: OrgsOrgPrivateRegistriesSecretNamePatchBodyType,
    ) -> Response: ...

    @overload
    async def async_update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[dict[str, str]] = None,
        registry_type: Missing[Literal["maven_repository"]] = UNSET,
        username: Missing[Union[str, None]] = UNSET,
        encrypted_value: Missing[str] = UNSET,
        key_id: Missing[str] = UNSET,
        visibility: Missing[Literal["all", "private", "selected"]] = UNSET,
        selected_repository_ids: Missing[list[int]] = UNSET,
    ) -> Response: ...

    async def async_update_org_private_registry(
        self,
        org: str,
        secret_name: str,
        *,
        headers: Optional[dict[str, str]] = None,
        data: Missing[OrgsOrgPrivateRegistriesSecretNamePatchBodyType] = UNSET,
        **kwargs,
    ) -> Response:
        """See also: https://docs.github.com/enterprise-cloud@latest//rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization"""

        from ..models import (
            BasicError,
            OrgsOrgPrivateRegistriesSecretNamePatchBody,
            ValidationError,
        )

        url = f"/orgs/{org}/private-registries/{secret_name}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                OrgsOrgPrivateRegistriesSecretNamePatchBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            error_models={
                "404": BasicError,
                "422": ValidationError,
            },
        )
