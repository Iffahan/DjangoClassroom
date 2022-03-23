from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'myP@ssw0rd',
        'HOST': 'dj_mysql',
        'PORT': '3306',
    }
}

DEBUG = False