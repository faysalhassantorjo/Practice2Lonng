#!/bin/bash

# Debugging output
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files for Django
python manage.py collectstatic --noinput
