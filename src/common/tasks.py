import time
from datetime import datetime

from celery import shared_task


@shared_task
def check_celery_task_health():
    print(f'celery task is working fine at {datetime.now().strftime("%d/%m/%y - %H:%M:%S")}.')


@shared_task
def ping():
    time.sleep(3)
    return "pong"
