# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "SplitWise2023.settings")

app = Celery('SplitWise2023')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Schedule the task weekly
app.conf.beat_schedule = {
    'send-weekly-email': {
        'task': 'SplitWiseApp.tasks.send_weekly_email',
        'schedule': crontab(minute=0, hour=0, day_of_week=1),  # Every Monday at midnight
    },
}
