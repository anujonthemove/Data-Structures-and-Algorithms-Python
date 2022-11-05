#!/bin/bash

echo 
echo --------------------------------------------------------------------------------
echo --------- Setting up Python Virtual Environment -------------
echo --------------------------------------------------------------------------------
echo 

# create a .env file from .env-template file
if [ -f ".env-template" ] && [ ! -f ".env" ]; then
    cp .env-template .env
fi

# create a virtual environment named .venv
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

# activate the newly created virtual environment
source .venv/bin/activate

# Test this first before uncommenting
# python -m pip config --site set install.user false
# python -m pip config --site set global.disable-pip-version-check false

# uncomment the code below, in case you trying to access pypi through a gateway behind a company firewall

# export $(grep -v '^#' .env | xargs)
#python -m pip install --upgrade pip -i https://$JFROG_USERNAME:$JFROG_API_KEY@amat-jfrog.amat.com/artifactory/api/$JFROG_REPOSITORY
#pip install pipenv -i https://$JFROG_USERNAME:$JFROG_API_KEY@amat-jfrog.amat.com/artifactory/api/$JFROG_REPOSITORY

# upgrade .venv python-pip
python -m pip install --upgrade pip

# install pipenv
pip install pipenv

if [[ "$1" == "--dev" ]]; then
	pipenv install --dev
    
    # uncomment to use detect-secrets pre-commit hook
	# if [ ! -f ".secrets.baseline" ]; then
	# 	detect-secrets scan >.secrets.baseline
	# fi
	# pre-commit install

else
	pipenv install
fi