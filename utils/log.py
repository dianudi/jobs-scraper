import logging as log
from dotenv import load_dotenv
from os import getenv

load_dotenv()
level = log.INFO
if getenv('ENV') and getenv('ENV') == 'local':
    level = log.DEBUG
log.basicConfig(level=level)
