from django.db import models
from django.utils import timezone


class Habit(models.Model):
    """
    Модель привычки
    """

    user = models.ForeignKey(
        "users.User",
        related_name="habits",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    place = models.CharField(max_length=50, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    duration = models.IntegerField(verbose_name="Время на выполнение", default=10)
    periodicity = models.SmallIntegerField(verbose_name="Периодичность", default=1)
    action = models.CharField(max_length=100, verbose_name="Действие")
    started_at = models.DateField(default=timezone.now)

    pleasant_habit = models.BooleanField(
        verbose_name="Полезная привычка", default=False
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, verbose_name="Связанная привычка"
    )
    reward = models.CharField(verbose_name="Вознаграждение", null=True)

    is_public = models.BooleanField(verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place} каждые {self.periodicity} дней"
