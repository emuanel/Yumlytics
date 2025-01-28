from config import settings

from celery.app import Celery

worker = Celery(
    settings.celery_name,
    broker=settings.celery_broker_url,
    backend=settings.celery_backend_url,
)

worker.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    broker_connection_retry_on_startup=True,
)
