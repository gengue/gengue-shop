# -*- coding: utf-8 -*-

from .common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'domain_info'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = 'info@domain.com.co'
SERVER_EMAIL = 'info@domain.com.co'


INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

