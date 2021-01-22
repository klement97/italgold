import os

import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


def settings(config):
    # Load Django Heroku settings
    django_heroku.settings(config=config)

    # Initialize Sentry
    sentry_sdk.init(
            dsn=os.getenv('SENTRY_DSN'),
            integrations=[DjangoIntegration()],
            traces_sample_rate=1.0,

            # If you wish to associate users to errors (assuming you are using
            # django.contrib.auth) you may enable sending PII data.
            send_default_pii=True
            )

    # Filesystem settings
    config['DEFAULT_FILE_STORAGE'] = os.getenv('DEFAULT_FILE_STORAGE')
    config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
    config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
    config['AWS_STORAGE_BUCKET_NAME'] = os.getenv('AWS_STORAGE_BUCKET_NAME')
    config['AWS_DEFAULT_ACL'] = None
    config['AWS_QUERYSTRING_AUTH'] = False
    config['AWS_QUERYSTRING_EXPIRE'] = 3600  # seconds
    config['AWS_S3_FILE_OVERWRITE'] = False
