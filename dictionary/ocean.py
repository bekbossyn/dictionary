from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dictionary_database',
        'USER': 'dictionary_user',
        'PASSWORD': 'dictionary_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/home/development/static/'
MEDIA_ROOT = '/home/development/media/'

SITE_URL = 'http://159.65.140.145'
