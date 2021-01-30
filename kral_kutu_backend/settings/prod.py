from urllib.parse import urlparse

import django_heroku
import sentry_sdk
from corsheaders.defaults import default_headers
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .base import *

django_heroku.settings(config=locals())

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration(), RedisIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
    )

CORS_ALLOW_HEADERS = list(default_headers) + ['sentry-trace']
ALLOWED_HOSTS = ['italgold.herokuapp.com', 'italgold.vercel.app']

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

DEFAULT_FROM_EMAIL = 'italgold.dev@gmail.com'
