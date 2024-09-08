from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Создание нового пользователя
    """

    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        password = user.password
        user.set_password(password)
        user.save()
