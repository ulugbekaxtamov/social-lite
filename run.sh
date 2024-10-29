#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Fake Posts for demo
#python manage.py create_post

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi
