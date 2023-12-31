# drf_habit_tracker

## Описание проекта
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек 
и искоренению старых плохих привычек. 
Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.
Результатом создания проекта является бэкенд-сервер SPA веб-приложения.

Трекер полезных привычек реализует принцип создания привычек описываемый в книге - 
хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. 
Но при этом привычка не должна расходовать на выполнение больше 2 минут.

## Развертывание проекта
Для корректной работы проекта, вам необходимо выполнить следующие шаги:

1) Установить локально на свой компьютер Python версией не ниже 3.10.x!
2) Клонировать файлы проекта с GitHub репозитория.
3) Установите виртуальное окружение.
```bash
python -m venv venv 
```
4) Активировать виртуальное окружение (если есть необходимость).
```bash
venv/Scripts/activate.bat 
```
5) Установить необходимые зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
6) Установить Redis, глобально себе на компьютер (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install redis-server
```
7) Запустить Redis-сервер (Redis-сервер запустится на стандартном порту 6379).
```bash
sudo service redis-server start
```
8) Убедиться, что Redis-сервер работает правильно, выполните команду:
```bash
redis-cli ping
```
9) Установить БД PostreSQL (используйте wsl, терминал Ubuntu).
```bash
sudo apt-get install postgresql
```
10) Если БД PostreSQL уже была ранее установлена, то перезапустите сервер PostreSQL.
```bash
sudo service postgresql restart
```
11) Выполнить вход.
```bash
sudo -u postgres psql
```
12) Создать базу данных с помощью следующей команды:
```bash
create database habit_tracker;
```
Если такая база данных уже используется, то возможно изменить ее название на свою.

13) Выйти.
```bash
\q
```
14) Создать файл .env
15) Добавить в файл настройки, как в .env.sample и заполнить их.
15) Применить миграции (локально, у себя в виртуальном окружении проекта).
```bash
python manage.py migrate
```
* При возникновении ошибки, сначала применить миграцию приложения users:
```bash
python manage.py migrate users
```
Потом применить остальные миграции:
```bash
python manage.py migrate
```
16) Запустить сервер
```bash
python manage.py runserver
```
17) Запустить Celery
```bash
celery -A config worker -l INFO
```
```bash
celery -A config beat -l info
```
18) Собрать и запустить образ docker-compose
```bash
docker-compose up --build
```

## Тестирование
* Для запуска тестов:
```bash
python manage.py test
```
* Отобразить процентное покрытие кода тестами:
```bash
coverage run --source='.' manage.py test
```
```bash
coverage report
```