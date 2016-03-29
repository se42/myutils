#! /bin/bash
GITHUB_URL=$1
PROJECT_NAME=$2

echo "Creating virtual environment..."
python3 -m venv env
source env/bin/activate
echo "Virual environment activated..."
echo "Upgrading pip..."
pip install -U pip
echo "Installing Django..."
pip install django
echo "Starting Django project from template..."
django-admin startproject --template=$GITHUB_URL --extension=py,md --name=Procfile $PROJECT_NAME .
echo "Installing template project requirements..."
pip install -r requirements.txt
echo "Deactivating virtual environment..."
deactivate

for d in templates/*/
do
	for f in $d/*.html
	do
		open $f
	done
done

echo "Done."