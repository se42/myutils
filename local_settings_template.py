"""
Template for local_settings.py file to be used during local
development of Heroku projects.  Production settings.py file
should be set up to access SECRET_KEY and DATABASE_URL as
environment variables.  Do a try/except to import set_local_env_variables
from local_settings.py and then run set_local_env_variables before
settings.py tries to access those variables, then do another
try/except at the bottom of settings.py to import * and thereby
override settings variables that need to be changed.
"""

import os

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False


def set_local_env_variables():
	# set KEY and DEV_DB_URL as strings
	os.environ['SECRET_KEY'] = None
	os.environ['DATABASE_URL'] = None


####################
### HEROKU NOTES ###
####################

## DATABASE MIGRATIONS
# heroku apps		to list app names
# heroku run --app APP_NAME bash		to launch one-off dyno for running migrations
