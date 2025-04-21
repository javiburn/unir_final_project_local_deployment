#!/bin/bash
# Requires the database to be up
#FLASK_ENV=development DATABASE_URI=postgresql://myuser:mypassword@db:5432/mydatabase python run.py
pytest --cov=app --cov-fail-under=80
