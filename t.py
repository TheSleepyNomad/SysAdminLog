from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from test import check_cmd
import time
from app.config.config import AAAA


scheduler = BackgroundScheduler()
scheduler.add_job(check_cmd, 'interval', seconds=3)
scheduler.start()

while True:
    print('check')
    time.sleep(10)
    print(AAAA)