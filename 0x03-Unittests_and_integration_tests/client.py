#!/usr/bin/env python3
"""A GitHub org client"""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """A GitHub org client that interacts with GitHub API"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the GitHubOrgClient with an organization name."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Return organization information by making an API request to GitHub.

        Returns:
            Dict: A dictionary containing organization details.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """
        Return the URL for fetching public repositories of the organization.

        Returns:
            str: The URL to fetch public repositories.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """
        Return the payload containing information about public repositories.

        Returns:
            Dict: A dictionary containing repository details.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """
        Return a list of public repository names optionally filtered by license.

        Args:
            license (str, optional): A license key to filter repositories by.

        Returns:
            List[str]: A list of repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """
        Check if the repository has a specific license.

        Args:
            repo (Dict[str, Dict]): A dictionary representing repository details.
            license_key (str): The license key to check against.

        Returns:
            bool: True if the repository has the specified license, False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license