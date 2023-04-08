#!/bin/bash

if [[ "${APP_ENVIRONMENT}" == "production" ]]; then
    ./wait-for-it.sh db:5432 && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn -c config/gunicornconfig.py
elif [[ "${APP_ENVIRONMENT}" == "test" ]]; then
    ./wait-for-it.sh db:5432 &&  python manage.py test
else
    ./wait-for-it.sh db:5432 && python manage.py migrate && python manage.py runserver 0.0.0.0:8001 --settings=config.settings.local
fi
