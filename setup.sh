#!/bin/bash

FOLDER=test
PROJECT=project 
APP=app

# make sure os is up to date
sudo apt-get update -y
sudo apt-get install -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt install net-tools -y

python3 -m 
# install os dependencies
sudo apt-get install python3-pip
pip3 install --upgrade pip

sudo pip3 install virtualenv
cd /$FOLDER


#create a .gitignore and ignore a future virtual environment
rm .gitignore
touch .gitignore
echo "*.pyc
venv/
.vscode/
" >> .gitignore


# Create a virtual environment and create requirements txt for future
virtualenv venv -p python3
source venv/bin/activate
REQUIREMENTS=/$FOLDER/requirements.txt
if test -f "$REQUIREMENTS"; then
    echo "$REQUIREMENTS exists."
    pip3 install -r requirements.txt
else 
    echo "$REQUIREMENTS does not exist."
    pip3 install django
    pip3 install djangorestframework
    pip3 install django-bootstrap4
    pip3 install django-crispy-forms
    pip3 install Pillow
    pip3 freeze > requirements.txt
fi
deactivate

django-admin startproject project
cd project
django-admin startapp app


# I . Install ap to main project
# Go to projects | Setting.py | add "app" to INSTALLED_APPS
# Check IP on IFCONFIG and add IP to ALLOWED_HOSTS in settings.py


# create url.py in app
# Go to projects | url.py | add  "app" add "from app import views"


# Run on port 80 on 0.0.0.0 not on Localhost if running on remote server
python3 manage.py migrate #initializes sql lite 3
python3 manage.py createsuperuser # create user for the admin console
python3 manage.py runserver 0.0.0.0:80

#Once Modal has been migrated
python3 manage.py makemigrations
python3 manage.py migrate


