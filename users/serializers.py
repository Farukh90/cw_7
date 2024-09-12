from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер создаваемого пользователя
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "telegram_id"]
