"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser


class Milestone(GitHubModel):
    """Milestone

    A collection of related issues and pull requests.
    """

    url: str = Field()
    html_url: str = Field()
    labels_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    state: Literal["open", "closed"] = Field(
        default="open", description="The state of the milestone."
    )
    title: str = Field(description="The title of the milestone.")
    description: Union[str, None] = Field()
    creator: Union[None, SimpleUser] = Field()
    open_issues: int = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    closed_at: Union[datetime, None] = Field()
    due_on: Union[datetime, None] = Field()


model_rebuild(Milestone)

__all__ = ("Milestone",)
