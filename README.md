# api_final
Final project of the 9th Sprint of the Yandex.Practicum course


## Overwiew
API for the <a href="https://github.com/dnltv/hw05_final">Yatube</a> project. A web service for creating/editing/deleting posts. 
The possibility of subscribing to authors has been implemented.


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


## How it work
### Examples of working with the API for all users
For unauthorized users, working with the API is available in read mode,
you will not be able to change or create anything.
```bash
GET api/v1/posts/ - get a list of all publications.
When specifying the limit and offset parameters, the output should work with pagination
GET api/v1/posts/{id}/ - getting a publication by id

GET api/v1/groups/ - getting a list of available communities
GET api/v1/groups/{id}/ - getting information about the community by id

GET api/v1/{post_id}/comments/ - getting all comments for publication
GET api/v1/{post_id}/comments/{id}/ - getting a comment on a publication by id
```
### Examples of working with the API for authorized users
To create a publication:
```bash
POST /api/v1/posts/
```
body
{
"text": "string",
"image": "string",
"group": 0
}

Update:
```bash
PUT /api/v1/posts/{id}/
```
body
{
"text": "string",
"image": "string",
"group": 0
}

Partial update:
```bash
PATCH /api/v1/posts/{id}/
```
body
{
"text": "string",
"image": "string",
"group": 0
}

Delete:
```bash
DEL /api/v1/posts/{id}/
```
Getting access to the endpoint /api/v1/follow/
(subscriptions) is only available for authorized users.
```bash
GET /api/v1/follow/ - subscription of the user on whose behalf the request was made
to the user transmitted in the request body. Anonymous requests are prohibited.
```
- Authorized users can create posts,
comment on them and subscribe to other users.
- Users can change (delete) the content of which they are the author.

### You need to add a group to the project through the Django admin panel:
```bash
admin/ - after authorization, go to the Groups section and create groups
```
Access to authorized users is available via a JWT token (djoser),
which can be obtained by executing a POST request at:
```bash
POST /api/v1/jwt/create/
```
By passing user data to the body (for example, to postman):
```bash
{
"username": "string",
"password": "string"
}
```
Add the received token to headers (postman), then all the functions of the project will be available:
```bash
Authorization: Bearer {your_token}
```
Update the JWT token:
```bash
POST /api/v1/jwt/refresh/ - updating the JWT token
```
Check the JWT token:
```bash
POST /api/v1/jwt/verify/ - checking the JWT token
```
Pagination is also implemented in the API project (LimitOffsetPagination):
```bash
GET /api/v1/posts/?limit=5&offset=0 - pagination for 5 posts, starting from the first


## Documentation

Read the documentation by running the project and opening the tab http://127.0.0.1:8000/redoc/
