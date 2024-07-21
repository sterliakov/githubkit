"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Label(GitHubModel):
    """Label

    Color-coded labels help you categorize and filter your issues (just like labels
    in Gmail).
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field(description="URL for the label")
    name: str = Field(description="The name of the label.")
    description: Union[str, None] = Field()
    color: str = Field(
        description="6-character hex code, without the leading #, identifying the color"
    )
    default: bool = Field()


model_rebuild(Label)

__all__ = ("Label",)
