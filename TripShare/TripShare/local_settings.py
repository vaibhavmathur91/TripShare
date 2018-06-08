from .settings import *
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tripshare-db')
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_URL

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_URL

# Organisation
ORGANISATION_NAME = 'TripShare'
ORGANISATION_REPLY_TO_EMAIL = 'vaibhav09121991@gmail.com'
ORGANISATION_FROM_EMAIL = 'vaibhav09121991@gmail.com'


path_1 = os.getcwd() + r'/static'
STATICFILES_DIRS = (path_1, )
TEMPLATE_CONTEXT_PROCESSORS = ['django.core.context_processors.static', ]

# Auth urls
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/home/'
