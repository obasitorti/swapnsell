#!/bin/bash
python manage.py migrate --no-input
gunicorn baseapp.wsgi --log-file -