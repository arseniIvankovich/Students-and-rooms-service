"""_summary_

    Returns:
        _type_: _description_
"""

import logging
import os
from logging import config

import psycopg2
from dotenv import load_dotenv

load_dotenv()
config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
connection_logger = logging.getLogger("connection_logger")


def connect():
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        with psycopg2.connect(
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
        ) as connection:
            return connection
    except (psycopg2.DatabaseError) as e:
        connection_logger.error(e)
        return None
