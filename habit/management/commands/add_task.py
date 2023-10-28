from datetime import datetime, timedelta
import pytz
from django.conf import settings
from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


# attention! execute the program with the command:
# >_ python manage.py add_task

class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.create(
            interval=schedule,
            name='Send habit reminders',
            task='habits_app.tasks.send_habit_reminders',
            expires=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=365)
        )
