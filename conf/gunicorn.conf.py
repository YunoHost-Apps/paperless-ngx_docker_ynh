"""
    Configuration for Gunicorn
"""
import multiprocessing


bind = '0.0.0.0:8000'


# https://docs.gunicorn.org/en/latest/settings.html#workers
workers = multiprocessing.cpu_count() + 1


# https://docs.gunicorn.org/en/latest/settings.html#logging
loglevel = '__LOG_LEVEL__'


# https://docs.gunicorn.org/en/latest/settings.html#logging
accesslog = '-'  # to stdout
errorlog = '-'  # to stderr
