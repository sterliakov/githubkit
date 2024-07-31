"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0591 import WebhookRubygemsMetadataType


class WebhookPackagePublishedPropPackagePropPackageVersionType(TypedDict):
    """WebhookPackagePublishedPropPackagePropPackageVersion"""

    author: NotRequired[
        Union[WebhookPackagePublishedPropPackagePropPackageVersionPropAuthorType, None]
    ]
    body: NotRequired[
        Union[
            str, WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1Type
        ]
    ]
    body_html: NotRequired[str]
    container_metadata: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataType,
            None,
        ]
    ]
    created_at: NotRequired[str]
    description: str
    docker_metadata: NotRequired[
        List[
            WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItemsType
        ]
    ]
    draft: NotRequired[bool]
    html_url: str
    id: int
    installation_command: str
    manifest: NotRequired[str]
    metadata: List[
        WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItemsType
    ]
    name: str
    npm_metadata: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataType,
            None,
        ]
    ]
    nuget_metadata: NotRequired[
        Union[
            List[
                WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsType
            ],
            None,
        ]
    ]
    package_files: List[
        WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItemsType
    ]
    package_url: NotRequired[str]
    prerelease: NotRequired[bool]
    release: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropReleaseType
    ]
    rubygems_metadata: NotRequired[List[WebhookRubygemsMetadataType]]
    source_url: NotRequired[str]
    summary: str
    tag_name: NotRequired[str]
    target_commitish: NotRequired[str]
    target_oid: NotRequired[str]
    updated_at: NotRequired[str]
    version: str


class WebhookPackagePublishedPropPackagePropPackageVersionPropAuthorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1Type(TypedDict):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadata"""

    labels: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabelsType,
            None,
        ]
    ]
    manifest: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifestType,
            None,
        ]
    ]
    tag: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTagType
    ]


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabelsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLab
    els
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifestType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropMan
    ifest
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTagType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTag"""

    digest: NotRequired[str]
    name: NotRequired[str]


class WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItems"""

    tags: NotRequired[List[str]]


class WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItems"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadata"""

    name: NotRequired[str]
    version: NotRequired[str]
    npm_user: NotRequired[str]
    author: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthorType,
            None,
        ]
    ]
    bugs: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugsType,
            None,
        ]
    ]
    dependencies: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependenciesType
    ]
    dev_dependencies: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType
    ]
    peer_dependencies: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType
    ]
    optional_dependencies: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType
    ]
    description: NotRequired[str]
    dist: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDistType,
            None,
        ]
    ]
    git_head: NotRequired[str]
    homepage: NotRequired[str]
    license_: NotRequired[str]
    main: NotRequired[str]
    repository: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepositoryType,
            None,
        ]
    ]
    scripts: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScriptsType
    ]
    id: NotRequired[str]
    node_version: NotRequired[str]
    npm_version: NotRequired[str]
    has_shrinkwrap: NotRequired[bool]
    maintainers: NotRequired[
        List[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItemsType
        ]
    ]
    contributors: NotRequired[
        List[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItemsType
        ]
    ]
    engines: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEnginesType
    ]
    keywords: NotRequired[List[str]]
    files: NotRequired[List[str]]
    bin_: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBinType
    ]
    man: NotRequired[
        WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropManType
    ]
    directories: NotRequired[
        Union[
            WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectoriesType,
            None,
        ]
    ]
    os: NotRequired[List[str]]
    cpu: NotRequired[List[str]]
    readme: NotRequired[str]
    installation_command: NotRequired[str]
    release_id: NotRequired[int]
    commit_oid: NotRequired[str]
    published_via_actions: NotRequired[bool]
    deleted_by_id: NotRequired[int]


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthorType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthor"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugs"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependenciesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependenc
    ies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDepend
    encies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDepen
    dencies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalD
    ependencies
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDistType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDist"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepositoryType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepositor
    y
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScriptsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScripts"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintaine
    rsItems
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContribut
    orsItems
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEnginesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEngines"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBinType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBin"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropManType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMan"""


class WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectoriesType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectori
    es
    """


class WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItems"""

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


class WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsType(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItems"""

    id: NotRequired[Union[int, str]]
    name: NotRequired[str]
    value: NotRequired[
        Union[
            bool,
            str,
            int,
            WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type,
        ]
    ]


class WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type(
    TypedDict
):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropVa
    lueOneof3
    """

    url: NotRequired[str]
    branch: NotRequired[str]
    commit: NotRequired[str]
    type: NotRequired[str]


class WebhookPackagePublishedPropPackagePropPackageVersionPropReleaseType(TypedDict):
    """WebhookPackagePublishedPropPackagePropPackageVersionPropRelease"""

    author: Union[
        WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthorType,
        None,
    ]
    created_at: str
    draft: bool
    html_url: str
    id: int
    name: Union[str, None]
    prerelease: bool
    published_at: str
    tag_name: str
    target_commitish: str
    url: str


class WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthorType(
    TypedDict
):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookPackagePublishedPropPackagePropPackageVersionType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropAuthorType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropBodyOneof1Type",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropLabelsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropManifestType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropContainerMetadataPropTagType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropDockerMetadataItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropMetadataItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropAuthorType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBugsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDependenciesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDevDependenciesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropPeerDependenciesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropOptionalDependenciesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDistType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropRepositoryType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropScriptsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropMaintainersItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropContributorsItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropEnginesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropBinType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropManType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNpmMetadataPropDirectoriesType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropPackageFilesItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropNugetMetadataItemsPropValueOneof3Type",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropReleaseType",
    "WebhookPackagePublishedPropPackagePropPackageVersionPropReleasePropAuthorType",
)
