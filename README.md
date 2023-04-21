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
source venv/bin/activate (Linux and Mac OS)


Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
Выполнить миграции:

python manage.py migrate
Запустить проект:

python manage.py runserver

Примеры запросов:
- Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
- POST .../api/v1/posts/
Пример ответа:
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}

- Пример GET-запроса: получаем информацию о группе. 
- GET .../api/v1/groups/2/
Пример ответа:
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
