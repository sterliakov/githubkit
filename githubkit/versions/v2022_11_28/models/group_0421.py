"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhooksSecurityAdvisory(GitHubModel):
    """WebhooksSecurityAdvisory

    The details of the security advisory, including summary, description, and
    severity.
    """

    cvss: WebhooksSecurityAdvisoryPropCvss = Field()
    cwes: List[WebhooksSecurityAdvisoryPropCwesItems] = Field()
    description: str = Field()
    ghsa_id: str = Field()
    identifiers: List[WebhooksSecurityAdvisoryPropIdentifiersItems] = Field()
    published_at: str = Field()
    references: List[WebhooksSecurityAdvisoryPropReferencesItems] = Field()
    severity: str = Field()
    summary: str = Field()
    updated_at: str = Field()
    vulnerabilities: List[WebhooksSecurityAdvisoryPropVulnerabilitiesItems] = Field()
    withdrawn_at: Union[str, None] = Field()


class WebhooksSecurityAdvisoryPropCvss(GitHubModel):
    """WebhooksSecurityAdvisoryPropCvss"""

    score: float = Field()
    vector_string: Union[str, None] = Field()


class WebhooksSecurityAdvisoryPropCwesItems(GitHubModel):
    """WebhooksSecurityAdvisoryPropCwesItems"""

    cwe_id: str = Field()
    name: str = Field()


class WebhooksSecurityAdvisoryPropIdentifiersItems(GitHubModel):
    """WebhooksSecurityAdvisoryPropIdentifiersItems"""

    type: str = Field()
    value: str = Field()


class WebhooksSecurityAdvisoryPropReferencesItems(GitHubModel):
    """WebhooksSecurityAdvisoryPropReferencesItems"""

    url: str = Field()


class WebhooksSecurityAdvisoryPropVulnerabilitiesItems(GitHubModel):
    """WebhooksSecurityAdvisoryPropVulnerabilitiesItems"""

    first_patched_version: Union[
        WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion, None
    ] = Field()
    package: WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropPackage = Field()
    severity: str = Field()
    vulnerable_version_range: str = Field()


class WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion(
    GitHubModel
):
    """WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion"""

    identifier: str = Field()


class WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropPackage(GitHubModel):
    """WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropPackage"""

    ecosystem: str = Field()
    name: str = Field()


model_rebuild(WebhooksSecurityAdvisory)
model_rebuild(WebhooksSecurityAdvisoryPropCvss)
model_rebuild(WebhooksSecurityAdvisoryPropCwesItems)
model_rebuild(WebhooksSecurityAdvisoryPropIdentifiersItems)
model_rebuild(WebhooksSecurityAdvisoryPropReferencesItems)
model_rebuild(WebhooksSecurityAdvisoryPropVulnerabilitiesItems)
model_rebuild(WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion)
model_rebuild(WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropPackage)

__all__ = (
    "WebhooksSecurityAdvisory",
    "WebhooksSecurityAdvisoryPropCvss",
    "WebhooksSecurityAdvisoryPropCwesItems",
    "WebhooksSecurityAdvisoryPropIdentifiersItems",
    "WebhooksSecurityAdvisoryPropReferencesItems",
    "WebhooksSecurityAdvisoryPropVulnerabilitiesItems",
    "WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropFirstPatchedVersion",
    "WebhooksSecurityAdvisoryPropVulnerabilitiesItemsPropPackage",
)
