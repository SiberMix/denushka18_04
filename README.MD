# README

Этот файл содержит инструкции по установке и запуску приложения.
Stack: 
```alembic           1.10.3`
anyio             3.6.2
black             23.3.0
cffi              1.15.1
click             8.1.3
cryptography      40.0.2
ecdsa             0.18.0
fastapi           0.95.1
greenlet          2.0.2
gunicorn          20.1.0
h11               0.14.0
idna              3.4
Jinja2            3.1.2
Mako              1.2.4
MarkupSafe        2.1.2
mypy-extensions   1.0.0
packaging         23.1
passlib           1.7.4
pathspec          0.11.1
pip               23.1
platformdirs      3.2.0
psycopg2-binary   2.9.6
pyasn1            0.4.8
pycparser         2.21
pydantic          1.10.7
python-jose       3.3.0
python-multipart  0.0.6
rsa               4.9
setuptools        67.6.1
six               1.16.0
sniffio           1.3.0
SQLAlchemy        2.0.9
starlette         0.26.1
tomli             2.0.1
typing_extensions 4.5.0
uvicorn           0.21.1
```
## Установка

1. Установите все необходимые библиотеки, перейдя в корневую директорию проекта и выполните команду:
```
pip install -r req.txt
```

2. Установите Docker и Docker Compose, если они еще не установлены.

3. Запустите базу данных, перейдя в корневую директорию проекта и выполните команду:
```
docker-compose up -d
```
Эта команда создат автоматически контейнер с базой данных postgres 14 и все сразу будет писаться туда. 
## Запуск

1. Перейдите в папку `app`.

2. Запустите сервер, выполнив команду:
```
python main.py
```

После этого приложение будет доступно по адресу ` http://0.0.0.0:8000` или `http://127.0.0.1:8000/`
Доступные линки: `http://0.0.0.0:8000/register` `http://0.0.0.0:8000/login` `http://0.0.0.0:8000` `http://0.0.0.0:8000/docs`
