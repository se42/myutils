import os
import subprocess as sp
import sys
import venv

section = '**********************************************************************'

# Confirm script is being run from the correct location
cwd = os.getcwd()
if cwd != '/Users/Scott/projects':
	print('You are currently at ', cwd)
	print('Script must be run from /Users/Scott/projects')
	sys.exit('Script terminated')

# Show list of templates with short description for user selection
temps = {
	1:{
		'name': 'Blank Slate',
		'description': 'Basic implementation of default Django auth with basic Bootstrap navbar',
		'github_url': 'https://github.com/se42/djroku-temp1/archive/master.zip',
	},
	2:{
		'name': 'Another TBD template',
		'description': 'TBD description',
		'github_url': 'TBD url',
	},
}

for key in sorted(temps.keys()):
	print(key, ' -- ', temps[key]['name'], ' -- ', temps[key]['description'])
temp = int(input('Enter the number of the template you want to use: '))
print(section)

# Prompt user for project name with reminder to check availability on Heroku
print('Check Heroku to confirm project name availability.')
print('When you are ready, enter the project name to continue.')
project = input('Project name: ')
print(section)

# Make base project directory and move into it
print('Setting up directories...')
os.mkdir(os.path.join(cwd, '{0}/'.format(project)))
os.chdir('{0}'.format(project))

# Run djroku.sh script to set up virtual environment and install packages
os.system('../myutils/djroku.sh {0} {1}'.format(temps[temp]['github_url'], project))
print(section)
# Manually edit html templates.  CMD-F to find PROJECT_NAME and replace with the actual project name
print('We need to manually edit the html templates.')
print('All html files in the templates/ directory should have opened automatically.')
print('CMD-F each template and replace PROJECT_NAME with the project name: {0}'.format(project))

ready = False
while not ready:
	response = input("Type 'ready' to continue: ")
	if response.lower() == 'ready':
		ready = True
	if not ready:
		print('Try again...')

print(section)
print('Setting up git repositories...')
os.system('git init')
os.system('git add -A')
os.system('git commit -m "initial commit"')
os.system('../myutils/gitcreate.sh')
os.system('git push -u origin master')
os.system('git checkout -b dev-master')
os.system('git push -u origin dev-master')
print('Git repository setup complete.  Local machine is on branch dev-master')
print(section)
print('Now for Heroku setup!')
# heroku create PROJECT_NAME
# heroku create dev-PROJECT_NAME
# pause to do the following
# open app and set SECRET_KEY config variables in heroku app
# point heroku apps at corresponding git branch and set auto deploys
# hit the button to deploy both apps to Heroku from Github
# wait for both to finish
# press key to continue when done
# heroku run --app PROJECT_NAME python manage.py migrate
# heroku run --app PROJECT_NAME python manage.py createsuperuser
# heroku run --app dev-PROJECT_NAME python manage.py migrate
# heroku run --app dev-PROJECT_NAME python manage.py createsuperuser
# function to copy local_settings_template.py into PROJECT_NAME/PROJECT_NAME/local_settings.py
#	but require user to enter a SECRET_KEY (not the production one!) and the DB_URL so
#	they can be automatically updated
# cp projects/myutils/local_settings_template.py projects/PROJECT_NAME/PROJECT_NAME/local_settings.py
# echo "You're ready to go!"















