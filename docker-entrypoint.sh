#!/bin/bash

# wait for postgres to start up
sleep 2s 

# collect static files
python manage.py collectstatic --noinput

# apply database migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Prepare log files and start outputting logs to stdout
mkdir -p /src/logs/

touch /src/logs/gunicorn.log
touch /src/logs/access.log
tail -n 0 -f /src/logs/*.log &

echo Starting runserver
python manage.py runserver 0.0.0.0:8080

# # Start Gunicorn processes
# echo Starting Gunicorn.

# exec gunicorn collier.wsgi:application -n gwi_api -b 0.0.0.0:8080 --workers 3 --log-level=info --log-file=/src/logs/gunicorn.log --access-logfile=/src/logs/access.log
