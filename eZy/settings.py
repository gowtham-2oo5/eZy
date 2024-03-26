# Import Section
from pathlib import Path
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent
    
# Security Settings
SECRET_KEY = 'django-insecure-dn-w0ekh6gbqe9im7qu@hza9s8!hpudmsk!#cn+$ez$c3qm^+('
DEBUG = True
ALLOWED_HOSTS = ['gowtham2oo5.pythonanywhere.com']

# Application Definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authApp',
    'userApp'
]

# Middleware Settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'eZy.urls'

# Template Settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/','templates/home','templates/auth','templates/user'],
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

# WSGI Application
WSGI_APPLICATION = 'eZy.wsgi.application'

# Database Settings
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'e_survey_platform',
        'HOST':'localhost',
        'USER':'gowtham',
        'PASSWORD':'gowtham',
        'PORT':'5432',
    }
}
"""
# Password Validators
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

# Internationalization Settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files Settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
