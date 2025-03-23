from datetime import datetime, timedelta
from typing import List
from ..models.subscription import Subscription
from ..services.github.github_client import GitHubClient
from ..services.storage.subscription_manager import SubscriptionManager

class GitHubSentinelAgent:
    def __init__(self, github_token: str):
        self.github = GitHubClient(github_token)
        self.subscription_manager = SubscriptionManager()
    
    def check_updates(self):
        subscriptions = self.subscription_manager.load_subscriptions()
        for sub in subscriptions:
            since = sub.last_checked or (datetime.now() - timedelta(days=7))
            events = self.github.get_repo_activity(sub.repo, since)
            if events:
                self._process_events(sub, events)
                sub.last_checked = datetime.now()
        self.subscription_manager.save_subscriptions(subscriptions)
    
    def _process_events(self, sub: Subscription, events: list):
        pass
