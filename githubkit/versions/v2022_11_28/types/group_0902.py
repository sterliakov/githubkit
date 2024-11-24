"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPatchBodyType(TypedDict):
    """ReposOwnerRepoPatchBody"""

    name: NotRequired[str]
    description: NotRequired[str]
    homepage: NotRequired[str]
    private: NotRequired[bool]
    visibility: NotRequired[Literal["public", "private"]]
    security_and_analysis: NotRequired[
        Union[ReposOwnerRepoPatchBodyPropSecurityAndAnalysisType, None]
    ]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    is_template: NotRequired[bool]
    default_branch: NotRequired[str]
    allow_squash_merge: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    archived: NotRequired[bool]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisType(TypedDict):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysis

    Specify which security and analysis features to enable or disable for the
    repository.

    To use this parameter, you must have admin permissions for the repository or be
    an owner or security manager for the organization that owns the repository. For
    more information, see "[Managing security managers in your
    organization](https://docs.github.com/organizations/managing-peoples-access-to-
    your-organization-with-roles/managing-security-managers-in-your-organization)."

    For example, to enable GitHub Advanced Security, use this data in the body of
    the `PATCH` request:
    `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

    You can check which security and analysis features are currently enabled by
    using a `GET /repos/{owner}/{repo}` request.
    """

    advanced_security: NotRequired[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurityType
    ]
    secret_scanning: NotRequired[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningType
    ]
    secret_scanning_push_protection: NotRequired[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtectionType
    ]
    secret_scanning_ai_detection: NotRequired[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningAiDetectionType
    ]
    secret_scanning_non_provider_patterns: NotRequired[
        ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningNonProviderPatternsType
    ]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurityType(TypedDict):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurity

    Use the `status` property to enable or disable GitHub Advanced Security for this
    repository. For more information, see "[About GitHub Advanced
    Security](/github/getting-started-with-github/learning-about-github/about-
    github-advanced-security)."
    """

    status: NotRequired[str]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningType(TypedDict):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanning

    Use the `status` property to enable or disable secret scanning for this
    repository. For more information, see "[About secret scanning](/code-
    security/secret-security/about-secret-scanning)."
    """

    status: NotRequired[str]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtectionType(
    TypedDict
):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtection

    Use the `status` property to enable or disable secret scanning push protection
    for this repository. For more information, see "[Protecting pushes with secret
    scanning](/code-security/secret-scanning/protecting-pushes-with-secret-
    scanning)."
    """

    status: NotRequired[str]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningAiDetectionType(
    TypedDict
):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningAiDetection

    Use the `status` property to enable or disable secret scanning AI detection for
    this repository. For more information, see "[Responsible detection of generic
    secrets with AI](https://docs.github.com/code-security/secret-scanning/using-
    advanced-secret-scanning-and-push-protection-features/generic-secret-
    detection/responsible-ai-generic-secrets)."
    """

    status: NotRequired[str]


class ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningNonProviderPatternsType(
    TypedDict
):
    """ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningNonProviderPatte
    rns

    Use the `status` property to enable or disable secret scanning non-provider
    patterns for this repository. For more information, see "[Supported secret
    scanning patterns](/code-security/secret-scanning/introduction/supported-secret-
    scanning-patterns#supported-secrets)."
    """

    status: NotRequired[str]


__all__ = (
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropAdvancedSecurityType",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningAiDetectionType",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningNonProviderPatternsType",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningPushProtectionType",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisPropSecretScanningType",
    "ReposOwnerRepoPatchBodyPropSecurityAndAnalysisType",
    "ReposOwnerRepoPatchBodyType",
)
