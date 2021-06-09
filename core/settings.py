"""
Django settings for APP project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import configparser
from django.apps import AppConfig

####################################################################
# GENERAL SETTINGS
####################################################################

# Django root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PERSONAL WARNING: Don't put this file in your git with important values
ini_path = os.path.join(BASE_DIR, 'private.ini')
Config = configparser.ConfigParser()
Config.read(ini_path)

# GOOD PRACTICE: Set minimum two environnements DEV/PROD
ENV = Config.get('DJANGO', 'ENV')

# SECURITY WARNING: change the secret key for each environnement!
SECRET_KEY = Config.get('DJANGO', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if ENV == 'DEV':
    DEBUG = True
else:
    DEBUG = False

# SECURITY WARNING: Whitelist as minimum as possible to reduce security risks.
ALLOWED_HOSTS = Config.get('DJANGO', 'ALLOWED_HOSTS').split(",")


####################################################################
# DJANGO APPLICATIONS
####################################################################
# Required for django >3.2 if not we need to add full path to each apps.py config name
AppConfig.default = False


def get_apps_definitions(apps_folder):
    """ Detect all modules , only if they are always inside modules folder

    :return: List of app_definitions
    """
    app_definitions = []
    for full_path, apps, folders in os.walk(os.path.join(BASE_DIR, apps_folder)):
        if os.path.basename(full_path) == apps_folder:
            for app in apps:
                fix_path_windows_linux = os.path.relpath(full_path, BASE_DIR).replace("/",".").replace("\\",".")
                app_path = f'{fix_path_windows_linux}.{app}'
                app_definitions.append(app_path)
    return app_definitions


DJANGO_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGO_EXTERNAL_APPS = []

DJANGO_SUBAPPS = get_apps_definitions('subapps')

INSTALLED_APPS = DJANGO_CORE_APPS + DJANGO_EXTERNAL_APPS + DJANGO_SUBAPPS

####################################################################
# REQUESTS HTTP MANAGER
####################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

####################################################################
# DATABASES
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
####################################################################
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

if ENV == 'DEV':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.db',
        }
    }
elif ENV == 'PROD':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': Config.get('POSTGRES', 'NAME'),
            'USER': Config.get('POSTGRES', 'USER'),
            'PASSWORD': Config.get('POSTGRES', 'PASSWORD'),
            'HOST': Config.get('POSTGRES', 'HOST'),
            'PORT': Config.get('POSTGRES', 'PORT'),
        }
    }

####################################################################
# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
####################################################################
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

####################################################################
# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/3.0/topics/i18n/
####################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

####################################################################
# STATIC FILES (CSS, JavaScript, Images)
# on debug false, static files are took from root path
# https://docs.djangoproject.com/en/3.0/howto/static-files/
####################################################################
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = Config.get('STATIC', 'STATIC_ROOT'),
if ENV == 'DEV':
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    MEDIA_ROOT = Config.get('STATIC', 'MEDIA_ROOT'),
