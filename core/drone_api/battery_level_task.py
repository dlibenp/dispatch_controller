from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .models import DroneModel

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', id='id_9876543210', year='*', month='*', day='*', hour='*/1', minute=0, second=0)
def background_task():
    logger.info('Start - Battery Level Check')
    for dron in DroneModel.objects.all():
        logger.info(f'Drone: {dron} - Battery Level: {dron.battery_capacity}')

    logger.info('End - Battery Level Check')
