#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python b_test_task/manage.py migrate

# Start server
echo "Starting server"
python b_test_task/manage.py runserver 0.0.0.0:8000