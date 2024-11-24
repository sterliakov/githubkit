"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing

from .group_0002 import SimpleUser
from .group_0008 import Integration


class MovedColumnInProjectIssueEvent(GitHubModel):
    """Moved Column in Project Issue Event

    Moved Column in Project Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["moved_columns_in_project"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration, None] = Field()
    project_card: Missing[MovedColumnInProjectIssueEventPropProjectCard] = Field(
        default=UNSET
    )


class MovedColumnInProjectIssueEventPropProjectCard(GitHubModel):
    """MovedColumnInProjectIssueEventPropProjectCard"""

    id: int = Field()
    url: str = Field()
    project_id: int = Field()
    project_url: str = Field()
    column_name: str = Field()
    previous_column_name: Missing[str] = Field(default=UNSET)


model_rebuild(MovedColumnInProjectIssueEvent)
model_rebuild(MovedColumnInProjectIssueEventPropProjectCard)

__all__ = (
    "MovedColumnInProjectIssueEvent",
    "MovedColumnInProjectIssueEventPropProjectCard",
)
