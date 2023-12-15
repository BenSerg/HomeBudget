import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('postgresql_logger')
logger.setLevel(logging.DEBUG)

file_handler = RotatingFileHandler('config/postgresql.log', mode='a', maxBytes=100000, backupCount=1)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
