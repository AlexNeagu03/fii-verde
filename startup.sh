#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn --bind=0.0.0.0 --timeout 600 mase_neagu_andronic.wsgi