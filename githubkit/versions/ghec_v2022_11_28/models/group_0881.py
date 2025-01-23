"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0048 import (
    AmazonS3AccessKeysConfig,
    AzureBlobConfig,
    AzureHubConfig,
    GoogleCloudConfig,
)
from .group_0049 import AmazonS3OidcConfig, SplunkConfig
from .group_0050 import DatadogConfig


class EnterprisesEnterpriseAuditLogStreamsStreamIdPutBody(GitHubModel):
    """EnterprisesEnterpriseAuditLogStreamsStreamIdPutBody"""

    enabled: bool = Field(description="This setting pauses or resumes a stream.")
    stream_type: Literal[
        "Azure Blob Storage",
        "Azure Event Hubs",
        "Amazon S3",
        "Splunk",
        "HTTPS Event Collector",
        "Google Cloud Storage",
        "Datadog",
    ] = Field(
        description="The audit log streaming provider. The name is case sensitive."
    )
    vendor_specific: Union[
        AzureBlobConfig,
        AzureHubConfig,
        AmazonS3OidcConfig,
        AmazonS3AccessKeysConfig,
        SplunkConfig,
        GoogleCloudConfig,
        DatadogConfig,
    ] = Field()


model_rebuild(EnterprisesEnterpriseAuditLogStreamsStreamIdPutBody)

__all__ = ("EnterprisesEnterpriseAuditLogStreamsStreamIdPutBody",)
