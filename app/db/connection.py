import logging
from logging import config

import psycopg2

config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
logger = logging.getLogger("connection_logger")


def connect(db_name: str, db_user: str, db_password: str, db_host: str) -> psycopg2.extensions.connection:
    """
    Connects to the specified database and returns the connection object.

    Args:
        db_name (str): The name of the database.
        db_user (str): The username for the database.
        db_password (str): The password for the database user.
        db_host (str): The location or hostname where the database is hosted.

    Raises:
        psycopg2.DatabaseError: If there is an error connecting to the database.
        KeyError: If there is a key error while connecting to the database.

    Returns:
        psycopg2.extensions.connection: A connection object to the database.
    """
    try:
        with psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
        ) as connection:
            return connection
    except (psycopg2.DatabaseError, KeyError) as e:
        logger.error(e)
        raise e
