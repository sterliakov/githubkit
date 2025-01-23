"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserCodespacesSecretsSecretNameRepositoriesPutBody(GitHubModel):
    """UserCodespacesSecretsSecretNameRepositoriesPutBody"""

    selected_repository_ids: builtins.list[int] = Field(
        description="An array of repository ids for which a codespace can access the secret. You can manage the list of selected repositories using the [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret), [Add a selected repository to a user secret](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret), and [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret) endpoints."
    )


model_rebuild(UserCodespacesSecretsSecretNameRepositoriesPutBody)

__all__ = ("UserCodespacesSecretsSecretNameRepositoriesPutBody",)
