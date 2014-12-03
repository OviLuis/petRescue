"""
Django settings for petRescue project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

#encoding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hni)5fd+&s9+tcuq)+v^nk1$u(06)%%*qgb5sdt9cw-uv!!g+j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DB = True

TEMPLATE_DEBUG = DEBUG


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mockups',
    'django_bootstrap_breadcrumbs',

    'principal',
    'web',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'petRescue.urls'

WSGI_APPLICATION = 'petRescue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DB:
    print "Depuracion"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    print "deployment"
    import dj_database_url
    DATABASES = { 'default': dj_database_url.config() }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#carga las imagenes de las mascotas
MEDIA_ROOT = os.path.join(BASE_DIR, 'carga')
MEDIA_URL = '/media/'

#templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'web/templates'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'web/static')
STATIC_URL = '/staticos/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


AUTH_USER_MODEL = 'principal.Usuario'

#TEMPLATE_CONTEXT_PROCESSORS = (
#    "django.core.context_processors.request",
#    "django.contrib.auth.context_processors.auth",
    ##Estaticos
#    "django.core.context_processors.static",
#)

#para heroku
# Parse database configuration from $DATABASE_URL

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


"""
FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler", )
"""

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',)


TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
'django.core.context_processors.request',
)