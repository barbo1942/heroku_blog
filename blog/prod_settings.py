from .settings import *
import dj_database_url

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTTP_X_FORWARDED_PROTO','https')

STATIC_ROOT = 'staticfiles'

DATABASE = {
  'default': dj_database_url.config()
}

ALLOWED_HOSTS= ['*']