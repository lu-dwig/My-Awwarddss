import dj_database_url
from pathlib import Path
from pyuploadcare import Uploadcare
import cloudinary
import cloudinary.uploader
import cloudinary.api

import os
from decouple import config, Csv
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
# ALLOWED_HOSTS = ['jango-galleria.herokuapp.com', 'localhost']
# Application definition

DEBUG = True
ALLOWED_HOSTS = [
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'awards.apps.AwardsConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'rest_framework',
    'cloudinary',
    
]

UPLOADCARE ={
    'pub_key' : '2b709bca64245dd9e55e',
    'secret':'django-insecure-tnfjal$7+z-fn61jnc!&$)k)#j(14losqo-h6koer+@2rtim*-'
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_awards.urls'

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

WSGI_APPLICATION = 'my_awards.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# development
if config('MODE') == "dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': 'localhost', # the missing piece of the puzzle 

        }
    }
# production
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
print("BASE DIR: ", BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
print("Static root: ", STATIC_ROOT)
STATIC_URL = '/static/'
print("Static Url: ", STATIC_URL)
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
print("STATICFILES DIRS: ", STATICFILES_DIRS)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = 'login'

cloudinary.config( 
  cloud_name = "dmoi3jabt", 
  api_key = "922158296559976", 
  api_secret = "U-V2Nf12YRGCiKr_-tWkfDqnD8Q" 
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())