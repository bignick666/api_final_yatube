Проект Yatube социальная сеть
Проект - это социальная сеть для постов, групп, пользователей и котиков. Реализован API

Используемые технологии
Python 3.9, Django 3.2.16 Django ORM, Django REST Framework (DRF), REST API, SQLite3, CSRF, Paginator, Simple-JWT, Djoser

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/Trohimets/api_final_yatube.git
cd api_final_yatube

Cоздать и активировать виртуальное окружение:
python -m venv venv
source venv/scripts/activate

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver
