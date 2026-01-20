from app.core.celery import celery_app

@celery_app.task
def send_email():
    pass
