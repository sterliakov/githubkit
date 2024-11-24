"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import TYPE_CHECKING
from weakref import ref
from functools import cached_property

if TYPE_CHECKING:
    from githubkit import GitHubCore

    from .git import GitClient
    from .apps import AppsClient
    from .meta import MetaClient
    from .oidc import OidcClient
    from .orgs import OrgsClient
    from .gists import GistsClient
    from .pulls import PullsClient
    from .repos import ReposClient
    from .teams import TeamsClient
    from .users import UsersClient
    from .checks import ChecksClient
    from .emojis import EmojisClient
    from .issues import IssuesClient
    from .search import SearchClient
    from .actions import ActionsClient
    from .billing import BillingClient
    from .copilot import CopilotClient
    from .activity import ActivityClient
    from .licenses import LicensesClient
    from .markdown import MarkdownClient
    from .packages import PackagesClient
    from .projects import ProjectsClient
    from .classroom import ClassroomClient
    from .gitignore import GitignoreClient
    from .reactions import ReactionsClient
    from .codespaces import CodespacesClient
    from .dependabot import DependabotClient
    from .migrations import MigrationsClient
    from .rate_limit import RateLimitClient
    from .interactions import InteractionsClient
    from .code_scanning import CodeScanningClient
    from .code_security import CodeSecurityClient
    from .secret_scanning import SecretScanningClient
    from .codes_of_conduct import CodesOfConductClient
    from .dependency_graph import DependencyGraphClient
    from .security_advisories import SecurityAdvisoriesClient


class RestNamespace:
    def __init__(self, github: "GitHubCore"):
        self._github_ref = ref(github)

    @property
    def _github(self) -> "GitHubCore":
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this namespace after the client has been collected."
        )

    @cached_property
    def meta(self) -> "MetaClient":
        from .meta import MetaClient

        return MetaClient(self._github)

    @cached_property
    def security_advisories(self) -> "SecurityAdvisoriesClient":
        from .security_advisories import SecurityAdvisoriesClient

        return SecurityAdvisoriesClient(self._github)

    @cached_property
    def apps(self) -> "AppsClient":
        from .apps import AppsClient

        return AppsClient(self._github)

    @cached_property
    def classroom(self) -> "ClassroomClient":
        from .classroom import ClassroomClient

        return ClassroomClient(self._github)

    @cached_property
    def codes_of_conduct(self) -> "CodesOfConductClient":
        from .codes_of_conduct import CodesOfConductClient

        return CodesOfConductClient(self._github)

    @cached_property
    def emojis(self) -> "EmojisClient":
        from .emojis import EmojisClient

        return EmojisClient(self._github)

    @cached_property
    def copilot(self) -> "CopilotClient":
        from .copilot import CopilotClient

        return CopilotClient(self._github)

    @cached_property
    def dependabot(self) -> "DependabotClient":
        from .dependabot import DependabotClient

        return DependabotClient(self._github)

    @cached_property
    def secret_scanning(self) -> "SecretScanningClient":
        from .secret_scanning import SecretScanningClient

        return SecretScanningClient(self._github)

    @cached_property
    def activity(self) -> "ActivityClient":
        from .activity import ActivityClient

        return ActivityClient(self._github)

    @cached_property
    def gists(self) -> "GistsClient":
        from .gists import GistsClient

        return GistsClient(self._github)

    @cached_property
    def gitignore(self) -> "GitignoreClient":
        from .gitignore import GitignoreClient

        return GitignoreClient(self._github)

    @cached_property
    def issues(self) -> "IssuesClient":
        from .issues import IssuesClient

        return IssuesClient(self._github)

    @cached_property
    def licenses(self) -> "LicensesClient":
        from .licenses import LicensesClient

        return LicensesClient(self._github)

    @cached_property
    def markdown(self) -> "MarkdownClient":
        from .markdown import MarkdownClient

        return MarkdownClient(self._github)

    @cached_property
    def orgs(self) -> "OrgsClient":
        from .orgs import OrgsClient

        return OrgsClient(self._github)

    @cached_property
    def actions(self) -> "ActionsClient":
        from .actions import ActionsClient

        return ActionsClient(self._github)

    @cached_property
    def oidc(self) -> "OidcClient":
        from .oidc import OidcClient

        return OidcClient(self._github)

    @cached_property
    def code_scanning(self) -> "CodeScanningClient":
        from .code_scanning import CodeScanningClient

        return CodeScanningClient(self._github)

    @cached_property
    def code_security(self) -> "CodeSecurityClient":
        from .code_security import CodeSecurityClient

        return CodeSecurityClient(self._github)

    @cached_property
    def codespaces(self) -> "CodespacesClient":
        from .codespaces import CodespacesClient

        return CodespacesClient(self._github)

    @cached_property
    def packages(self) -> "PackagesClient":
        from .packages import PackagesClient

        return PackagesClient(self._github)

    @cached_property
    def interactions(self) -> "InteractionsClient":
        from .interactions import InteractionsClient

        return InteractionsClient(self._github)

    @cached_property
    def migrations(self) -> "MigrationsClient":
        from .migrations import MigrationsClient

        return MigrationsClient(self._github)

    @cached_property
    def projects(self) -> "ProjectsClient":
        from .projects import ProjectsClient

        return ProjectsClient(self._github)

    @cached_property
    def repos(self) -> "ReposClient":
        from .repos import ReposClient

        return ReposClient(self._github)

    @cached_property
    def billing(self) -> "BillingClient":
        from .billing import BillingClient

        return BillingClient(self._github)

    @cached_property
    def teams(self) -> "TeamsClient":
        from .teams import TeamsClient

        return TeamsClient(self._github)

    @cached_property
    def reactions(self) -> "ReactionsClient":
        from .reactions import ReactionsClient

        return ReactionsClient(self._github)

    @cached_property
    def rate_limit(self) -> "RateLimitClient":
        from .rate_limit import RateLimitClient

        return RateLimitClient(self._github)

    @cached_property
    def checks(self) -> "ChecksClient":
        from .checks import ChecksClient

        return ChecksClient(self._github)

    @cached_property
    def dependency_graph(self) -> "DependencyGraphClient":
        from .dependency_graph import DependencyGraphClient

        return DependencyGraphClient(self._github)

    @cached_property
    def git(self) -> "GitClient":
        from .git import GitClient

        return GitClient(self._github)

    @cached_property
    def pulls(self) -> "PullsClient":
        from .pulls import PullsClient

        return PullsClient(self._github)

    @cached_property
    def search(self) -> "SearchClient":
        from .search import SearchClient

        return SearchClient(self._github)

    @cached_property
    def users(self) -> "UsersClient":
        from .users import UsersClient

        return UsersClient(self._github)
