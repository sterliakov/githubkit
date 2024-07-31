"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0387 import DiscussionType
from .group_0386 import WebhooksAnswerType
from .group_0376 import RepositoryWebhooksType
from .group_0377 import SimpleUserWebhooksType
from .group_0375 import OrganizationSimpleWebhooksType


class WebhookDiscussionUnansweredType(TypedDict):
    """discussion unanswered event"""

    action: Literal["unanswered"]
    discussion: DiscussionType
    old_answer: WebhooksAnswerType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookDiscussionUnansweredType",)
