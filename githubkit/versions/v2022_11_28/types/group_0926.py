"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType(TypedDict):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput

    Check runs can accept a variety of data in the `output` object, including a
    `title` and `summary` and can optionally provide descriptive details about the
    run.
    """

    title: NotRequired[str]
    summary: str
    text: NotRequired[str]
    annotations: NotRequired[
        List[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItemsType
        ]
    ]
    images: NotRequired[
        List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItemsType]
    ]


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItemsType(
    TypedDict
):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems"""

    path: str
    start_line: int
    end_line: int
    start_column: NotRequired[int]
    end_column: NotRequired[int]
    annotation_level: Literal["notice", "warning", "failure"]
    message: str
    title: NotRequired[str]
    raw_details: NotRequired[str]


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItemsType(
    TypedDict
):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems"""

    alt: str
    image_url: str
    caption: NotRequired[str]


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType(TypedDict):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems"""

    label: str
    description: str
    identifier: str


__all__ = (
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItemsType",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItemsType",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType",
)
