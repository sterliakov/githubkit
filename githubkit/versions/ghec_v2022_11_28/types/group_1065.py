"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Any
from typing_extensions import NotRequired, TypeAlias, TypedDict


class ReposOwnerRepoAttestationsSubjectDigestGetResponse200Type(TypedDict):
    """ReposOwnerRepoAttestationsSubjectDigestGetResponse200"""

    attestations: NotRequired[
        builtins.list[
            ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsType
        ]
    ]


class ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsType(
    TypedDict
):
    """ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItems"""

    bundle: NotRequired[
        ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundleType
    ]
    repository_id: NotRequired[int]
    bundle_url: NotRequired[str]


class ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundleType(
    TypedDict
):
    """ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBu
    ndle

    The attestation's Sigstore Bundle.
    Refer to the [Sigstore Bundle
    Specification](https://github.com/sigstore/protobuf-
    specs/blob/main/protos/sigstore_bundle.proto) for more information.
    """

    media_type: NotRequired[str]
    verification_material: NotRequired[
        ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropVerificationMaterialType
    ]
    dsse_envelope: NotRequired[
        ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropDsseEnvelopeType
    ]


ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropVerificationMaterialType: TypeAlias = dict[
    str, Any
]
"""ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBu
ndlePropVerificationMaterial
"""


ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropDsseEnvelopeType: TypeAlias = dict[
    str, Any
]
"""ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBu
ndlePropDsseEnvelope
"""


__all__ = (
    "ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropDsseEnvelopeType",
    "ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundlePropVerificationMaterialType",
    "ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsPropBundleType",
    "ReposOwnerRepoAttestationsSubjectDigestGetResponse200PropAttestationsItemsType",
    "ReposOwnerRepoAttestationsSubjectDigestGetResponse200Type",
)
