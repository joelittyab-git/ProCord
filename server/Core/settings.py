"""
Django settings for Core project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# database credentials file
from __config.credentials import (
    DefaultDatabase,
    ChannelLayerDatabase
)

from Core.base import BaseConfiguration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g&xayr$()$e18-jxgr@9m_%b2grgq2j4x46&j#5@7)g0&vyip&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'channels',
    'channels_postgres',
    "debug_toolbar",
    
    "User",
    "ChatRoom"
    
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",                        #cors headers middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",              #debug toolbar middleware
]

# rest framework authentication and permission configuration
REST_FRAMEWORK =  BaseConfiguration.REST_FRAMEWORK_CONFIGURATION

ROOT_URLCONF = 'Core.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'Core.wsgi.application'
ASGI_APPLICATION = 'Core.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': f'{DefaultDatabase.NAME}',
        'PORT':f'{DefaultDatabase.PORT}',
        'HOST':f"{DefaultDatabase.HOST}",
        'USER':f'{DefaultDatabase.USER}',
        'PASSWORD':F'{DefaultDatabase.PASSWORD}'
    },
    'channels_postgres': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': f'{ChannelLayerDatabase.NAME}',
		'USER': f'{ChannelLayerDatabase.USER}',
		'PASSWORD': f'{ChannelLayerDatabase.PASSWORD}',
		'HOST': f'{ChannelLayerDatabase.HOST}',
		'PORT': f'{ChannelLayerDatabase.PORT}',
	}
    
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_postgres.core.PostgresChannelLayer',
        'CONFIG': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': f'{ChannelLayerDatabase.NAME}',
            'USER': f'{ChannelLayerDatabase.USER}',
            'PASSWORD': f'{ChannelLayerDatabase.PASSWORD}',
            'HOST': f'{ChannelLayerDatabase.HOST}',
            'PORT': f'{ChannelLayerDatabase.PORT}',

        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

# IP's for django bebug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    'localhost'
]