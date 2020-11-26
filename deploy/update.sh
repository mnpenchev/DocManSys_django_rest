#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/DocManSys_django_rest'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart DocManSys_django_rest

echo "DONE! :)"
