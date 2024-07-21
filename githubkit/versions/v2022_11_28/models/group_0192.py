"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0183 import BranchRestrictionPolicy
from .group_0193 import ProtectedBranchPropRequiredPullRequestReviews


class ProtectedBranch(GitHubModel):
    """Protected Branch

    Branch protections protect branches
    """

    url: str = Field()
    required_status_checks: Missing[StatusCheckPolicy] = Field(
        default=UNSET, title="Status Check Policy", description="Status Check Policy"
    )
    required_pull_request_reviews: Missing[
        ProtectedBranchPropRequiredPullRequestReviews
    ] = Field(default=UNSET)
    required_signatures: Missing[ProtectedBranchPropRequiredSignatures] = Field(
        default=UNSET
    )
    enforce_admins: Missing[ProtectedBranchPropEnforceAdmins] = Field(default=UNSET)
    required_linear_history: Missing[ProtectedBranchPropRequiredLinearHistory] = Field(
        default=UNSET
    )
    allow_force_pushes: Missing[ProtectedBranchPropAllowForcePushes] = Field(
        default=UNSET
    )
    allow_deletions: Missing[ProtectedBranchPropAllowDeletions] = Field(default=UNSET)
    restrictions: Missing[BranchRestrictionPolicy] = Field(
        default=UNSET,
        title="Branch Restriction Policy",
        description="Branch Restriction Policy",
    )
    required_conversation_resolution: Missing[
        ProtectedBranchPropRequiredConversationResolution
    ] = Field(default=UNSET)
    block_creations: Missing[ProtectedBranchPropBlockCreations] = Field(default=UNSET)
    lock_branch: Missing[ProtectedBranchPropLockBranch] = Field(
        default=UNSET,
        description="Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.",
    )
    allow_fork_syncing: Missing[ProtectedBranchPropAllowForkSyncing] = Field(
        default=UNSET,
        description="Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.",
    )


class ProtectedBranchPropRequiredSignatures(GitHubModel):
    """ProtectedBranchPropRequiredSignatures"""

    url: str = Field()
    enabled: bool = Field()


class ProtectedBranchPropEnforceAdmins(GitHubModel):
    """ProtectedBranchPropEnforceAdmins"""

    url: str = Field()
    enabled: bool = Field()


class ProtectedBranchPropRequiredLinearHistory(GitHubModel):
    """ProtectedBranchPropRequiredLinearHistory"""

    enabled: bool = Field()


class ProtectedBranchPropAllowForcePushes(GitHubModel):
    """ProtectedBranchPropAllowForcePushes"""

    enabled: bool = Field()


class ProtectedBranchPropAllowDeletions(GitHubModel):
    """ProtectedBranchPropAllowDeletions"""

    enabled: bool = Field()


class ProtectedBranchPropRequiredConversationResolution(GitHubModel):
    """ProtectedBranchPropRequiredConversationResolution"""

    enabled: Missing[bool] = Field(default=UNSET)


class ProtectedBranchPropBlockCreations(GitHubModel):
    """ProtectedBranchPropBlockCreations"""

    enabled: bool = Field()


class ProtectedBranchPropLockBranch(GitHubModel):
    """ProtectedBranchPropLockBranch

    Whether to set the branch as read-only. If this is true, users will not be able
    to push to the branch.
    """

    enabled: Missing[bool] = Field(default=UNSET)


class ProtectedBranchPropAllowForkSyncing(GitHubModel):
    """ProtectedBranchPropAllowForkSyncing

    Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    enabled: Missing[bool] = Field(default=UNSET)


class StatusCheckPolicy(GitHubModel):
    """Status Check Policy

    Status Check Policy
    """

    url: str = Field()
    strict: bool = Field()
    contexts: List[str] = Field()
    checks: List[StatusCheckPolicyPropChecksItems] = Field()
    contexts_url: str = Field()


class StatusCheckPolicyPropChecksItems(GitHubModel):
    """StatusCheckPolicyPropChecksItems"""

    context: str = Field()
    app_id: Union[int, None] = Field()


model_rebuild(ProtectedBranch)
model_rebuild(ProtectedBranchPropRequiredSignatures)
model_rebuild(ProtectedBranchPropEnforceAdmins)
model_rebuild(ProtectedBranchPropRequiredLinearHistory)
model_rebuild(ProtectedBranchPropAllowForcePushes)
model_rebuild(ProtectedBranchPropAllowDeletions)
model_rebuild(ProtectedBranchPropRequiredConversationResolution)
model_rebuild(ProtectedBranchPropBlockCreations)
model_rebuild(ProtectedBranchPropLockBranch)
model_rebuild(ProtectedBranchPropAllowForkSyncing)
model_rebuild(StatusCheckPolicy)
model_rebuild(StatusCheckPolicyPropChecksItems)

__all__ = (
    "ProtectedBranch",
    "ProtectedBranchPropRequiredSignatures",
    "ProtectedBranchPropEnforceAdmins",
    "ProtectedBranchPropRequiredLinearHistory",
    "ProtectedBranchPropAllowForcePushes",
    "ProtectedBranchPropAllowDeletions",
    "ProtectedBranchPropRequiredConversationResolution",
    "ProtectedBranchPropBlockCreations",
    "ProtectedBranchPropLockBranch",
    "ProtectedBranchPropAllowForkSyncing",
    "StatusCheckPolicy",
    "StatusCheckPolicyPropChecksItems",
)
