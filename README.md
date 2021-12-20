[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Техническое задание

Необходимо расширить проект «Панель администратора»: запустить приложение через WSGI/ASGI, настроить отдачу статических файлов через Nginx и подготовить инфраструктуру для работы с Docker. 

Задание предполагает выполнение двух последовательных подзадач:
1. Реализовать API на Django, который возвращает список фильмов.
2. Настроить запуск всех компонентов системы (Django, Nginx и Postgresql) с использованием docker-compose.

## Используемые технологии

- Приложение запускается под управлением сервера WSGI/ASGI.
- Для отдачи [статических файлов](https://nginx.org/ru/docs/beginners_guide.html#static) используется **Nginx.**
- Виртуализация осуществляется в **Docker.**

## Основные компоненты системы

1. **Cервер WSGI/ASGI** — сервер с запущенным приложением.
2. **Nginx** — прокси-сервер, который является точкой входа для web-приложения.
3. **PostgreSQL** — реляционное хранилище данных. 

## Подготовка и запуск проекта
### Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/Djalyarim/Admin_panel_sprint_2
```
### Создайте и активируйте виртуальное окружение
```
python -m venv venv<br>
source ./venv/Scripts/activate  #для Windows
source ./venv/bin/activate      #для Linux и macOS
```
### Установите требуемые зависимости
```
pip install -r requirements.txt
```
### В корне проекта создайте файл .env и заполните переменные окружения:
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_PORT=5432
DB_HOST=db
DB_LOCAL_HOST=localhost
SECRET_KEY='=r%8-4!jg_8z!^r793lt@dyn+(^e_($^wd_ic&t#2p5gpsuo-u'
DEBAG=False
ALLOWED_HOSTS=[*]

```
### Соберите docker-compose:
```
infra/docker-compose up -d --build
```
