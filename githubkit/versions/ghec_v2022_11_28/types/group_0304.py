"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing_extensions import NotRequired, TypedDict


class DependencyGraphSpdxSbomType(TypedDict):
    """Dependency Graph SPDX SBOM

    A schema for the SPDX JSON format returned by the Dependency Graph.
    """

    sbom: DependencyGraphSpdxSbomPropSbomType


class DependencyGraphSpdxSbomPropSbomType(TypedDict):
    """DependencyGraphSpdxSbomPropSbom"""

    spdxid: str
    spdx_version: str
    comment: NotRequired[str]
    creation_info: DependencyGraphSpdxSbomPropSbomPropCreationInfoType
    name: str
    data_license: str
    document_namespace: str
    packages: builtins.list[DependencyGraphSpdxSbomPropSbomPropPackagesItemsType]
    relationships: NotRequired[
        builtins.list[DependencyGraphSpdxSbomPropSbomPropRelationshipsItemsType]
    ]


class DependencyGraphSpdxSbomPropSbomPropCreationInfoType(TypedDict):
    """DependencyGraphSpdxSbomPropSbomPropCreationInfo"""

    created: str
    creators: builtins.list[str]


class DependencyGraphSpdxSbomPropSbomPropRelationshipsItemsType(TypedDict):
    """DependencyGraphSpdxSbomPropSbomPropRelationshipsItems"""

    relationship_type: NotRequired[str]
    spdx_element_id: NotRequired[str]
    related_spdx_element: NotRequired[str]


class DependencyGraphSpdxSbomPropSbomPropPackagesItemsType(TypedDict):
    """DependencyGraphSpdxSbomPropSbomPropPackagesItems"""

    spdxid: NotRequired[str]
    name: NotRequired[str]
    version_info: NotRequired[str]
    download_location: NotRequired[str]
    files_analyzed: NotRequired[bool]
    license_concluded: NotRequired[str]
    license_declared: NotRequired[str]
    supplier: NotRequired[str]
    copyright_text: NotRequired[str]
    external_refs: NotRequired[
        builtins.list[
            DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItemsType
        ]
    ]


class DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItemsType(
    TypedDict
):
    """DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItems"""

    reference_category: str
    reference_locator: str
    reference_type: str


__all__ = (
    "DependencyGraphSpdxSbomPropSbomPropCreationInfoType",
    "DependencyGraphSpdxSbomPropSbomPropPackagesItemsPropExternalRefsItemsType",
    "DependencyGraphSpdxSbomPropSbomPropPackagesItemsType",
    "DependencyGraphSpdxSbomPropSbomPropRelationshipsItemsType",
    "DependencyGraphSpdxSbomPropSbomType",
    "DependencyGraphSpdxSbomType",
)
