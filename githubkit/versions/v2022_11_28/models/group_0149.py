"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0150 import RepositoryRuleWorkflowsPropParameters


class RepositoryRuleWorkflows(GitHubModel):
    """workflows

    Require all changes made to a targeted branch to pass the specified workflows
    before they can be merged.
    """

    type: Literal["workflows"] = Field()
    parameters: Missing[RepositoryRuleWorkflowsPropParameters] = Field(default=UNSET)


model_rebuild(RepositoryRuleWorkflows)

__all__ = ("RepositoryRuleWorkflows",)
