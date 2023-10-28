# from celery import shared_task
from datetime import datetime, timedelta
from django.conf import settings
from telebot import TeleBot
from config.celery import app
from habit.models import Habit


@app.task
def send_telegram_message(*args, **kwargs):
    """
    Функция отправляет сообщения через Telegram Bot.
    """

    time = datetime.now().time()
    start_time = datetime.now() - timedelta(minutes=1)
    habits_lst = Habit.objects.filter(time__gte=start_time)
    for habit in habits_lst.filter(time__lte=time):
        bot = TeleBot(settings.TG_BOT_TOKEN)
        message = f"Напоминание о выполнении привычки {habit.action} в {habit.time} в {habit.place}"
        bot.send_message(habit.owner.chat_id, message)
