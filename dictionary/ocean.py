from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dict_database',
        'USER': 'dict_user',
        'PASSWORD': 'dict_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/development/static/'
MEDIA_ROOT = '/home/development/media/'

SITE_URL = 'http://159.65.140.145'
