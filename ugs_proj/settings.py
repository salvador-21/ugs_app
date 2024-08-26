"""
Django settings for ugs_proj project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.core.management.utils import get_random_secret_key
import os
import sys
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
USE_TZ = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-ard^dr15f8bucl+ml=s)g@4g^ck&8s5!5ys+l&9$cwf^1n(7d2'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.getenv("DEBUG", "False") == "True"
# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
CORS_ALLOWED_ORIGINS =[
    # 'http://localhost:8000',
    # 'http://127.0.0.1:8000',
    'https://ultimate-gs.net',
]

CORS_ALLOW_CREDENTIALS =True
AUTH_USER_MODEL = 'ugs_app.UserProfile'

# Application definition

INSTALLED_APPS = [
    'channels',
    'staking_app.apps.StakingAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ugs_app.apps.UgsAppConfig',
    'rest_framework',
    'corsheaders',
    'django.contrib.humanize',
    'django_minify_html',
    'django_template_obfuscator.apps.DjangoTemplateObfuscatorConfig',
    'django_hide',
    'django_recaptcha',
]

MIDDLEWARE = [
    'django_hide.middleware.CSRFHIDEMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_minify_html.middleware.MinifyHtmlMiddleware',
]

ROOT_URLCONF = 'ugs_proj.urls'

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

WSGI_APPLICATION = 'ugs_proj.wsgi.application'
ASGI_APPLICATION = 'ugs_proj.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ugs_db_081324',
#         'USER': 'root',
#         'PASSWORD':'Kinsee_06',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"
if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG':{
            "hosts": [
                os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')
            ],
        }
    }
}

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = ( os.path.join(BASE_DIR,'ugs_app/static/'),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, 'ugs_app/static/ugs_app/uploads')
MEDIA_URL = '/uploads/'



# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'uploads'),
#     )
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


RECAPTCHA_PUBLIC_KEY = '6Ld3iA8qAAAAABXPe2MdSf4htmxTJq4mdKjqbMvM'
RECAPTCHA_PRIVATE_KEY = '6Ld3iA8qAAAAAMh29MY2cpYxj9mqqgT8vGUh9-5L'
