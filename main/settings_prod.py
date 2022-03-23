from .settings import *

# run manage.py with --setting=main.settings_prod


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

ALLOWED_HOSTS = ["wd0303.coe.psu.ac.th"]
CSRF_TRUSTED_ORIGINS = ["https://wd0303.coe.psu.ac.th"]

# STATIC_ROOT = "/code/static"
# MEDIA_ROOT = "/code/media"

DEBUG = False