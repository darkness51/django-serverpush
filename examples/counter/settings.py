# Django settings for counter project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'counter.sqlite',			   # Or path to database file if using sqlite3.
		'USER': '',							 # Not used with sqlite3.
		'PASSWORD': '',						 # Not used with sqlite3.
		'HOST': '',							 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',							 # Set to empty string for default. Not used with sqlite3.
	}
}

# Serverpush settings!
SERVERPUSH_PORT = 8013
SERVERPUSH_NOTIFIER_PORT = 8014
SERVERPUSH_GLOBALS = (

)

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '&*f=tl-k_6o9lwglsfgbrp6h9dpjgmbyxuvy(p6m36tvow%m*g'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (

)

TEMPLATE_CONTEXT_PROCESSORS = (
	'serverpush.client.context_processor',
)

ROOT_URLCONF = 'counter.urls'

TEMPLATE_DIRS = (
	'templates',
)

INSTALLED_APPS = (
	'django.contrib.staticfiles',
	'serverpush',
	'counter.demoapp',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}
