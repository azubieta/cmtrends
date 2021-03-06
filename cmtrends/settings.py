"""
Django settings for cmtrends project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nn&xi65^tuuuk_-g2=bu-e75*$l!!kju5!i#lvn7_l*z99m!a*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	## Twitter
    'oauth_tokens',
    'm2m_history',
    'taggit',
    'twitter_api',
	## Dajax 
	'dajaxice',
	'dajax',
)

# oauth-tokens settings
OAUTH_TOKENS_HISTORY = True # to keep in DB expired access tokens
OAUTH_TOKENS_TWITTER_CLIENT_ID = 'gAiFpONpJqniQ8iUx74nQfMm1' # application ID
OAUTH_TOKENS_TWITTER_CLIENT_SECRET = 'fR2YA4bM4urcfD1DNzezMxl4i3scOIDhXxXXVtIbN7IEFGiA3R' # application secret key
OAUTH_TOKENS_TWITTER_USERNAME = 'CMobileTrends' # user login
OAUTH_TOKENS_TWITTER_PASSWORD = 'devcmtrends' # user password

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cmtrends.urls'

WSGI_APPLICATION = 'cmtrends.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
