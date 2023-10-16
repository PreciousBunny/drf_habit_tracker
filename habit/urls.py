from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .apps import HabitConfig
from .views import HabitViewSet, HabitsListAPIView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')


urlpatterns = [
    path('public_habits', HabitsListAPIView.as_view(), name='public_habits'),
    path('', include(router.urls)),
              ]
