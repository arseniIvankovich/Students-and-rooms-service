"""
SQLRepository class implements IRepository interface for interacting with a PostgreSQL database.
"""

import logging
from logging import config

import psycopg2
from db.abstract_repository import AbstractRepository
from dotenv import load_dotenv

load_dotenv()

config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
logger = logging.getLogger("queries_logger")


class SQLRepository(AbstractRepository):
    """
    SQLRepository class implements IRepository interface for interacting with a PostgreSQL database.

    Args:
        connection (psycopg2.extensions.connection): A connection to the PostgreSQL database.
    """

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        self._connection = connection

    def insert_rooms(self, items: list) -> None:
        """
        Inserts room data into the database.

        Args:
            items (list): A list of tuples containing room IDs and names.

        Returns:
            None

        Raises:
            psycopg2.Error: If an error occurs while executing the SQL query.
        """

        try:
            with self._connection.cursor() as cursor:
                cursor.executemany(
                    'INSERT INTO "Rooms" (id, room) \
                                    VALUES (%s, %s);',
                    items,
                )
                self._connection.commit()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def insert_students(self, items: list) -> None:
        """
        Inserts student data into the database.

        Args:
            items (list): A list of tuples containing student information including
                ID, birthday, first name, second name, room, and sex.

        Returns:
            None

        Raises:
            psycopg2.Error: If an error occurs while executing the SQL query.
        """

        try:
            with self._connection.cursor() as cursor:
                cursor.executemany(
                    'INSERT INTO "Students" (id, birthday, \
                                    first_name, second_name, room, sex) \
                                    VALUES (%s, %s, %s, %s, %s, %s);',
                    items,
                )
            self._connection.commit()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def get_rooms_students_count(self) -> list[tuple]:
        """
        Retrieves the count of students in each room from the database.

        Returns:
            list[tuple]: A list of tuples containing room IDs and the count of students.

        Raises:
            psycopg2.Error: If an error occurs while executing the SQL query.
        """

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    'SELECT rooms.room, COUNT(students.id) AS amount \
                                FROM "Rooms" AS rooms \
                                LEFT JOIN "Students" AS students ON students.room = rooms.id \
                                GROUP BY rooms.room ORDER BY amount DESC;'
                )
                return cursor.fetchall()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def get_rooms_with_mixedSex_students(self) -> list[tuple]:
        """
        etrieves rooms where students of different sexes live from the database.

        Returns:
            list[tuple]: A list of tuples containing room IDs.

        Raises:
            psycopg2.Error: If an error occurs while executing the SQL query.
        """

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    'SELECT rooms.room FROM "Rooms" AS rooms \
                                LEFT JOIN "Students" AS students ON students.room = rooms.id \
                                GROUP BY rooms.room HAVING COUNT(DISTINCT sex) > 1'
                )
                return cursor.fetchall()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def get_five_rooms_with_smallest_age_average(self) -> list[tuple]:
        """
        Retrieves the five rooms with the least average age of students who lives in the same room
        from the database.

        Returns:
            list[tuple]: A list of tuples containing room IDs.
        """

        try:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    'SELECT room FROM ( \
                                    SELECT rooms.room, ROUND(CAST(AVG(DATE_PART(\'year\', \
                                    AGE(birthday)))as numeric),2) AS avg_age \
                                    FROM "Rooms" AS rooms \
                                    LEFT JOIN "Students" AS students ON students.room = rooms.id \
                                    GROUP BY rooms.room ORDER BY avg_age \
                                    ) AS inner_query LIMIT 5;'
                )
                return cursor.fetchall()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def get_five_rooms_with_largest_age_differnce(self) -> list[tuple]:
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT room FROM ( \
                                SELECT rooms.room, DATE_PART('year', \
                                MAX(AGE(birthday))) - DATE_PART('year', MIN(AGE(birthday))) AS max_min_sub_age \
                                FROM \"Rooms\" AS rooms \
                                LEFT JOIN \"Students\" AS students ON students.room = rooms.id \
                                GROUP BY rooms.room ORDER BY max_min_sub_age DESC) AS inner_query LIMIT 5;"
                )
                return cursor.fetchall()
        except psycopg2.Error as e:
            logger.error(e)
            raise e

    def create_index_on_rooms(self) -> None:
        """
        Creates an index on the 'Rooms' table on the 'room' field in the database.

        Returns:
            None

        Raises:
            psycopg2.Error: If an error occurs while executing the SQL query
        """
        try:
            with self._connection.cursor() as cursor:
                cursor.execute('CREATE INDEX IF NOT EXISTS rooms_index ON "Rooms" (room);')
                self._connection.commit()
        except psycopg2.Error as e:
            logger.error(e)
            raise e
