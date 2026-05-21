# Fii Verde — Django Web Application

Web platform for recyclable paper container management and monitoring.

The application allows users to:
- create an account;
- authenticate;
- save their recycling container address;
- view their location on a map;
- change container status (full / empty);
- administrators can monitor all containers on a global map.

---

# Technologies Used

## Backend
- Python 3.13
- Django 5

## Frontend
- HTML5
- CSS3
- JavaScript

## Database
- SQLite3

## Maps & Geolocation
- Leaflet.js
- OpenStreetMap
- Nominatim API

## Deployment
- Microsoft Azure App Service
- Gunicorn
- WhiteNoise
- GitHub Actions

---

# Recommended Python Version

Python 3.13

---

# One Time Setup

## Install pipenv

pip install pipenv

## Install dependencies

pipenv install

or manually:

pip install django
pip install requests
pip install gunicorn
pip install whitenoise

---

# Activate Virtual Environment

Windows:

venv\Scripts\activate

---

# Run Server

python manage.py runserver

Local URL:

http://127.0.0.1:8000

---

# Database Commands

python manage.py migrate

python manage.py makemigrations

python manage.py createsuperuser

---

# Azure Deployment

Startup Command:

bash startup.sh

startup.sh:

#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn --bind=0.0.0.0 --timeout 600 mase_neagu_andronic.wsgi

---

# Main Functionalities

- User registration
- Authentication
- Dashboard
- Interactive map
- Container management
- Admin monitoring
- Address geolocation

---

# Notes

- SQLite used for educational purposes.
- Hosted using Azure App Service.
- GitHub Actions used for CI/CD deployment.
