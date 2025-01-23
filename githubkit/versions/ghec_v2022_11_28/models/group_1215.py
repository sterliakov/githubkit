"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoTopicsPutBody(GitHubModel):
    """ReposOwnerRepoTopicsPutBody"""

    names: builtins.list[str] = Field(
        description="An array of topics to add to the repository. Pass one or more topics to _replace_ the set of existing topics. Send an empty array (`[]`) to clear all topics from the repository. **Note:** Topic `names` will be saved as lowercase."
    )


model_rebuild(ReposOwnerRepoTopicsPutBody)

__all__ = ("ReposOwnerRepoTopicsPutBody",)
