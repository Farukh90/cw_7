from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None
    email = models.EmailField(max_length=40, unique=True, verbose_name="Email")
    telegram_id = models.CharField(
        max_length=200, verbose_name="телеграм айди", null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
