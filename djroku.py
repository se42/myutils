import os
import subprocess as sp
import sys
import venv

import sh


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
print('The templates/ directory should have opened automatically.')
print('CMD-F each template and replace PROJECT_NAME with the actual project name.')

ready = False
while not ready:
	response = input("Type 'ready' to continue: ")
	if response.lower() == 'ready':
		ready = True
	if not ready:
		print('Try again...')

print(section)
print('On to git and Heroku tomorrow!')















