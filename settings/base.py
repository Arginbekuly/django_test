from pathlib import Path

from django.apps import apps
#----------------------------------Path----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
WSGI_APPLICATION = 'settings.wsgi.application'
ASGI_APPLICATION = 'settings.adgi.application'



# Application definition
#---------------------------------------Apps---------------------------------------------
#
DJANGO_AND_THIRD_PARTY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps'
]
PROJECT_APPS = [apps.tasks]

INSTALLED_APPS = PROJECT_APPS + DJANGO_AND_THIRD_PARTY_APPS

#----------------------MIDDLEWARE|TEMPLATES|VALIDATORS---------------------------------------------
#
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
#------------------------------------URLS-------------------------------------------------------
ROOT_URLCONF = 'settings.urls'


# -------------------------------Internationalization--------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

#--------------------------STATIC----------------------
#
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'