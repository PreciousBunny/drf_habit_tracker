import os

from django.core.management import BaseCommand

from habit.models import Habit
from users.models import User, UserRoles


# attention! execute the program with the command:
# >_ python manage.py create_users

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        Команда для сброса и создания вариаций тестовых пользователей.
        """

        print("Привет! Начинаю заполнять БД вариациями тестовых пользователей - Wait few minutes!")

        User.objects.all().delete()
        Habit.objects.all().delete()

        superuser = User.objects.create(
            email=os.getenv('EMAIL_HOST_ADMIN'),
            first_name='Admin',
            last_name='Adm',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        superuser.set_password(os.getenv('ADMIN_PASSWORD'))
        superuser.save()

        moderator_user = User.objects.create(
            email=os.getenv('EMAIL_HOST_MODERATOR'),
            first_name='Moderator',
            last_name='Mod',
            is_staff=True,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MODERATOR,
        )
        moderator_user.set_password(os.getenv('MODERATOR_PASSWORD'))
        moderator_user.save()

        user1 = User.objects.create(
            email='user1@example.com',
            first_name='User1',
            last_name='User1',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        user1.set_password(os.getenv('MODERATOR_PASSWORD'))
        user1.save()

        user2 = User.objects.create(
            email='user2@example.com',
            first_name='User2',
            last_name='User2',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
            chat_id=os.getenv('TG_CHAT_ID'),
        )
        user2.set_password(os.getenv('MODERATOR_PASSWORD'))
        user2.save()

        print('Все пользователи созданы!')
