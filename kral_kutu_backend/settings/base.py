import os

package_path = os.path.dirname(os.path.dirname(os.path.abspath(__package__)))
root_path = 'kral_kutu_backend'
BASE_DIR = os.path.join(package_path, root_path)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
    ]

THIRD_PARTY = [
    'corsheaders',
    'rest_framework',
    'django_filters',
    ]

INTERNAL = [
    'order'
    ]

INSTALLED_APPS += THIRD_PARTY
INSTALLED_APPS += INTERNAL

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'kral_kutu_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            'libraries': {
                'templatetags': 'order.templatetags.i18n_switcher'
                }
            },
        },
    ]

WSGI_APPLICATION = 'kral_kutu_backend.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        ],
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.Pagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
        ),
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = [
    ('en', 'English'),
    ('tr', 'Turkish'),
    ('sq', 'Albanian'),
    ]

FRONTEND_URL = 'https://italgold.herokuapp.com'
FRONTEND_INVOICE_URL = f'{FRONTEND_URL}/order/post-checkout'
