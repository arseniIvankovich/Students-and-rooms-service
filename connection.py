import psycopg2
import os
from dotenv import load_dotenv
import logging
import logging.config

load_dotenv()
logging.config.fileConfig('logging.conf', disable_existing_loggers=True, encoding=None)
connection_logger = logging.getLogger('connection_logger')


def connect():
    try:
        with psycopg2.connect(database=os.getenv("DATABASE_NAME"), user= os.getenv("DATABASE_USER"), 
                                password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST")) as connection:
            return connection
    except (psycopg2.DatabaseError, Exception) as e:
        connection_logger.error(e)
            
