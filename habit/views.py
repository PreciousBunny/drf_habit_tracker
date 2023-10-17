from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginations import HabitPagination
from habit.serializers import HabitSerializer
from habit.services import create_habit_schedule
from users.models import UserRoles

# Create your views here.


class HabitViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с привычками пользователей.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Метод выводит список всех привычек модераторам или администратору,
        владельцам - только созданные им привычки.
        """
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(owner=user)

    def perform_create(self, serializer) -> None:
        """
        Метод создает и сохраняет новую привычку, и создает задачу на отправку.
        """
        serializer.save(owner=self.request.user)
        habit = serializer.save()
        create_habit_schedule(habit)


class HabitsListAPIView(generics.ListAPIView):
    """
    Класс выводит список всех публичных привычек.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]
