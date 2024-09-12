from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.pagination import MyPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    """
    Просмотр и создание привычек
    """

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = MyPaginator

    def perform_create(self, serializer):
        if not serializer.validated_data.get("started_at"):
            date = timezone.now().date()
        serializer.save(user=self.request.user, started_at=date)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение привычки
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление привычки
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class MyHabitsListView(generics.ListAPIView):
    """
    Список собственных привычек
    """

    serializer_class = HabitSerializer
    pagination_class = MyPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicListAPIView(generics.ListAPIView):
    """Список публичных привычек."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = MyPaginator
