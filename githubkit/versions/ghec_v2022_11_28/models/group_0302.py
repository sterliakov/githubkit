"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0068 import DependabotAlertPackage


class DependabotAlertPropDependency(GitHubModel):
    """DependabotAlertPropDependency

    Details for the vulnerable dependency.
    """

    package: Missing[DependabotAlertPackage] = Field(
        default=UNSET, description="Details for the vulnerable package."
    )
    manifest_path: Missing[str] = Field(
        default=UNSET,
        description="The full path to the dependency manifest file, relative to the root of the repository.",
    )
    scope: Missing[Union[None, Literal["development", "runtime"]]] = Field(
        default=UNSET, description="The execution scope of the vulnerable dependency."
    )


model_rebuild(DependabotAlertPropDependency)

__all__ = ("DependabotAlertPropDependency",)
