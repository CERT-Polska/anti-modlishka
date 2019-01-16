# see Flask-Session for docs on that
import os

from redis import Redis

SESSION_TYPE = 'redis'

# change to something random
SECRET_KEY = os.environ['SECRET_KEY']

# your real domain
LEGITIMATE_HOST = os.environ['LEGITIMATE_HOST']


SESSION_REDIS = Redis(host='redis', port=6379)
