"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class Feed(GitHubModel):
    """Feed

    Feed
    """

    timeline_url: str = Field()
    user_url: str = Field()
    current_user_public_url: Missing[str] = Field(default=UNSET)
    current_user_url: Missing[str] = Field(default=UNSET)
    current_user_actor_url: Missing[str] = Field(default=UNSET)
    current_user_organization_url: Missing[str] = Field(default=UNSET)
    current_user_organization_urls: Missing[builtins.list[str]] = Field(default=UNSET)
    security_advisories_url: Missing[str] = Field(default=UNSET)
    repository_discussions_url: Missing[str] = Field(
        default=UNSET, description="A feed of discussions for a given repository."
    )
    repository_discussions_category_url: Missing[str] = Field(
        default=UNSET,
        description="A feed of discussions for a given repository and category.",
    )
    links: FeedPropLinks = Field(alias="_links")


class FeedPropLinks(GitHubModel):
    """FeedPropLinks"""

    timeline: LinkWithType = Field(
        title="Link With Type", description="Hypermedia Link with Type"
    )
    user: LinkWithType = Field(
        title="Link With Type", description="Hypermedia Link with Type"
    )
    security_advisories: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    current_user: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    current_user_public: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    current_user_actor: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    current_user_organization: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    current_user_organizations: Missing[builtins.list[LinkWithType]] = Field(
        default=UNSET
    )
    repository_discussions: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )
    repository_discussions_category: Missing[LinkWithType] = Field(
        default=UNSET, title="Link With Type", description="Hypermedia Link with Type"
    )


class LinkWithType(GitHubModel):
    """Link With Type

    Hypermedia Link with Type
    """

    href: str = Field()
    type: str = Field()


model_rebuild(Feed)
model_rebuild(FeedPropLinks)
model_rebuild(LinkWithType)

__all__ = (
    "Feed",
    "FeedPropLinks",
    "LinkWithType",
)
