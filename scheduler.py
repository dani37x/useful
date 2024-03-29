# APScheduler==3.10.1

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone="Europe/Warsaw")

# example func with args
scheduler.add_job(delete_expired_data, args=[7, 0, 0, DATA], trigger='interval', days=1)

scheduler.start()
