"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0262 import Metadata


class Snapshot(GitHubModel):
    """snapshot

    Create a new snapshot of a repository's dependencies.
    """

    version: int = Field(
        description="The version of the repository snapshot submission."
    )
    job: SnapshotPropJob = Field()
    sha: str = Field(
        min_length=40,
        max_length=40,
        description="The commit SHA associated with this dependency snapshot. Maximum length: 40 characters.",
    )
    ref: str = Field(
        pattern="^refs/",
        description="The repository branch that triggered this snapshot.",
    )
    detector: SnapshotPropDetector = Field(
        description="A description of the detector used."
    )
    metadata: Missing[Metadata] = Field(
        default=UNSET,
        title="metadata",
        description="User-defined metadata to store domain-specific information limited to 8 keys with scalar values.",
    )
    manifests: Missing[SnapshotPropManifests] = Field(
        default=UNSET,
        description="A collection of package manifests, which are a collection of related dependencies declared in a file or representing a logical group of dependencies.",
    )
    scanned: datetime = Field(description="The time at which the snapshot was scanned.")


class SnapshotPropJob(GitHubModel):
    """SnapshotPropJob"""

    id: str = Field(description="The external ID of the job.")
    correlator: str = Field(
        description="Correlator provides a key that is used to group snapshots submitted over time. Only the \"latest\" submitted snapshot for a given combination of `job.correlator` and `detector.name` will be considered when calculating a repository's current dependencies. Correlator should be as unique as it takes to distinguish all detection runs for a given \"wave\" of CI workflow you run. If you're using GitHub Actions, a good default value for this could be the environment variables GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build matrix, then you'll also need to add additional key(s) to distinguish between each submission inside a matrix variation."
    )
    html_url: Missing[str] = Field(default=UNSET, description="The url for the job.")


class SnapshotPropDetector(GitHubModel):
    """SnapshotPropDetector

    A description of the detector used.
    """

    name: str = Field(description="The name of the detector used.")
    version: str = Field(description="The version of the detector used.")
    url: str = Field(description="The url of the detector used.")


class SnapshotPropManifests(ExtraGitHubModel):
    """SnapshotPropManifests

    A collection of package manifests, which are a collection of related
    dependencies declared in a file or representing a logical group of dependencies.
    """


model_rebuild(Snapshot)
model_rebuild(SnapshotPropJob)
model_rebuild(SnapshotPropDetector)
model_rebuild(SnapshotPropManifests)

__all__ = (
    "Snapshot",
    "SnapshotPropDetector",
    "SnapshotPropJob",
    "SnapshotPropManifests",
)
