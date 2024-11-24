"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal, Annotated
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0001 import CvssSeverities
from .group_0002 import SimpleUser
from .group_0056 import Team
from .group_0184 import RepositoryAdvisoryCredit


class RepositoryAdvisory(GitHubModel):
    """RepositoryAdvisory

    A repository security advisory.
    """

    ghsa_id: str = Field(description="The GitHub Security Advisory ID.")
    cve_id: Union[str, None] = Field(
        description="The Common Vulnerabilities and Exposures (CVE) ID."
    )
    url: str = Field(description="The API URL for the advisory.")
    html_url: str = Field(description="The URL for the advisory.")
    summary: str = Field(
        max_length=1024, description="A short summary of the advisory."
    )
    description: Union[Annotated[str, Field(max_length=65535)], None] = Field(
        description="A detailed description of what the advisory entails."
    )
    severity: Union[None, Literal["critical", "high", "medium", "low"]] = Field(
        description="The severity of the advisory."
    )
    author: None = Field(description="The author of the advisory.")
    publisher: None = Field(description="The publisher of the advisory.")
    identifiers: list[RepositoryAdvisoryPropIdentifiersItems] = Field()
    state: Literal["published", "closed", "withdrawn", "draft", "triage"] = Field(
        description="The state of the advisory."
    )
    created_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was created, in ISO 8601 format."
    )
    updated_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was last updated, in ISO 8601 format."
    )
    published_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was published, in ISO 8601 format."
    )
    closed_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was closed, in ISO 8601 format."
    )
    withdrawn_at: Union[datetime, None] = Field(
        description="The date and time of when the advisory was withdrawn, in ISO 8601 format."
    )
    submission: Union[RepositoryAdvisoryPropSubmission, None] = Field()
    vulnerabilities: Union[list[RepositoryAdvisoryVulnerability], None] = Field()
    cvss: Union[RepositoryAdvisoryPropCvss, None] = Field()
    cvss_severities: Missing[Union[CvssSeverities, None]] = Field(default=UNSET)
    cwes: Union[list[RepositoryAdvisoryPropCwesItems], None] = Field()
    cwe_ids: Union[list[str], None] = Field(description="A list of only the CWE IDs.")
    credits_: Union[list[RepositoryAdvisoryPropCreditsItems], None] = Field(
        alias="credits"
    )
    credits_detailed: Union[list[RepositoryAdvisoryCredit], None] = Field()
    collaborating_users: Union[list[SimpleUser], None] = Field(
        description="A list of users that collaborate on the advisory."
    )
    collaborating_teams: Union[list[Team], None] = Field(
        description="A list of teams that collaborate on the advisory."
    )
    private_fork: None = Field(
        description="A temporary private fork of the advisory's repository for collaborating on a fix."
    )


class RepositoryAdvisoryPropIdentifiersItems(GitHubModel):
    """RepositoryAdvisoryPropIdentifiersItems"""

    type: Literal["CVE", "GHSA"] = Field(description="The type of identifier.")
    value: str = Field(description="The identifier value.")


class RepositoryAdvisoryPropSubmission(GitHubModel):
    """RepositoryAdvisoryPropSubmission"""

    accepted: bool = Field(
        description="Whether a private vulnerability report was accepted by the repository's administrators."
    )


class RepositoryAdvisoryPropCvss(GitHubModel):
    """RepositoryAdvisoryPropCvss"""

    vector_string: Union[str, None] = Field(description="The CVSS vector.")
    score: Union[Annotated[float, Field(le=10.0)], None] = Field(
        description="The CVSS score."
    )


class RepositoryAdvisoryPropCwesItems(GitHubModel):
    """RepositoryAdvisoryPropCwesItems"""

    cwe_id: str = Field(description="The Common Weakness Enumeration (CWE) identifier.")
    name: str = Field(description="The name of the CWE.")


class RepositoryAdvisoryPropCreditsItems(GitHubModel):
    """RepositoryAdvisoryPropCreditsItems"""

    login: Missing[str] = Field(
        default=UNSET, description="The username of the user credited."
    )
    type: Missing[
        Literal[
            "analyst",
            "finder",
            "reporter",
            "coordinator",
            "remediation_developer",
            "remediation_reviewer",
            "remediation_verifier",
            "tool",
            "sponsor",
            "other",
        ]
    ] = Field(default=UNSET, description="The type of credit the user is receiving.")


class RepositoryAdvisoryVulnerability(GitHubModel):
    """RepositoryAdvisoryVulnerability

    A product affected by the vulnerability detailed in a repository security
    advisory.
    """

    package: Union[RepositoryAdvisoryVulnerabilityPropPackage, None] = Field(
        description="The name of the package affected by the vulnerability."
    )
    vulnerable_version_range: Union[str, None] = Field(
        description="The range of the package versions affected by the vulnerability."
    )
    patched_versions: Union[str, None] = Field(
        description="The package version(s) that resolve the vulnerability."
    )
    vulnerable_functions: Union[list[str], None] = Field(
        description="The functions in the package that are affected."
    )


class RepositoryAdvisoryVulnerabilityPropPackage(GitHubModel):
    """RepositoryAdvisoryVulnerabilityPropPackage

    The name of the package affected by the vulnerability.
    """

    ecosystem: Literal[
        "rubygems",
        "npm",
        "pip",
        "maven",
        "nuget",
        "composer",
        "go",
        "rust",
        "erlang",
        "actions",
        "pub",
        "other",
        "swift",
    ] = Field(description="The package's language or package management ecosystem.")
    name: Union[str, None] = Field(
        description="The unique package name within its ecosystem."
    )


model_rebuild(RepositoryAdvisory)
model_rebuild(RepositoryAdvisoryPropIdentifiersItems)
model_rebuild(RepositoryAdvisoryPropSubmission)
model_rebuild(RepositoryAdvisoryPropCvss)
model_rebuild(RepositoryAdvisoryPropCwesItems)
model_rebuild(RepositoryAdvisoryPropCreditsItems)
model_rebuild(RepositoryAdvisoryVulnerability)
model_rebuild(RepositoryAdvisoryVulnerabilityPropPackage)

__all__ = (
    "RepositoryAdvisory",
    "RepositoryAdvisoryPropCreditsItems",
    "RepositoryAdvisoryPropCvss",
    "RepositoryAdvisoryPropCwesItems",
    "RepositoryAdvisoryPropIdentifiersItems",
    "RepositoryAdvisoryPropSubmission",
    "RepositoryAdvisoryVulnerability",
    "RepositoryAdvisoryVulnerabilityPropPackage",
)
