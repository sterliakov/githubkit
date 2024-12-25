"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0262 import Metadata


class Manifest(GitHubModel):
    """Manifest"""

    name: str = Field(description="The name of the manifest.")
    file: Missing[ManifestPropFile] = Field(default=UNSET)
    metadata: Missing[Metadata] = Field(
        default=UNSET,
        title="metadata",
        description="User-defined metadata to store domain-specific information limited to 8 keys with scalar values.",
    )
    resolved: Missing[ManifestPropResolved] = Field(
        default=UNSET, description="A collection of resolved package dependencies."
    )


class ManifestPropFile(GitHubModel):
    """ManifestPropFile"""

    source_location: Missing[str] = Field(
        default=UNSET,
        description="The path of the manifest file relative to the root of the Git repository.",
    )


class ManifestPropResolved(ExtraGitHubModel):
    """ManifestPropResolved

    A collection of resolved package dependencies.
    """


model_rebuild(Manifest)
model_rebuild(ManifestPropFile)
model_rebuild(ManifestPropResolved)

__all__ = (
    "Manifest",
    "ManifestPropFile",
    "ManifestPropResolved",
)
