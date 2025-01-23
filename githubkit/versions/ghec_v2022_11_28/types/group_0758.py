"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Any, Union
from typing_extensions import NotRequired, TypeAlias, TypedDict

from .group_0677 import WebhookRubygemsMetadataType


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion"""

    author: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthorType
    ]
    body: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1Type,
        ]
    ]
    body_html: NotRequired[str]
    container_metadata: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataType
    ]
    created_at: NotRequired[str]
    description: str
    docker_metadata: NotRequired[
        builtins.list[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType
        ]
    ]
    draft: NotRequired[bool]
    html_url: str
    id: int
    installation_command: str
    manifest: NotRequired[str]
    metadata: builtins.list[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItemsType
    ]
    name: str
    npm_metadata: NotRequired[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataType,
            None,
        ]
    ]
    nuget_metadata: NotRequired[
        Union[
            builtins.list[
                WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsType
            ],
            None,
        ]
    ]
    package_files: builtins.list[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType
    ]
    package_url: str
    prerelease: NotRequired[bool]
    release: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleaseType
    ]
    rubygems_metadata: NotRequired[builtins.list[WebhookRubygemsMetadataType]]
    summary: str
    tag_name: NotRequired[str]
    target_commitish: NotRequired[str]
    target_oid: NotRequired[str]
    updated_at: NotRequired[str]
    version: str


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthorType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthor"""

    avatar_url: str
    events_url: str
    followers_url: str
    following_url: str
    gists_url: str
    gravatar_id: str
    html_url: str
    id: int
    login: str
    node_id: str
    organizations_url: str
    received_events_url: str
    repos_url: str
    site_admin: bool
    starred_url: str
    subscriptions_url: str
    type: str
    url: str
    user_view_type: NotRequired[str]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneo
    f1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMe
    tadataItems
    """

    tags: NotRequired[builtins.list[str]]


WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItemsType: TypeAlias = dict[
    str, Any
]
"""WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadata
Items
"""


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ata
    """

    name: NotRequired[str]
    version: NotRequired[str]
    npm_user: NotRequired[str]
    author: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1Type,
            None,
        ]
    ]
    bugs: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1Type,
            None,
        ]
    ]
    dependencies: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependenciesType
    ]
    dev_dependencies: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType
    ]
    peer_dependencies: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType
    ]
    optional_dependencies: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType
    ]
    description: NotRequired[str]
    dist: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1Type,
            None,
        ]
    ]
    git_head: NotRequired[str]
    homepage: NotRequired[str]
    license_: NotRequired[str]
    main: NotRequired[str]
    repository: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1Type,
            None,
        ]
    ]
    scripts: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScriptsType
    ]
    id: NotRequired[str]
    node_version: NotRequired[str]
    npm_version: NotRequired[str]
    has_shrinkwrap: NotRequired[bool]
    maintainers: NotRequired[builtins.list[str]]
    contributors: NotRequired[builtins.list[str]]
    engines: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEnginesType
    ]
    keywords: NotRequired[builtins.list[str]]
    files: NotRequired[builtins.list[str]]
    bin_: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBinType
    ]
    man: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropManType
    ]
    directories: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1Type,
            None,
        ]
    ]
    os: NotRequired[builtins.list[str]]
    cpu: NotRequired[builtins.list[str]]
    readme: NotRequired[str]
    installation_command: NotRequired[str]
    release_id: NotRequired[int]
    commit_oid: NotRequired[str]
    published_via_actions: NotRequired[bool]
    deleted_by_id: NotRequired[int]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropAuthorOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropBugsOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependenciesType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDevDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropPeerDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropOptionalDependencies
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDistOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropRepositoryOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScriptsType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropScripts
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEnginesType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropEngines
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBinType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropBin
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropManType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropMan
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetad
    ataPropDirectoriesOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageF
    ilesItems
    """

    content_type: str
    created_at: str
    download_url: str
    id: int
    md5: Union[str, None]
    name: str
    sha1: Union[str, None]
    sha256: Union[str, None]
    size: int
    state: Union[str, None]
    updated_at: str


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadata
    """

    labels: NotRequired[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabelsType,
            None,
        ]
    ]
    manifest: NotRequired[
        Union[
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifestType,
            None,
        ]
    ]
    tag: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTagType
    ]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabelsType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropLabels
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifestType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropManifest
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTagType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContaine
    rMetadataPropTag
    """

    digest: NotRequired[str]
    name: NotRequired[str]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItems
    """

    id: NotRequired[
        Union[
            str,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1Type,
            int,
            None,
        ]
    ]
    name: NotRequired[str]
    value: NotRequired[
        Union[
            bool,
            str,
            int,
            WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type,
        ]
    ]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItemsPropIdOneof1
    """


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMet
    adataItemsPropValueOneof3
    """

    url: NotRequired[str]
    branch: NotRequired[str]
    commit: NotRequired[str]
    type: NotRequired[str]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleaseType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropRelease"""

    author: NotRequired[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType
    ]
    created_at: NotRequired[str]
    draft: NotRequired[bool]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[Union[str, None]]
    prerelease: NotRequired[bool]
    published_at: NotRequired[str]
    tag_name: NotRequired[str]
    target_commitish: NotRequired[str]
    url: NotRequired[str]


class WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType(
    TypedDict
):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleaseP
    ropAuthor
    """

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropAuthorType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropBodyOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropLabelsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropManifestType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataPropTagType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropContainerMetadataType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropDockerMetadataItemsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropMetadataItemsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropAuthorOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBinType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropBugsOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDependenciesType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDirectoriesOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropDistOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropEnginesType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropManType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropRepositoryOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataPropScriptsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNpmMetadataType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropIdOneof1Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropNugetMetadataItemsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropPackageFilesItemsType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleasePropAuthorType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionPropReleaseType",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersionType",
)
