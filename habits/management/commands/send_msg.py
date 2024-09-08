from django.core.management.base import BaseCommand

from habits.tasks import send_reminder_manually


class Command(BaseCommand):
    help = "Отправляет уведомления о запланированных привычках"

    def handle(self, *args, **kwargs):
        send_reminder_manually()
