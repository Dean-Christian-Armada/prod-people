"""
Django settings for people project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# START Searchable Sections
# Use control+f and type these words below
    # INSTALLED_APPS
    # MIDDLEWARE
    # TEMPLATES
    # DATABASES
    # STATIC
    # MEDIA
    # CKEDITOR
    # DJANGO SESSION SECURITY
    # LOG
    # DJANGO DEFENDER
# END Searchable Sectons

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# Enables logging and used as to database Insert, Update and Delete logs in the project
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_7ev-nc(c*@j605%5r7*mtzw)o2&refw(u7qkm72@#-rz535!w'

# SECURITY WARNING: don't run with debug turned on in production!
# Please take note that 'session_security' app forces this as False on the server
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    # START django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # END django built-in apps
    # START third-party packages app
    'session_security',
    'jsignature',
    'widget_tweaks',
    'ckeditor',
    'wkhtmltopdf',
    'report_builder',
    'defender',
    'import_export',
    'autocomplete_light',
    # 'swampdragon', # django real-time app using redis, currently not used for priority and implementation reasons
    # END third-party packages app
    # START django manage.py built apps
    'login',
    'application_form',
    'mariners_profile',
    'application_profile',
    'cms',
    'notifications',
    'company_staffs',
    # 'people', # this was used during database presentation with Mike Kennedy separating the redundancy tables
    # END django manage.py built apps
    # START extra-apps
    'globals_declarations',
    # END extra-apps
    
)

MIDDLEWARE_CLASSES = (
    # START django built-in middlewares
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # END django built-in middlewares
    # START third-party middlewares
    'defender.middleware.FailedLoginMiddleware'
    # END third-party middlewares
    # START custom-built middlewares
    # END custom-built middlewares
)

ROOT_URLCONF = 'people.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'people.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'people',
        # 'USER': 'root',
        # 'PASSWORD': 'd3@narmada13',
        # 'HOST': 'localhost',
        # 'PORT': 80,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# Set to False because of pytz conflict on django-defender package
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# collectstatic is used when deploying in sub-domain server of Manship like people.manship.com to enable the css of admin and others that are defined bia module
# UNCOMMENT STATIC ROOT to run collectstatic
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# COMMENT STATIC_PATH to run collecstatic
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# COMMENT STATICFIELS_DIRS to run collecstatic
STATICFILES_DIRS = (STATIC_PATH, )

# START CUSTOM EMAIL CONFIGURATIONS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'deanarmada@gmail.com'
EMAIL_HOST_PASSWORD = 'd3@narmada13'
DEFAULT_FROM_EMAIL = 'deanarmada@gmail.com'
DEFAULT_TO_EMAIL = 'deanarmada@gmail.com'

LOGIN_URL = '/?error=Session Expired, Please login again'
# END CUSTOM EMAIL CONFIGURATIONS

# START SwampDragon settings
# try:
#     SWAMP_DRAGON_CONNECTION = ('swampdragon.connections.sockjs_connection.DjangoSubscriberConnection', '/data')
#     DRAGON_URL = 'http://localhost:9999/'
# except:
#     pass
# END SwampDragon settings

# Used in defining date formats
# Syntax tells that the defined date formats file is in /formats/en/formats.py 
FORMAT_MODULE_PATH = [ 'formats', ]

# START CKEDITOR Configurations
# To enable complete toolbar capabilities of ckeditor
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': None,
#     },
# }


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
                        ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                        ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                        ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'],
                    ],
    },
}
# END CKEDITOR Configurations

# START DJANGO SESSION SECURITY SETTINGS
# SESSION_SECURITY_WARN_AFTER = 10
# SESSION_SECURITY_EXPIRE_AFTER = 20
SESSION_SECURITY_WARN_AFTER = 9000
SESSION_SECURITY_EXPIRE_AFTER = 9100
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SECURITY_ACTIVE_URLS = [ "/application-form/", ]
# END DJANGO SESSION SECURITY SETTINGS

# START LOG every CRUD query on a logfile named db.log
# Source: http://stackoverflow.com/questions/5739830/simple-log-to-file-example-for-django-1-3

# Filter Object custom Class
# Source: http://www.lexev.org/en/2013/django-logging-settings/
class CustomQueryFilter(logging.Filter):
    def filter(self, record):
        for action in ['INSERT', 'UPDATE', 'DELETE']:
            if action in getattr(record, 'sql', ''):
                return True
        return False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'db_query_filter':{
            '()': CustomQueryFilter,
        },
    },
    'handlers': {
        # Nulled because it produces in Django1.9 
        # 'null': {
        #     'level':'DEBUG',
        #     'class':'django.utils.log.NullHandler',
        # },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/db.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
            'filters': ['db_query_filter'],
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
# END LOG every CRUD query on a logfile named db.log


# START DJANGO-DEFENDER settings
# DEFENDER_USERNAME_FORM_FIELD = "username"
# END DJANGO-DEFENDER settings