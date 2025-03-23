from apscheduler.schedulers.blocking import BlockingScheduler
from .agent import GitHubSentinelAgent

class SentinelScheduler:
    def __init__(self, agent: GitHubSentinelAgent):
        self.scheduler = BlockingScheduler()
        self.agent = agent
    
    def start(self):
        # 每天凌晨1点执行
        self.scheduler.add_job(self.agent.check_updates, 'cron', hour=1)
        self.scheduler.start()
