#!/bin/bash
echo "Creating virtual environment..."
python3.9 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput
