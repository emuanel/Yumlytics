from celery.app import Celery

from config import settings

celery_app = Celery(
    settings.celery_name,
    broker=settings.celery_broker_url,
    backend=settings.celery_backend_url,
)


celery_app.conf.update(
    worker_pool="threads",  # prefork, threads
    worker_concurrency=settings.celery_workers,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    broker_connection_retry_on_startup=True
)

celery_app.autodiscover_tasks(["video_analysis"], force=True)
