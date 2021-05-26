from .base import *

DEBUG = True

SECRET_KEY = 'development'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

# LOGGING['loggers']['django.db.backends'] = {
#     'handlers': ['console'],
#     'level': 'DEBUG',
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'italgold',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '172.30.1.7',
        'PORT': '5432',
        }
    }

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles/')
MEDIA_URL = '/mediafiles/'

AUTH_PASSWORD_VALIDATORS = []

ALLOWED_HOSTS = ['*']
