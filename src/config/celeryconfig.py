from celery.schedules import crontab

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

enable_utc = True

CELERY_BEAT_SCHEDULE = {
    "check_celery_task_health": {
        "task": "common.tasks.check_celery_task_health",
        "schedule": crontab(),
    },
}

MAX_RETRIES_FOR_BASIC_DATA = 5
RETRY_DELAY = 30 * 60
