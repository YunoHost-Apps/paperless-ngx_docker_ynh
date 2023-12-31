"""
    WSGI config
"""
import os

# DJANGO_SETTINGS_MODULE set via common.env usage in docker-compose.yml
assert os.environ['DJANGO_SETTINGS_MODULE'], f'{os.environ["DJANGO_SETTINGS_MODULE"]=}'


from django.core.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
