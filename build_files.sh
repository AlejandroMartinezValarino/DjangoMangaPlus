#!/bin/bash

/usr/bin/pip install -r requirements.txt

/usr/bin/python3.9 manage.py collectstatic --noinput
