import os
from logging.config import fileConfig
import json

fileConfig('./logging_config.ini')

USE_ENV = False
DEGIRO_USERNAME = os.getenv('DEGIRO_USERNAME', '<SECRET>')
DEGIRO_PASSWORD = os.getenv('DEGIRO_PASSWORD', '<SECRET>')
if not USE_ENV:
    globals().update(json.load(open('./auth.json', 'rt')))