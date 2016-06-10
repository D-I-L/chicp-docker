from projCHICP.settings_secret import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Z#3D;%0Fx0nF&?cwMKCBa6/1.awj7R{Dw9,W3ezvTy<T>UF__]~<@dkQkocwZxpCdAoo/nc|mnx9{aVQ/Dn_8R4/:q&l(VajqxZ<'

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'chicp',
    'elastic',
    'analytical',
    'pydgin_auth',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)



ROOT_URLCONF = 'projCHICP.urls'
WSGI_APPLICATION = 'projCHICP.wsgi.application'

AUTH_PROFILE_MODULE = "pydgin_auth.UserProfile"

TEMPLATES = [
       {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
	    'DIRS': [os.path.join(BASE_DIR, 'projCHICP/templates/')
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








# Import Application-specific Settings
BASE_HTML_DIR = 'chicp/'
PYDGIN_AUTH_APPS_BASE_NAME = 'pydgin_auth'
for app in INSTALLED_APPS:
    if app.startswith(PYDGIN_AUTH_APPS_BASE_NAME):
        try:
            app_module = __import__(app, globals(), locals(), ["settings"])
            app_settings = getattr(app_module, "settings", None)
            for setting in dir(app_settings):
                if setting == setting.upper():
                    locals()[setting] = getattr(app_settings, setting)
        except ImportError:
            pass

## comment out the databases section ##

STATIC_ROOT = os.path.join(PROJECT_DIR, 'apache')
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)

if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# writes all request logging from the django.request logger to a local file
LOG_FILE = os.path.join(BASE_DIR, 'tmp/apache.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 10,
            'filename': LOG_FILE,
            'formatter': 'verbose',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'elastic': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'data_pipeline': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'search_engine': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'pydgin_auth': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "projCHICP/static"),
)
STATIC_ROOT = os.path.join(PROJECT_DIR, 'apache')

if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
