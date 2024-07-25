from .base import *

DEBUG = False

SECRET_KEY = 'your-production-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'your-database-host',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['example.com', 'example2.com']

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

