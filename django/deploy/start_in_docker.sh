#!/usr/bin/env bash

export PGPASSWORD=somepass

until psql -h "db" -U "project" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

sudo /etc/init.d/nginx start;

export DJANGO_SETTINGS_MODULE=project.settings_production;

python3 manage.py migrate --noinput;

uwsgi --socket /tmp/uwsgi.sock --module project.wsgi --chmod-socket=777 --processes=10;

while true; do
sleep 300
done
