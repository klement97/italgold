from urllib.parse import urlparse

import dj_database_url
import sentry_sdk
from corsheaders.defaults import default_headers
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .base import *

DEBUG = bool(int(os.getenv('DEBUG')))
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
        )
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            }
        },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
            }
        },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
            }
        }
    }

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration(), RedisIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
    )

CORS_ALLOW_HEADERS = list(default_headers) + ['sentry-trace']
ALLOWED_HOSTS = ['italgold.herokuapp.com', 'italgold.vercel.app',
                 'italgold-api.herokuapp.com']

# Add whitenoise for static files
MIDDLEWARE = tuple(
    ['whitenoise.middleware.WhiteNoiseMiddleware']
    + list(MIDDLEWARE)
    )

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
AWS_QUERYSTRING_EXPIRE = 3600  # seconds
AWS_S3_FILE_OVERWRITE = False

redis_url = urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': f'{redis_url.hostname}:{redis_url.port}',
        'OPTIONS': {
            'PASSWORD': redis_url.password,
            'DB': 0,
            }
        }
    }

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
ADMINS = [
    ('Klement Omeri', 'klementomeri97@gmail.com'),
    ('Klement Omeri', 'italgold.dev@gmail.com'),
    ('Klement Omeri', 'klement-omeri97@hotmail.com'),
    ]
