from os import environ
from ast import literal_eval

from psycogreen.gevent import patch_psycopg


# Check this guide to optimize gunicorn WORKERS and WORKER CONNECTIONS
# https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
# workers = int(environ.get('GUNICORN_WORKERS', '3'))
# worker_class = 'gevent'
# Number of clients a worker can manage, this is: total_connections = workers * connections
# worker_connections = int(environ.get('GUNICORN_WORKER_CONNECTIONS', '100'))

timeout = int(environ.get('GUNICORN_TIMEOUT', '120'))
bind = '0.0.0.0:' + environ.get('PORT', '8000')

# Recommended by Heroku
# https://devcenter.heroku.com/articles/python-gunicorn#app-preloading
preload_app = literal_eval(environ.get('GUNICORN_PRELOAD_APP', 'False'))

# Max request by worker before automatically restarting
# http://docs.gunicorn.org/en/latest/settings.html#max-requests
# Could try it with 10000
max_requests = int(environ.get('GUNICORN_MAX_REQUESTS', '0'))

# Highly recommended if we set max requests
# This is intended to stagger worker restarts to avoid all workers restarting at the same time.
max_requests_jitter = int(environ.get('GUNICORN_MAX_REQUESTS_JITTER', '0'))

# Only support TSL v1.2 in order to avoid old browsers with untrusty certificates and well know issues
# ssl_version = 'TLSv1_2'

def post_fork(server, worker):
    ''' This patch psycopg to work with gevents '''
    patch_psycopg()
    worker.log.info("Made Psycopg2 Green")

