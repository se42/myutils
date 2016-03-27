import os

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
# set SECRET_KEY and DEV_DB_URL as strings
SECRET_KEY = None
DEV_DB_URL = None

def set_local_env_variables():
	os.environ['SECRET_KEY'] = SECRET_KEY
	os.environ['DATABASE_URL'] = DEV_DB_URL


####################
### HEROKU NOTES ###
####################

## DATABASE MIGRATIONS
# heroku apps		to list app names
# heroku run --app APP_NAME bash		to launch one-off dyno for running migrations
