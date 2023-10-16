from rest_framework import serializers
from datetime import time

from habit.models import Habit


def criteria_validator(value):
    """
    Функция проверяет ряд заданных критериев.
    """

    if value.get('associated_habit') and value.get('reward'):
        raise serializers.ValidationError('Исключён одновременный выбор '
                                          'связанной привычки и '
                                          'указания вознаграждения.')

    if value.get('execution_time') > time(hour=0, minute=2, second=0):
        raise serializers.ValidationError('Время выполнения должно быть '
                                          'не больше 120 секунд.')

    # if 'associated_habit' in value and value.get(
    # 'associated_habit').is_pleasurable:
    #     raise serializers.ValidationError('В связанные привычки могут
    #     попадать только привычки с признаком приятной привычки.')

    if value.get('associated_habit') and value.get('reward'):
        raise serializers.ValidationError('У приятной привычки не может быть '
                                          'вознаграждения или '
                                          'связанной привычки.')

    if value.get('periodic') > 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, '
                                          'чем 1 раз в 7 дней.')


class AssociatedIsPleasurableValidator():
    def __call__(self, value):
        associated_habit = dict(value).get('associated_habit')
        if associated_habit:
            hab = Habit.objects.get(pk=associated_habit.id)
            if not hab.is_pleasurable:
                raise serializers.ValidationError('В связанные привычки '
                                                  'могут попадать только '
                                                  'привычки с признаком '
                                                  'приятной привычки.')
