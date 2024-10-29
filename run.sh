#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
    sleep 1
done
echo "Database is ready"


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
