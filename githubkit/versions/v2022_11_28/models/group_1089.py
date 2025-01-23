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


class ReposOwnerRepoPullsPullNumberCommentsPostBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberCommentsPostBody"""

    body: str = Field(description="The text of the review comment.")
    commit_id: str = Field(
        description="The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as the `position`."
    )
    path: str = Field(
        description="The relative path to the file that necessitates a comment."
    )
    position: Missing[int] = Field(
        default=UNSET,
        description='**This parameter is closing down. Use `line` instead**. The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.',
    )
    side: Missing[Literal["LEFT", "RIGHT"]] = Field(
        default=UNSET,
        description='In a split diff view, the side of the diff that the pull request\'s changes appear on. Can be `LEFT` or `RIGHT`. Use `LEFT` for deletions that appear in red. Use `RIGHT` for additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see "[Diff view options](https://docs.github.com/articles/about-comparing-branches-in-pull-requests#diff-view-options)" in the GitHub Help documentation.',
    )
    line: Missing[int] = Field(
        default=UNSET,
        description="**Required unless using `subject_type:file`**. The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to.",
    )
    start_line: Missing[int] = Field(
        default=UNSET,
        description='**Required when using multi-line comments unless using `in_reply_to`**. The `start_line` is the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)" in the GitHub Help documentation.',
    )
    start_side: Missing[Literal["LEFT", "RIGHT", "side"]] = Field(
        default=UNSET,
        description='**Required when using multi-line comments unless using `in_reply_to`**. The `start_side` is the starting side of the diff that the comment applies to. Can be `LEFT` or `RIGHT`. To learn more about multi-line comments, see "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)" in the GitHub Help documentation. See `side` in this table for additional context.',
    )
    in_reply_to: Missing[int] = Field(
        default=UNSET,
        description='The ID of the review comment to reply to. To find the ID of a review comment with ["List review comments on a pull request"](#list-review-comments-on-a-pull-request). When specified, all parameters other than `body` in the request body are ignored.',
    )
    subject_type: Missing[Literal["line", "file"]] = Field(
        default=UNSET, description="The level at which the comment is targeted."
    )


model_rebuild(ReposOwnerRepoPullsPullNumberCommentsPostBody)

__all__ = ("ReposOwnerRepoPullsPullNumberCommentsPostBody",)
