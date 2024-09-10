# -*- coding: utf-8 -*-
"""
Django settings for pwn v2 project.
"""

import os
from pathlib import Path
from utils.secret_key_gen import get_secret_key


# ==============================================================================
# PATH CONFIGURATION
# ------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# ==============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent



# ==============================================================================
# the secret key
# ------------------
# SECURITY WARNING: keep the secret key used in production secret!
# ==============================================================================
SECRET_KEY = get_secret_key('secret_key')


# ==============================================================================
# APPS CONFIGURATION
# ==============================================================================
DJANGO_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'django_extensions',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    # 'djangocms_text_ckeditor',
    'djangocms_text',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_snippet',
    'ckeditor',
    'djangocms_text.contrib.text_ckeditor5',
)

LOCAL_APPS = (
    'core',
    'pwn_event',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
DJANGOCMS_TEXT_EDITOR = "djangocms_text.contrib.text_ckeditor5.ckeditor5"

# ==============================================================================
# MIDDLEWARE CONFIGURATION
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ==============================================================================
# URL CONFIGURATION
# ==============================================================================
ROOT_URLCONF = 'core.urls'


# ==============================================================================
# TEMPLATE CONFIGURATION
# ==============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# ==============================================================================
# PASSWORD VALIDATION
# -------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
# ==============================================================================
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

# ==============================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
# ==============================================================================

TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = 'fr'
LANGUAGES = [
    ('fr', 'Français'),
]


# ==============================================================================
# MEDIA
# ==============================================================================
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# ==============================================================================
# STATIC
# ==============================================================================
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'

