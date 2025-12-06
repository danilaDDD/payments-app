from time import sleep

from celery import shared_task


@shared_task
def task():
    print("Task started")
    sleep(2)
    print("Task completed")