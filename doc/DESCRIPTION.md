[![tests](https://github.com/YunoHost-Apps/docker_django_example_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/docker_django_example_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/docker_django_example_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/docker_django_example_ynh)
[![docker_django_example_ynh @ PyPi](https://img.shields.io/pypi/v/docker_django_example_ynh?label=docker_django_example_ynh%20%40%20PyPi)](https://pypi.org/project/docker_django_example_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/docker_django_example_ynh)](https://github.com/YunoHost-Apps/docker_django_example_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/docker_django_example_ynh)](https://github.com/YunoHost-Apps/docker_django_example_ynh/blob/main/LICENSE)

A example YunoHost App that package a Python/Django via Docker.

Notes:

 * Use docker-compose from Debian repository (installed by manifest v2 `[resources.apt]` section)
 * Add tree containers:
   * The Web App container with the Django project
   * Postgres
   * Redis
 * Use SystemD service file to start the Docker container
 * Use YunoHost system nginx as proxy
 * Postgres database:
   * Store database files under `__DATA_DIR__` in: `/home/yunohost.app/$app/volumes/postgresql-data/`
   * Run Postgres as "App user/group" (So database files are owned by app user)
 * Serve static files from system nginx (From: `__INSTALL_DIR__` -> `/var/www/$app/`)


Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)
