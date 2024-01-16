import os
from dotenv import load_dotenv
from pathlib import Path
from django_ratelimit.middleware import RatelimitMiddleware
import mimetypes
import datetime

mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_w3igt4)kvso#_)9cq3-daz!@8xobw55jdk=x((m1h#5lwd2z-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if os.environ.get('WEB_ENV') == 'prod':
  DEBUG = False

ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
  'daphne',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'perpus',
  'inertia',
  'django_vite',
  'rest_framework',
  'corsheaders',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'inertia.middleware.InertiaMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django_ratelimit.middleware.RatelimitMiddleware',
  'perpus.authentication.JSONWebTokenAuthentication',
  'perpus.middleware.ContentTypeMiddleware',
]

RATELIMIT_VIEW = 'perpus.views.ratelimited_error'

ROOT_URLCONF = 'perpus.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      BASE_DIR / 'templates',
    ],
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

CORS_ALLOWED_ORIGINS = [
  'http://localhost:8000',
]

CORS_ALLOW_CREDENTIALS = True

JWT = {
  'ACCESS_TOKEN_LIFETIME': datetime.datetime.utcnow() + datetime.timedelta(weeks=16),
  'REFRESH_TOKEN_LIFETIME': datetime.datetime.utcnow() + datetime.timedelta(days=1),
  'ROTATE_REFRESH_TOKENS': False,
  'BLACKLIST_AFTER_ROTATION': True,
  'UPDATE_LAST_LOGIN': False,

  'ALGORITHM': 'HS256',
  'SIGNING_KEY': SECRET_KEY,
  'VERIFYING_KEY': None,
  'AUDIENCE': None,
  'ISSUER': None,

  'AUTH_HEADER_TYPES': ('Bearer',),
  'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
  'USER_ID_FIELD': 'id',
  'USER_ID_CLAIM': 'user_id',
  
  'TOKEN_TYPE_CLAIM': 'token_type',

  'JTI_CLAIM': 'jti',

  'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
  'SLIDING_TOKEN_LIFETIME': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
  'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.datetime.utcnow() + datetime.timedelta(days=1),

  # custom
  'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
  'AUTH_COOKIE_DOMAIN': None,     # A string like 'example.com', or None for standard domain cookie.
  'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
  'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
  'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
  'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
}

WSGI_APPLICATION = 'perpus.wsgi.application'
ASGI_APPLICATION = "perpus.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('MARIADB_DATABASE'),
    'USER': os.environ.get('MARIADB_USER'),
    'PASSWORD': os.environ.get('MARIADB_PASSWORD'),
    'HOST':  os.environ.get('MARIADB_HOST'),
    'PORT': os.environ.get('MARIADB_PORT'),
  }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Use bcrypt for password hashing
PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = BASE_DIR / 'web' / 'dist'
DJANGO_VITE_DEV_MODE = True
DJANGO_VITE_DEV_SERVER_PORT = 3000

# Name of static files folder (after called python manage.py collectstatic)
STATIC_ROOT = BASE_DIR / 'web' / 'dist' / '.vite' 

# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS = [
  DJANGO_VITE_ASSETS_PATH,
  BASE_DIR / 'web' / 'assets'
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Inertia
INERTIA_LAYOUT = 'app.html'
CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'
CSRF_COOKIE_NAME = 'XSRF-TOKEN'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': '{asctime} {levelname} {filename} {funcName} {lineno} {message}',
      'style': '{',
    },
    'simple': {
      'format': '{asctime} {levelname} - {message}',
      'style': '{',
    },
  },
  'filters': {
    'require_debug_false': {
      '()': 'django.utils.log.RequireDebugFalse',
    },
    'require_debug_true': {
      '()': 'django.utils.log.RequireDebugTrue',
    },
  },
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'filters': ['require_debug_true'],
      'formatter': 'simple',
    },
    'log_file': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': 'api.log',
      'maxBytes': 1024 * 1024 * 5,
      'backupCount': 5,
      'formatter': 'verbose',
    },
    'error_file': {
      'level': 'ERROR',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': 'api_error.log',
      'maxBytes': 1024 * 1024 * 5,
      'backupCount': 5,
      'formatter': 'verbose',
    },
    'mail_admins': {
      'level': 'ERROR',
      'class': 'django.utils.log.AdminEmailHandler',
      'filters': ['require_debug_false'],
      'formatter': 'verbose',
    },
  },
  'loggers': {
    'django_project_api': {
      'handlers': ['console', 'log_file', 'error_file', 'mail_admins'],
      'level': 'DEBUG',
    },
    'django.request': {
      'handlers': ['mail_admins', 'error_file'],
      'level': 'ERROR',
      'propagate': False,
    },
  },
}

REST_FRAMEWORK = {
  'DEFAULT_THROTTLE_CLASSES': [
    'rest_framework.throttling.AnonRateThrottle',
    'rest_framework.throttling.UserRateThrottle'
  ],
  'DEFAULT_THROTTLE_RATES': {
    'anon': '30/min',
    'user': '30/min'
  },
  'EXCEPTION_HANDLER': 'perpus.common_response.ThrottledHandler',
}