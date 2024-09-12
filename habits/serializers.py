from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    validate_duration,
    validate_periodicity,
    validate_pleasant_habit,
    validate_related_habit,
    validate_related_habit_and_reward,
)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериалайзер привычки
    """

    duration = serializers.IntegerField(validators=[validate_duration])
    periodicity = serializers.IntegerField(validators=[validate_periodicity])

    class Meta:
        model = Habit
        exclude = ("user",)

    def validate(self, data):
        validate_related_habit_and_reward(data)
        validate_related_habit(data)
        validate_pleasant_habit(data)

        return data
