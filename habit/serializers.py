from rest_framework import serializers
from habit.models import Habit
from habit.validators import criteria_validator, AssociatedIsPleasurableValidator


class HabitSerializer(serializers.ModelSerializer):
    # Сокрытие поля "Создатель" и автоматическая привязка его к пользователю
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [criteria_validator, AssociatedIsPleasurableValidator()]
