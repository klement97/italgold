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

sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[DjangoIntegration(), RedisIntegration()],
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
        )

CORS_ALLOW_HEADERS = list(default_headers) + ['sentry-trace']
ALLOWED_HOSTS = [
    'italgold.herokuapp.com',
    'italgold.vercel.app',
    'italgold-api.herokuapp.com'
    ]

STATICFILES_STORAGE = os.getenv('STATICFILES_STORAGE')
DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_AUTH = True
AWS_QUERYSTRING_EXPIRE = 3600  # seconds
AWS_S3_FILE_OVERWRITE = False
AWS_IS_GZIPPED = True
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'eu-central-1'

CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": os.environ.get('REDIS_URL'),
    }
}

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
ADMINS = [
    ('Klement Omeri', 'klementomeri97@gmail.com'),
    ('Klement Omeri', 'italgold.dev@gmail.com'),
    ('Klement Omeri', 'klement-omeri97@hotmail.com'),
    ]
