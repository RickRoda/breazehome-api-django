#!/bin/bash

# Give time for the DB to start

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn breaze.wsgi:application \
    --name breaze \
    --bind 0.0.0.0:8080 \
    --workers 8 \
    --log-level=debug \
    --error-logfile - \
    --log-file - \
    "$@"
