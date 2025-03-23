from github import Github
from github.Repository import Repository
from datetime import datetime

class GitHubClient:
    def __init__(self, token: str):
        self.client = Github(token)
    
    def get_repo_activity(self, repo_name: str, since: datetime) -> list:
        repo = self.client.get_repo(repo_name)
        events = repo.get_events()
        return [event for event in events if event.created_at > since]
