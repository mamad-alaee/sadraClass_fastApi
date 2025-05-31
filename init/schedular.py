from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger




def my_cron_job():
    print("i am doing this every 10 seconds")
    
    
def createCronTrigger():
    trigger = IntervalTrigger(seconds=3)
    return trigger
    
    
def set_scheduler():
    scheduler = BackgroundScheduler()
    trigger = createCronTrigger()
    scheduler.add_job(my_cron_job,trigger)
    scheduler.start()
    