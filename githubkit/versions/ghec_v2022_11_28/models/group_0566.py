"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0561 import (
    WebhookIssueCommentDeletedPropIssueAllof0PropMilestonePropCreator,
)


class WebhookIssueCommentDeletedPropIssueMergedMilestone(GitHubModel):
    """WebhookIssueCommentDeletedPropIssueMergedMilestone"""

    closed_at: Union[datetime, None] = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    creator: Union[
        WebhookIssueCommentDeletedPropIssueAllof0PropMilestonePropCreator, None
    ] = Field(title="User")
    description: Union[str, None] = Field()
    due_on: Union[datetime, None] = Field()
    html_url: str = Field()
    id: int = Field()
    labels_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    open_issues: int = Field()
    state: Literal["open", "closed"] = Field(description="The state of the milestone.")
    title: str = Field(description="The title of the milestone.")
    updated_at: datetime = Field()
    url: str = Field()


model_rebuild(WebhookIssueCommentDeletedPropIssueMergedMilestone)

__all__ = ("WebhookIssueCommentDeletedPropIssueMergedMilestone",)
