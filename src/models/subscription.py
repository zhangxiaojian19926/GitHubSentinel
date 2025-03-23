from pydantic import BaseModel
from datetime import datetime

class Subscription(BaseModel):
    repo: str
    frequency: str
    last_checked: datetime = None
    notification_type: str
