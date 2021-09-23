# Authentication Apps Using JWT

````doctest 
    A JSON web token is a standardized, optionally 
    validated and/or encrypted container format 
    that is used to securely transfer information
    between two parties.
````

## Create and Connect virtual environment

## JWT STRING
````doctest 
    JSON Web Token is a string that is sent in the 
    HTTP request (from client to server) to validate
    the authenticity of the client.
````
## Why JWT 
````doctest
     JWTs are a good way of securely transmitting 
     information between parties because they can 
     be signed(secretkey)
````
## Install Packages
```python 
    pip install django 
    pip install djangorestframework
    pip install djangorestframework-simplejwt
````
## configure JWT in django settings.py

````python
INSTALLED_APPS = [
    'app',
    'rest_framework',
    'rest_framework_simplejwt',
]

AUTH_USER_MODEL = 'app.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
````
## Applications URLS

````doctest 
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/auth/register/
    http://127.0.0.1:8000/auth/login/
    http://127.0.0.1:8000/auth/refresh/
    http://127.0.0.1:8000/auth/password/pk/
    http://127.0.0.1:8000/auth/profile/pk/
````

