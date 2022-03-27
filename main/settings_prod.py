from .settings import *

# run manage.py with --setting=main.settings_prod

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj',
        'USER': 'root',
        'PASSWORD': 'myPassw0rd',
        'HOST': 'dj_mysql',
        'PORT': '3306',
    }
}


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ["https://wd0303.coe.psu.ac.th"]


DEBUG = True