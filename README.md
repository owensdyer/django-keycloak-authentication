# Django Keycloak Authentication
Django web application using Keycloak for the user authentication containerised by Docker.

## Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Resources](#resources)
- [Frequently asked questions](#frequenty-asked-questions)

## Requirements
- Python 3
- Keycloak 24

This project has been tested on:
- Python 3.12.3
- Keycloak 24.0.1

## Installation
1. Download this repository to a directory of choice
2. Open your console and navigate to the directory where the repository was downloaded to
3. Create a virual environment
    ```
    python -m venv venv
    ```
4. Active your virtual environment (important)
    ```
    ./venv/Scripts/activate
    ```
5. Install packages
    ```
    pip install -r requirements.txt
    ```
6. Create a superuser to access Django admin site
    ```
    python manage.py createsuperuser
    ```
7. Configure the settings.py file with your Keycloak configuration
8. Run the django web server
    ```
    python manage.py runserver
    ```
9. Go to `accounts/login` and keycloak should be displayed if configured correctly


## Resources
- [Keycloak documentation](https://www.keycloak.org/documentation)
- [Allauth documentation](https://docs.allauth.org/en/latest)

## Frequenty asked questions
### Keycloak doesn't display on login screen.
There are a few reasons why this may happen.
#### Missing required packages
Make sure that all [packages](#requirements) are installed.
#### Mis-configured settings.py
To enable the soical login for Keycloak, you need to make sure that `SOCIALACCOUNT_ENABLED = True`

### Login redirect wrong
In the settings.py file, change the path of the `LOGIN_REDIRECT_URL`.