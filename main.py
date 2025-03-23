from src.core.agent import GitHubSentinelAgent
from src.core.scheduler import SentinelScheduler
import os

if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TOKEN")
    agent = GitHubSentinelAgent(github_token)
    
    # 手动运行模式
    # agent.check_updates()
    
    # 定时任务模式
    scheduler = SentinelScheduler(agent)
    scheduler.start()
