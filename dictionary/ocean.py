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

STATIC_URL = '/root/dev/static/'
STATIC_ROOT = '/root/dev/static/'
MEDIA_ROOT = '/root/dev/media/'

SITE_URL = 'http://159.65.140.145'
