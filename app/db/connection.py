"""_summary_

    Returns:
        _type_: _description_
"""

import logging
from logging import config

import psycopg2

config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
connection_logger = logging.getLogger("connection_logger")


def connect(db_name: str, db_user: str, db_password: str, db_host: str) -> psycopg2.extensions.connection:
    """_summary_

    Returns:
        _type_: _description_
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
        connection_logger.error(e)
        raise e
