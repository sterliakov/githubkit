"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class FileCommit(GitHubModel):
    """File Commit

    File Commit
    """

    content: Union[FileCommitPropContent, None] = Field()
    commit: FileCommitPropCommit = Field()


class FileCommitPropContent(GitHubModel):
    """FileCommitPropContent"""

    name: Missing[str] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)
    size: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    git_url: Missing[str] = Field(default=UNSET)
    download_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    links: Missing[FileCommitPropContentPropLinks] = Field(
        default=UNSET, alias="_links"
    )


class FileCommitPropContentPropLinks(GitHubModel):
    """FileCommitPropContentPropLinks"""

    self_: Missing[str] = Field(default=UNSET, alias="self")
    git: Missing[str] = Field(default=UNSET)
    html: Missing[str] = Field(default=UNSET)


class FileCommitPropCommit(GitHubModel):
    """FileCommitPropCommit"""

    sha: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    author: Missing[FileCommitPropCommitPropAuthor] = Field(default=UNSET)
    committer: Missing[FileCommitPropCommitPropCommitter] = Field(default=UNSET)
    message: Missing[str] = Field(default=UNSET)
    tree: Missing[FileCommitPropCommitPropTree] = Field(default=UNSET)
    parents: Missing[builtins.list[FileCommitPropCommitPropParentsItems]] = Field(
        default=UNSET
    )
    verification: Missing[FileCommitPropCommitPropVerification] = Field(default=UNSET)


class FileCommitPropCommitPropAuthor(GitHubModel):
    """FileCommitPropCommitPropAuthor"""

    date: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    email: Missing[str] = Field(default=UNSET)


class FileCommitPropCommitPropCommitter(GitHubModel):
    """FileCommitPropCommitPropCommitter"""

    date: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    email: Missing[str] = Field(default=UNSET)


class FileCommitPropCommitPropTree(GitHubModel):
    """FileCommitPropCommitPropTree"""

    url: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)


class FileCommitPropCommitPropParentsItems(GitHubModel):
    """FileCommitPropCommitPropParentsItems"""

    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    sha: Missing[str] = Field(default=UNSET)


class FileCommitPropCommitPropVerification(GitHubModel):
    """FileCommitPropCommitPropVerification"""

    verified: Missing[bool] = Field(default=UNSET)
    reason: Missing[str] = Field(default=UNSET)
    signature: Missing[Union[str, None]] = Field(default=UNSET)
    payload: Missing[Union[str, None]] = Field(default=UNSET)
    verified_at: Missing[Union[str, None]] = Field(default=UNSET)


model_rebuild(FileCommit)
model_rebuild(FileCommitPropContent)
model_rebuild(FileCommitPropContentPropLinks)
model_rebuild(FileCommitPropCommit)
model_rebuild(FileCommitPropCommitPropAuthor)
model_rebuild(FileCommitPropCommitPropCommitter)
model_rebuild(FileCommitPropCommitPropTree)
model_rebuild(FileCommitPropCommitPropParentsItems)
model_rebuild(FileCommitPropCommitPropVerification)

__all__ = (
    "FileCommit",
    "FileCommitPropCommit",
    "FileCommitPropCommitPropAuthor",
    "FileCommitPropCommitPropCommitter",
    "FileCommitPropCommitPropParentsItems",
    "FileCommitPropCommitPropTree",
    "FileCommitPropCommitPropVerification",
    "FileCommitPropContent",
    "FileCommitPropContentPropLinks",
)
