from apscheduler.schedulers.background import BackgroundScheduler
from .job import set_item_status


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(set_item_status, 'interval', seconds=10, id='item_001', replace_existing=True)
    scheduler.start()