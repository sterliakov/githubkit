"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Optional, overload
from weakref import ref

from pydantic import BaseModel

from githubkit.compat import model_dump, type_validate_python
from githubkit.typing import Missing, UnsetType
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    import builtins
    from typing import Literal, Union

    from githubkit import GitHubCore
    from githubkit.response import Response
    from githubkit.typing import Missing
    from githubkit.utils import UNSET

    from ..models import (
        OrganizationSecretScanningAlert,
        SecretScanningAlert,
        SecretScanningLocation,
        SecretScanningPushProtectionBypass,
        SecretScanningScanHistory,
    )
    from ..types import (
        OrganizationSecretScanningAlertType,
        ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
        ReposOwnerRepoSecretScanningPushProtectionBypassesPostBodyType,
        SecretScanningAlertType,
        SecretScanningLocationType,
        SecretScanningPushProtectionBypassType,
        SecretScanningScanHistoryType,
    )


class SecretScanningClient:
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

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[OrganizationSecretScanningAlert],
        builtins.list[OrganizationSecretScanningAlertType],
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-enterprise"""

        import builtins

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            OrganizationSecretScanningAlert,
        )

        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[OrganizationSecretScanningAlert],
        builtins.list[OrganizationSecretScanningAlertType],
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-enterprise"""

        import builtins

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            OrganizationSecretScanningAlert,
        )

        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[OrganizationSecretScanningAlert],
        builtins.list[OrganizationSecretScanningAlertType],
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-organization"""

        import builtins

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            OrganizationSecretScanningAlert,
        )

        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[OrganizationSecretScanningAlert],
        builtins.list[OrganizationSecretScanningAlertType],
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-organization"""

        import builtins

        from ..models import (
            BasicError,
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            OrganizationSecretScanningAlert,
        )

        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[SecretScanningAlert], builtins.list[SecretScanningAlertType]
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-a-repository"""

        import builtins

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = UNSET,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        validity: Missing[str] = UNSET,
        is_publicly_leaked: Missing[bool] = UNSET,
        is_multi_repo: Missing[bool] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[SecretScanningAlert], builtins.list[SecretScanningAlertType]
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-a-repository"""

        import builtins

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
            "validity": validity,
            "is_publicly_leaked": is_publicly_leaked,
            "is_multi_repo": is_multi_repo,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#get-a-secret-scanning-alert"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#get-a-secret-scanning-alert"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]: ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]: ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs: Any,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#update-a-secret-scanning-alert"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json: Any = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(  # type: ignore[call-overload]
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]: ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]: ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs: Any,
    ) -> Response[SecretScanningAlert, SecretScanningAlertType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#update-a-secret-scanning-alert"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
            SecretScanningAlert,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json: Any = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(  # type: ignore[call-overload]
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[SecretScanningLocation], builtins.list[SecretScanningLocationType]
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-locations-for-a-secret-scanning-alert"""

        import builtins

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningLocation,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[
        builtins.list[SecretScanningLocation], builtins.list[SecretScanningLocationType]
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#list-locations-for-a-secret-scanning-alert"""

        import builtins

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningLocation,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=builtins.list[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: ReposOwnerRepoSecretScanningPushProtectionBypassesPostBodyType,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]: ...

    @overload
    def create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        reason: Literal["false_positive", "used_in_tests", "will_fix_later"],
        placeholder_id: str,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]: ...

    def create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningPushProtectionBypassesPostBodyType
        ] = UNSET,
        **kwargs: Any,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#create-a-push-protection-bypass"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            ReposOwnerRepoSecretScanningPushProtectionBypassesPostBody,
            SecretScanningPushProtectionBypass,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json: Any = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                ReposOwnerRepoSecretScanningPushProtectionBypassesPostBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(  # type: ignore[call-overload]
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningPushProtectionBypass,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: ReposOwnerRepoSecretScanningPushProtectionBypassesPostBodyType,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]: ...

    @overload
    async def async_create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        data: UnsetType = UNSET,
        headers: Optional[Mapping[str, str]] = None,
        reason: Literal["false_positive", "used_in_tests", "will_fix_later"],
        placeholder_id: str,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]: ...

    async def async_create_push_protection_bypass(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        data: Missing[
            ReposOwnerRepoSecretScanningPushProtectionBypassesPostBodyType
        ] = UNSET,
        **kwargs: Any,
    ) -> Response[
        SecretScanningPushProtectionBypass, SecretScanningPushProtectionBypassType
    ]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#create-a-push-protection-bypass"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            ReposOwnerRepoSecretScanningPushProtectionBypassesPostBody,
            SecretScanningPushProtectionBypass,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses"

        headers = {
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": self._REST_API_VERSION,
            **(headers or {}),
        }

        json: Any = kwargs if data is UNSET else data
        if self._github.config.rest_api_validate_body:
            json = type_validate_python(
                ReposOwnerRepoSecretScanningPushProtectionBypassesPostBody, json
            )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(  # type: ignore[call-overload]
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningPushProtectionBypass,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_scan_history(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SecretScanningScanHistory, SecretScanningScanHistoryType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#get-secret-scanning-scan-history-for-a-repository"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningScanHistory,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/scan-history"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(  # type: ignore[call-overload]
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningScanHistory,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_scan_history(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[SecretScanningScanHistory, SecretScanningScanHistoryType]:
        """See also: https://docs.github.com/rest/secret-scanning/secret-scanning#get-secret-scanning-scan-history-for-a-repository"""

        from ..models import (
            EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            SecretScanningScanHistory,
        )

        url = f"/repos/{owner}/{repo}/secret-scanning/scan-history"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(  # type: ignore[call-overload]
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningScanHistory,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )
