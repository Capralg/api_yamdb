REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

НАСТРОЙКА ПРОЕКТА:

1)Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/account_name/api_yamdb/

cd api_yamdb

2)Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

3)Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

4)Выполнить миграции:

python3 manage.py migrate

5)Запустить проект:

python3 manage.py runserver

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. 
В документации описано, как должен работать ваш API. Документация представлена в формате Redoc.