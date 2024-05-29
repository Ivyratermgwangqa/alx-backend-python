#!/usr/bin/env python3
"""
This module contains unit and integration tests for the client.py file.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"login": org_name})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the _public_repos_url property returns the correct URL."""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test that public_repos method returns the correct list of repos."""
        mock_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_get_json.assert_called_once_with("http://example.com/repos")
        mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that the has_license method returns the correct value."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": fixtures.org_payload, "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos, "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the mock for requests.get to use fixtures as payloads."""
        cls.get_patcher = patch('client.requests.get', side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher for requests.get."""
        cls.get_patcher.stop()

    @classmethod
    def mocked_requests_get(cls, url):
        """Mock function for requests.get to return different payloads based on the URL."""
        if "orgs" in url:
            return Mock(json=lambda: cls.org_payload)
        if "repos" in url:
            return Mock(json=lambda: cls.repos_payload)

    def test_public_repos(self):
        """Test that public_repos method returns the expected list of repos."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos method filters repos by license."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
