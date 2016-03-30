"""
Script I use to create new Heroku applications with the following features:
	- Basic implementation of default Django authentication views
	- Dictionary of basic Bootstrap3 templates to choose from
	- Heroku apps named PROJECT_NAME and dev-PROJECT_NAME configured in a pipeline
	- Each app has its own Postgres database with the auth models automatically migrated
	- User is prompted to set up first superuser for each application
	- App PROJECT_NAME is set to auto-deploy from Github master branch
	- App dev-PROJECT_NAME is set to auto-deply from Github dev-master branch
	- All loacl git configuration is automated
	- Virtual environment is created and template packages automatically installed

There are few manual inputs and manipulations required (e.g. superuser input,
some CMD-F on the html templates as the Django template engine wasn't playing
nice, copy/pasting local DATABASE_URL and SECRET_KEY values into the
local_settings.py file, pointing Heroku apps at the right Github branches).

The whole process takes less than 10 minutes.
"""

import os
import random
import shutil
import sys

section = '**********************************************************************'

def continue_when_ready():
	ready = False
	while not ready:
		response = input("Type 'ready' to continue: ")
		if response.lower() == 'ready':
			ready = True
		if not ready:
			print('Try again...')

# Confirm script is being run from the correct location
cwd = os.getcwd()
if cwd != '/Users/Scott/projects':
	print('You are currently at ', cwd)
	print('Script must be run from /Users/Scott/projects')
	sys.exit('Script terminated')

# Prompt user for project name with reminder to check availability on Heroku
print('Check Heroku to confirm project name availability.')
print('When you are ready, enter the project name to continue.')
project_name = input('Project name: ')

# Show list of templates with short description for user selection
print(section)
temps = {
	1:{
		'name': 'Blank Slate',
		'description': 'Basic implementation of default Django auth with basic Bootstrap navbar',
		'github_url': 'https://github.com/se42/djroku-temp1/archive/master.zip',
	},
	# 2:{
	# 	'name': 'Another TBD template',
	# 	'description': 'TBD description',
	# 	'github_url': 'TBD url',
	# },
}

for key in sorted(temps.keys()):
	print(key, ' -- ', temps[key]['name'], ' -- ', temps[key]['description'])
temp = int(input('Enter the number of the template you want to use: '))
print(section)

# Make base project directory and move into it
print('Setting up directories...')
os.mkdir(os.path.join(cwd, '{0}/'.format(project_name)))
os.chdir('{0}'.format(project_name))

## TEMPLATE CONFIGURATION
print(section)
# Run djroku.sh script to set up virtual environment and install template packages
os.system('../myutils/djroku.sh {0} {1}'.format(temps[temp]['github_url'], project_name))
print(section)
# Unfortunately have to manually edit html templates
print('We need to manually edit the html templates.')
print('All html files in the templates/ directory should have opened automatically.')
print('CMD-F each template and replace PROJECT_NAME with the project name: {0}'.format(project_name))
continue_when_ready()

## GIT CONFIGURATION
print(section)
print('Setting up git repositories...')
os.system('git init')
os.system('git add -A')
os.system('git commit -m "initial commit"')
print('Creating new repo named {0} in Github account {1}'.format(project_name, 'se42'))
# shell script for curl command to create Github repository
os.system('../myutils/gitcreate.sh {0} {1}'.format(project_name, 'se42'))
# configure remotes and branches
os.system('git remote add origin https://github.com/se42/{0}.git'.format(project_name))
os.system('git push -u origin master')
os.system('git checkout -b dev-master')
os.system('git push -u origin dev-master')
print('Git repository setup complete.  Local machine is on branch dev-master')

## HEROKU CONFIGURATION
print(section)

def secret_key_gen():
	return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

os.system('heroku create {0}'.format(project_name))
os.system('heroku config:set --app {0} SECRET_KEY="{1}"'.format(project_name, secret_key_gen()))
os.system('heroku create dev-{0}'.format(project_name))
os.system('heroku config:set --app dev-{0} SECRET_KEY="{1}"'.format(project_name, secret_key_gen()))

# make new pipeline project_name
os.system('heroku pipelines:create {0} --app {1} --stage production'.format(project_name, project_name))
os.system('heroku pipelines:add {0} --app dev-{1} --stage staging'.format(project_name, project_name))
os.system('heroku pipelines:open {0}'.format(project_name))
print(section)
print('Use the Heroku dashboard that just opened to connect {0}'.format(project_name))
print('to the master branch of the {0} repository and to connect'.format(project_name))
print('dev-{0} to the dev-master branch of the {1} repository.'.format(project_name, project_name))
print('and also hit the deploy button for each app to deploy')
print('the appropriate branch.')
print()
print('Do not continue until both are successfully deployed.')
continue_when_ready()
print(section)

# migrate databases
os.system('heroku run --app {0} python manage.py migrate'.format(project_name))
os.system('heroku run --app dev-{0} python manage.py migrate'.format(project_name))
print(section)

# setup superusers (will require user input)
os.system('heroku run --app {0} python manage.py createsuperuser'.format(project_name))
os.system('heroku run --app dev-{0} python manage.py createsuperuser'.format(project_name))

# copy local_settings_template.py into local_settings.py in the project directory and open
shutil.copy('../myutils/local_settings_template.py', '{0}/local_settings.py'.format(project_name))
os.system('open {0}/local_settings.py'.format(project_name))
print(section)

# get dev-app DATABASE_URL and generate local secret key for local_settings.py file
print('DATABASE_URL for dev-{0}:'.format(project_name))
os.system('heroku config:get --app dev-{0} DATABASE_URL'.format(project_name))
print('SECRET_KEY for local development:')
print(secret_key_gen())
print()
print('Copy/paste those two values into the local_settings.py file that just opened.')
continue_when_ready()
os.system('heroku apps:open --app {0}'.format(project_name))
os.system('heroku apps:open --app dev-{0}'.format(project_name))
print(section)
print("You're ready to go!")

