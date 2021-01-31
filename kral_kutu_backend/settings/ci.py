from .dev import *

SECRET_KEY = 'ci/cd'
AUTH_PASSWORD_VALIDATORS = []
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
