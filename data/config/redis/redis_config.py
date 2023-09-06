import os

from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

REDIS_HOST = os.getenv('PREDIS_HOST')
REDIS_PORT = 6379
REDIS_DB = 1
