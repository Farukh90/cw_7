from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings

from .models import Habit
from .services import send_telegram_message


@shared_task
def send_reminder():
    """
    За 10 минут до начала выполнения привычки отправляет предупреждение
    и переносит дату следующего выполнения на количество дней, указанное в периодичности выполнения привычки.
    """

    tz = pytz.timezone(settings.TIME_ZONE)
    now_local = datetime.now(tz)

    habits = Habit.objects.all()

    for habit in habits:
        user_tg = habit.user.telegram_id

        habit_time_local = habit.time.astimezone(tz)

        if (
            user_tg
            and now_local >= habit_time_local - timedelta(minutes=10)
            and now_local.date() == habit_time_local.date()
        ):
            formatted_time = habit_time_local.strftime("%d.%m.%Y %H:%M")

            if habit.pleasant_habit:
                message = f"Молодец, ты заслужил {habit.action} в {formatted_time} {habit.place}"
            else:
                message = (f"Не забудь!!!\n"
                           f"Действие: {habit.action}\n"
                           f"Дата и время: {formatted_time}.\n"
                           f"Место: {habit.place}")

            send_telegram_message(user_tg, message)

            if habit.reward:
                send_telegram_message(
                    user_tg, f"Молодец! Ты заслужил награду: {habit.reward}"
                )

            habit.time += timedelta(days=habit.periodicity)
            habit.save()
