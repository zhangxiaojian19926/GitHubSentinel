import json
from pathlib import Path
from typing import List
from ..models.subscription import Subscription

class SubscriptionManager:
    def __init__(self, storage_path: str = "data/subscriptions.json"):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(exist_ok=True)
        
    def load_subscriptions(self) -> List[Subscription]:
        if not self.storage_path.exists():
            return []
        with open(self.storage_path, "r") as f:
            return [Subscription(**item) for item in json.load(f)]
    
    def save_subscriptions(self, subscriptions: List[Subscription]):
        with open(self.storage_path, "w") as f:
            json.dump([sub.dict() for sub in subscriptions], f, default=str)
