# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from habit.models import Habit
from users.models import User, UserRoles


# Create your tests here.


class HabitTestCase(APITestCase):
    """
    Класс для тестов модели Habit.
    """

    def setUp(self) -> None:
        """
        Метод подготавливает данные тестового пользователя перед каждым тестом.
        """
        self.user = User.objects.create(
            id=1,
            email='testuser@example.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
            chat_id=9999999999,
        )
        self.user.set_password('testpassword')
        self.user.save()

        # Получаем токен авторизации
        response = self.client.post('/users/token/',
                                    {'email': 'testuser@example.com', 'password': 'testpassword'})
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'habit_for_test'

    def test_habit_create(self):
        """
        Метод тестирует создание привычки.
        """
        habit_test = Habit.objects.create(name=self.test_model_name,
                                          place="home", time="10:10",
                                          action="do 10 push-ups",
                                          is_pleasurable=True,
                                          periodic=1,
                                          reward=None,
                                          execution_time="00:02",
                                          is_public=True,
                                          owner=self.user,
                                          associated_habit=None)
        response = self.client.post('/habits/', {'name': 'test2',
                                                 'place': 'home',
                                                 'time': '10:10',
                                                 'action': 'do 10 push-ups',
                                                 'is_pleasurable': True,
                                                 'periodic': 1,
                                                 'reward': 'None',
                                                 'execution_time': '00:02',
                                                 'is_public': True,
                                                 'owner': 1})
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(habit_test.name, 'habit_for_test')

    def test_get_habit(self):
        """
        Метод тестирует просмотр созданной привычки.
        """
        self.test_habit_create()
        response = self.client.get('/habits/1/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 1, 'name': 'habit_for_test',
                                           'place': 'home',
                                           'time': '10:10:00',
                                           'action': 'do 10 push-ups',
                                           'is_pleasurable': True,
                                           'periodic': 1,
                                           'reward': None,
                                           'execution_time': '00:02:00',
                                           'is_public': True, 'owner': 1,
                                           'associated_habit': None})

    def test_list_habits(self):
        """
        Метод тестирует просмотр листа привычек.
        """
        self.test_habit_create()
        response = self.client.get('/habits/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_list_habits_public(self):
        """
        Метод тестирует просмотр публичного листа привычек.
        """
        self.test_habit_create()
        response = self.client.get('/public_habits')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)


class SuperuserTestCase(APITestCase):
    """
    Класс для теста superuser.
    """

    def setUp(self) -> None:
        """
        Метод подготавливает данные тестового superuser для теста.
        """
        self.superuser = User.objects.create(
            email='testadmin@example.com',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER,
            chat_id=9999999999,
        )
        self.superuser.set_password('testpassword')
        self.superuser.save()

        # Получаем токен авторизации
        response = self.client.post('/users/token/',
                                    {"email": "testadmin@example.com", "password": "testpassword"})
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_users_get(self):
        """
        Метод тестирует вывод/отображение созданного superuser.
        """
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
