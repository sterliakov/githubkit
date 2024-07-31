"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0265 import MetadataType


class ManifestType(TypedDict):
    """Manifest"""

    name: str
    file: NotRequired[ManifestPropFileType]
    metadata: NotRequired[MetadataType]
    resolved: NotRequired[ManifestPropResolvedType]


class ManifestPropFileType(TypedDict):
    """ManifestPropFile"""

    source_location: NotRequired[str]


class ManifestPropResolvedType(TypedDict):
    """ManifestPropResolved

    A collection of resolved package dependencies.
    """


__all__ = (
    "ManifestType",
    "ManifestPropFileType",
    "ManifestPropResolvedType",
)
