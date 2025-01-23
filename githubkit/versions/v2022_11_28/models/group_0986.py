"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Literal

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput(GitHubModel):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput

    Check runs can accept a variety of data in the `output` object, including a
    `title` and `summary` and can optionally provide descriptive details about the
    run.
    """

    title: Missing[str] = Field(default=UNSET, description="**Required**.")
    summary: str = Field(max_length=65535, description="Can contain Markdown.")
    text: Missing[str] = Field(
        max_length=65535, default=UNSET, description="Can contain Markdown."
    )
    annotations: Missing[
        builtins.list[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems
        ]
    ] = Field(
        max_length=50 if PYDANTIC_V2 else None,
        default=UNSET,
        description="Adds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/rest/checks/runs#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see \"[About status checks](https://docs.github.com/articles/about-status-checks#checks)\".",
    )
    images: Missing[
        builtins.list[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems
        ]
    ] = Field(
        default=UNSET,
        description="Adds images to the output displayed in the GitHub pull request UI.",
    )


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems(
    GitHubModel
):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems"""

    path: str = Field(
        description="The path of the file to add an annotation to. For example, `assets/css/main.css`."
    )
    start_line: int = Field(
        description="The start line of the annotation. Line numbers start at 1."
    )
    end_line: int = Field(description="The end line of the annotation.")
    start_column: Missing[int] = Field(
        default=UNSET,
        description="The start column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values. Column numbers start at 1.",
    )
    end_column: Missing[int] = Field(
        default=UNSET,
        description="The end column of the annotation. Annotations only support `start_column` and `end_column` on the same line. Omit this parameter if `start_line` and `end_line` have different values.",
    )
    annotation_level: Literal["notice", "warning", "failure"] = Field(
        description="The level of the annotation."
    )
    message: str = Field(
        description="A short description of the feedback for these lines of code. The maximum size is 64 KB."
    )
    title: Missing[str] = Field(
        default=UNSET,
        description="The title that represents the annotation. The maximum size is 255 characters.",
    )
    raw_details: Missing[str] = Field(
        default=UNSET,
        description="Details about this annotation. The maximum size is 64 KB.",
    )


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems(GitHubModel):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems"""

    alt: str = Field(description="The alternative text for the image.")
    image_url: str = Field(description="The full URL of the image.")
    caption: Missing[str] = Field(
        default=UNSET, description="A short image description."
    )


class ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems(GitHubModel):
    """ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems"""

    label: str = Field(
        max_length=20,
        description="The text to be displayed on a button in the web UI. The maximum size is 20 characters.",
    )
    description: str = Field(
        max_length=40,
        description="A short explanation of what this action would do. The maximum size is 40 characters.",
    )
    identifier: str = Field(
        max_length=20,
        description="A reference for the action on the integrator's system. The maximum size is 20 characters.",
    )


model_rebuild(ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput)
model_rebuild(ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems)
model_rebuild(ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems)
model_rebuild(ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems)

__all__ = (
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItems",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutput",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropAnnotationsItems",
    "ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputPropImagesItems",
)
