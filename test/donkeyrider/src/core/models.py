from pathlib import Path
from typing import Dict
from git import Commit, Repo
from github import Github, Repository, Branch as branch
from typing import List

class LocalRepo(Repo):
    def __init__(self, path: Path, upstream: str, github_token: str ):
        self.path = path
        Repo.__init__(self, path)
        self._github_token = github_token
        org, repo = upstream.split('/')
        if org is None or repo is None:
            raise ValueError("Invalid upstream repository {upstream}. Please specify it in the format <org>/<repo}")
        self._upstream = RemoteRepo(org, repo, github_token)

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
    @property
    def upstream(self) -> 'RemoteRepo':
        return self._upstream
    
   
    def get_latest_commit(self, branch: str) -> str:
        """Returns the latest commit hash for the given branch."""
        return self.branches[branch].commit

    def get_closest_release_family(self) -> str:
        """Returns the closest release family to the current HEAD."""
        release_branch_commit_map = self.upstream.get_release_branch_commit_map()
        git_history = self.iter_commits()
        for commit in git_history:
            for branch_name, branch_commit in release_branch_commit_map.items():
                if commit.hexsha == branch_commit.sha:
                    return branch_name
        return None

    def __str__(self):
        return f"LocalRepo({self.path})"
    

class RemoteRepo():
    """ __summary__  A class to represent a remote repository on Github.
    """
    def __init__(self, org, repo, github_token: str):
        self._org_name, self._repo_name = org, repo
        self._github_token = github_token
        self._client = Github(github_token)

    @property
    def org_name(self) -> str:
        return self._org_name
    
    @property
    def repo_name(self) -> str:
        return self._repo_name

    @property
    def client(self) -> Github:
        return self._client

    @property
    def repo(self) -> Repository:
        return self.client.get_repo(f"{self.org_name}/{self.repo_name}")
    
    @property
    def release_branches(self) -> List[branch.Branch]:
        """Returns a dictionary of release branches and their latest commit hashes."""
        return [branch for branch in self.repo.get_branches() if branch.name.startswith("feature-")]

    def get_release_branch_commit_map(self) -> Dict[branch.Branch, Commit]:
        """Returns a dictionary of release branches and their latest commit hashes."""
        return {branch.name: branch.commit for branch in self.release_branches}