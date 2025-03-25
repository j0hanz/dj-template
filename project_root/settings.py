"""Django settings"""

import os
from pathlib import Path

import cloudinary
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path configuration
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = 'DEV' in os.environ
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cloudinary',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'core',
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# URL configuration
ROOT_URLCONF = 'project_root.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                (
                    'django.template.loaders.cached.Loader',
                    [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ],
                ),
            ],
        },
    },
]


# WSGI configuration
WSGI_APPLICATION = 'project_root.wsgi.application'

# Database configuration
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'CONN_MAX_AGE': 60,
        }
    }
    print('Development environment')
else:
    DATABASES = {'default': dj_database_url.parse(os.getenv('DATABASE_URL'))}
    DATABASES['default']['CONN_MAX_AGE'] = 60
    print('Production environment')

# Authentication configuration
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' (Uncomment for production)

# Default field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security configuration
CSRF_TRUSTED_ORIGINS = [
    'https://*.herokuapp.com',
]

# Site configuration
SITE_ID = 1

# Authentication settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_NAME'),
    api_key=os.getenv('CLOUDINARY_KEY'),
    api_secret=os.getenv('CLOUDINARY_SECRET'),
    secure=True,
)

# Jazzmin admin theme settings
# https://django-jazzmin.readthedocs.io/configuration/
JAZZMIN_SETTINGS = {
    'site_title': 'Django',
    'site_brand': 'admin panel',
    'site_header': 'Django',
    'site_logo': 'images/favicon.ico',
    'welcome_sign': '',
    'topmenu_links': [
        {
            'name': 'Home',
            'url': 'admin:index',
            'permissions': ['auth.view_user'],
        },
        {'model': 'auth.User'},
        {'app': 'core'},
        {
            'name': 'Site',
            'url': '/',
            'new_window': True,
        },
    ],
    'usermenu_links': [
        {'model': 'auth.user'},
        {
            'name': 'Documentation',
            'url': 'https://docs.djangoproject.com/',
            'new_window': True,
        },
    ],
    'related_modal_active': True,
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [
        'socialaccount.SocialApp',
        'socialaccount.SocialAccount',
        'socialaccount.SocialToken',
    ],
    'order_with_respect_to': ['auth', 'core'],
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'core': 'fas fa-cogs',
    },
    'default_icon_parents': 'fas fa-folder',
    'default_icon_children': 'fas fa-folder',
}

# Jazzmin UI tweaks
# https://django-jazzmin.readthedocs.io/ui_customisation/
JAZZMIN_UI_TWEAKS = {
    'navbar': 'navbar-dark',
    'no_navbar_border': True,
    'dark_mode_theme': None,
}
