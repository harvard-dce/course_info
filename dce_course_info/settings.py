"""
Django settings for dce_course_info project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from getenv import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'course_info'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_auth_lti.middleware.LTIAuthMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'dce_course_info.urls'

WSGI_APPLICATION = 'dce_course_info.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django_auth_lti.backends.LTIAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = 'static_root'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'course_info/static'), )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'course_info/templates'),
)

LTI_APPS = {
    'course_info': {
        'id': 'course_info',
        'name': 'Course Info',
        'menu_title': 'Course Info',
        'extensions_provider': 'canvas.instructure.com',
        'description': "Insert live updating course info widget into canvas pages.",
        'privacy_level': 'public',
        'selection_height': '400px',
        'selection_width':'400px',
        'icon_url': STATIC_URL + 'images/course-info.png'
    }
}

SECRET_KEY = env('DJANGO_SECRET_KEY', required=True)

# depends on DATABASE_URL being set in your env. See https://github.com/kennethreitz/dj-database-url
# you can also set DJANGO_DATABASE_DEFAULT_ENGINE if you want to override the
# default engine, e.g., using https://github.com/kennethreitz/django-postgrespool/
# default engine, e.g., using https://github.com/kennethreitz/django-postgrespool/
DATABASES = {
    'default': dj_database_url.config(
        engine=env('DJANGO_DATABASE_DEFAULT_ENGINE', None))
}

REDIS_URL = env('REDIS_URL')

LTI_REQUEST_VALIDATOR = 'course_info.validator.LTIRequestValidator'

LTI_OAUTH_CREDENTIALS = {
    env('LTI_OAUTH_COURSE_INFO_CONSUMER_KEY'): env(
        'LTI_OAUTH_COURSE_INFO_CONSUMER_SECRET')
}

# if you want to test locally and aren't getting real course instance ids from LTI launch params.
COURSE_INSTANCE_ID=env('COURSE_INSTANCE_ID')
if COURSE_INSTANCE_ID :
    COURSE_INSTANCE_ID=str(COURSE_INSTANCE_ID)

ICOMMONS_API_TOKEN= env('ICOMMONS_API_TOKEN')

ICOMMONS_BASE_URL= env('ICOMMONS_BASE_URL')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console'],
            'level': "DEBUG",
        },
    }
}

