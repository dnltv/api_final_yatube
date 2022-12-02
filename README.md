# api_final
Final project of the 9th Sprint of the Yandex.Practicum course


## Overwiew
API for the <a href="https://github.com/dnltv/hw05_final">Yatube</a> project

## Features and Examples
- Getting posts for any users. 
- Writing posts for authorized users
- Splitting posts into groups
- Getting and working with comments to posts
- Subscribing to authors

## Stack
- [Python 3.7.0](https://www.python.org)
- [Django 3.2.14](https://www.djangoproject.com)
- [djangorestframework 3.12.4](https://www.django-rest-framework.org)

Full information in requirements.txt

## Examples


## Getting Started
Clone the repository and go to it on the command line:

```
git clone https://github.com/dnltv/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install requirements:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Perform migrate:

```
python3 manage.py migrate
```

Launch a project:

```
python3 manage.py runserver
```

API is available at http://127.0.0.1:8000/api/v1/

## Documentation

Read the documentation by running the project and opening the tab http://127.0.0.1:8000/redoc/
