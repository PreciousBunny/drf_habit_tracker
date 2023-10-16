from django.db import models

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Класс для работы с моделью Привычек.
    """
    name = models.CharField(max_length=255, verbose_name='Название привычки')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE,
                              verbose_name='Создатель', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='Место действия')
    time = models.TimeField(verbose_name='Время действия')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_pleasurable = models.BooleanField(default=True,
                                         verbose_name='Призн. полез. привычки')
    associated_habit = models.ForeignKey('self', **NULLABLE,
                                         on_delete=models.SET_NULL,
                                         verbose_name='Связанная привычка')
    periodic = models.PositiveIntegerField(default=1,
                                           verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение',
                              **NULLABLE)
    execution_time = models.TimeField(verbose_name='Время на выполнение',
                                      **NULLABLE)
    is_public = models.BooleanField(default=True,
                                    verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
