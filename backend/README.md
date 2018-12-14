# REST API для проекта рейтинга студента

## Предустановка

Перед началом работы активируйте virtualenv из корня проекта (папка корня репозитория)

```bash
source ENV/bin/activate
```

Требуется pip с версией старше 9.1  
[установка pip](https://pip.pypa.io/en/stable/installing/#)

Требуется установить Django

```bash
pip install django
```

Еще django rest framework

```bash
pip install django-rest-framework
```

а также django cors headers

```bash
pip install django-cors-headers
```

и Pillow

```bash
pip install Pillow
```

## Запуск сервера

Все пути прописаны из корня проекта (корень репозитория)

```bash
cd backend
```

```bash
python3 manage.py runserver
```

## Адреса

localhost:8000/admin — админ-панель
http://localhost:8000/students/ — api студентов