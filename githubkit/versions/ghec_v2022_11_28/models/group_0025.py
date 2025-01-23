"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0023 import SimpleClassroomRepository


class ClassroomAcceptedAssignment(GitHubModel):
    """Classroom Accepted Assignment

    A GitHub Classroom accepted assignment
    """

    id: int = Field(description="Unique identifier of the repository.")
    submitted: bool = Field(
        description="Whether an accepted assignment has been submitted."
    )
    passing: bool = Field(description="Whether a submission passed.")
    commit_count: int = Field(description="Count of student commits.")
    grade: str = Field(description="Most recent grade.")
    students: builtins.list[SimpleClassroomUser] = Field()
    repository: SimpleClassroomRepository = Field(
        title="Simple Classroom Repository",
        description="A GitHub repository view for Classroom",
    )
    assignment: SimpleClassroomAssignment = Field(
        title="Simple Classroom Assignment", description="A GitHub Classroom assignment"
    )


class SimpleClassroomUser(GitHubModel):
    """Simple Classroom User

    A GitHub user simplified for Classroom.
    """

    id: int = Field()
    login: str = Field()
    avatar_url: str = Field()
    html_url: str = Field()


class SimpleClassroomAssignment(GitHubModel):
    """Simple Classroom Assignment

    A GitHub Classroom assignment
    """

    id: int = Field(description="Unique identifier of the repository.")
    public_repo: bool = Field(
        description="Whether an accepted assignment creates a public repository."
    )
    title: str = Field(description="Assignment title.")
    type: Literal["individual", "group"] = Field(
        description="Whether it's a Group Assignment or Individual Assignment."
    )
    invite_link: str = Field(
        description="The link that a student can use to accept the assignment."
    )
    invitations_enabled: bool = Field(
        description="Whether the invitation link is enabled. Visiting an enabled invitation link will accept the assignment."
    )
    slug: str = Field(description="Sluggified name of the assignment.")
    students_are_repo_admins: bool = Field(
        description="Whether students are admins on created repository on accepted assignment."
    )
    feedback_pull_requests_enabled: bool = Field(
        description="Whether feedback pull request will be created on assignment acceptance."
    )
    max_teams: Missing[Union[int, None]] = Field(
        default=UNSET, description="The maximum allowable teams for the assignment."
    )
    max_members: Missing[Union[int, None]] = Field(
        default=UNSET, description="The maximum allowable members per team."
    )
    editor: Union[str, None] = Field(
        description="The selected editor for the assignment."
    )
    accepted: int = Field(
        description="The number of students that have accepted the assignment."
    )
    submitted: Missing[int] = Field(
        default=UNSET,
        description="The number of students that have submitted the assignment.",
    )
    passing: int = Field(
        description="The number of students that have passed the assignment."
    )
    language: Union[str, None] = Field(
        description="The programming language used in the assignment."
    )
    deadline: Union[datetime, None] = Field(
        description="The time at which the assignment is due."
    )
    classroom: SimpleClassroom = Field(
        title="Simple Classroom", description="A GitHub Classroom classroom"
    )


class SimpleClassroom(GitHubModel):
    """Simple Classroom

    A GitHub Classroom classroom
    """

    id: int = Field(description="Unique identifier of the classroom.")
    name: str = Field(description="The name of the classroom.")
    archived: bool = Field(description="Returns whether classroom is archived or not.")
    url: str = Field(description="The url of the classroom on GitHub Classroom.")


model_rebuild(ClassroomAcceptedAssignment)
model_rebuild(SimpleClassroomUser)
model_rebuild(SimpleClassroomAssignment)
model_rebuild(SimpleClassroom)

__all__ = (
    "ClassroomAcceptedAssignment",
    "SimpleClassroom",
    "SimpleClassroomAssignment",
    "SimpleClassroomUser",
)
