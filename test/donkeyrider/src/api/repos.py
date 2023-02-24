from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict
from git import Repo
from github import Github
import github


import requests

class GitRepo(ABC):
    """A wrapper around the git.Repo class to add some extra functionality."""
    @property
    def type(self) -> str:
        """The type of repository, either "local" or "remote"."""
        return self._type

    @property
    def path(self) -> str:
        """The path to the repository."""
        return self._path

    @path.setter
    def path(self, value: Path | str):
        if isinstance(value, Path):
            self._path = str(value)
        else:
            self._path = value

    def __init__(self, path: Path | None = None, url: str | None = None):
        if path is None and url is None:
            raise ValueError("Must provide either a path or a url to the repository.")
        self.path = path
        if path is not None:
            self._type = "local"
        else:
            self._type = "remote"

    @property
    @abstractmethod
    def release_families(self) -> list[str]:
        """The current release families of the repository."""
        pass 

    

class LocalRepo(GitRepo, Repo):
    def __init__(self, path: Path, upstream: str, github_token: str ):
        GitRepo.__init__(self, path=path)
        Repo.__init__(self, path)
        self._github_token = github_token
        self.upstream = upstream

    @property
    def upstream(self) -> str:
        return self._upstream
    
    @upstream.setter
    def upstream(self, value: str):
        # check if upstream url exists
        try:
            repo = Github(self._github_token).get_repo(value)
            self._upstream = value
        except github.GithubException as e:
            raise ValueError(f"Upstream repository {value} does not exist.") from e
    
    @property
    def github_token(self) -> str:
        return self._github_token

    @github_token.setter
    def github_token(self, value: str):
        self._github_token = value
    
    @property
    def release_families(self) -> Dict[str, str]:
        """
        The current release families of the repository. 
        Returns a dictionary with key as the release line and value as the latest commit hash in that release line.
        """
        release_branches = [branch.name for branch in self.branches if branch.name.startswith("feature-")]
        return { 
            release_family: self.get_latest_commit(release_family) 
            for release_family in release_branches 
        }

    def get_latest_commit(self, branch: str) -> str:
        """Returns the latest commit hash for the given branch."""
        return self.branches[branch].commit

    def __str__(self):
        return f"LocalRepo({self.path})"
    