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
