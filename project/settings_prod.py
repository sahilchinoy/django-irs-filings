import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config()