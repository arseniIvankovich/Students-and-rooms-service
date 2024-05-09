"""_summary_

    Returns:
        _type_: _description_
"""
import logging
import os
from logging import config

import psycopg2
from db.connection import connect
from db.repository_interface import IRepository
from dotenv import load_dotenv

load_dotenv()

config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
queries_logger = logging.getLogger("queries_logger")


class SQLRepository(IRepository):
    """_summary_

    Args:
        IRepository (_type_): _description_
    """

    def __init__(self, connection: psycopg2.extensions.connection):
        self._connection = connection

    def insert_rooms(self, items):
        try:
            with self._connection.cursor() as cursor:
                cursor.executemany(
                    'INSERT INTO "Rooms" (id, room) \
                                    VALUES (%s, %s);',
                    items,
                )
                self._connection.commit()
        except psycopg2.Error as e:
            queries_logger.error(e)
            return None

    def insert_students(self, items):
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
            queries_logger.error(e)
            return None

    def get_rooms_students_count(self):
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
            queries_logger.error(e)

    def get_rooms_with_different_sex(self):
        try:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    'SELECT rooms.room FROM "Rooms" AS rooms \
                                LEFT JOIN "Students" AS students ON students.room = rooms.id \
                                GROUP BY rooms.room HAVING COUNT(DISTINCT sex) > 1'
                )
                return cursor.fetchall()
        except psycopg2.Error as e:
            queries_logger.error(e)
            return None

    def get_five_rooms_with_least_age_average(self):
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
            return None

    def get_five_rooms_with_largest_age_differnce(self):
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
            queries_logger.error(e)
            return None

    def create_index_on_rooms(self):
        try:
            with self._connection.cursor() as cursor:
                cursor.execute('CREATE INDEX IF NOT EXISTS rooms_index ON "Rooms" (room);')
                self._connection.commit()
        except psycopg2.Error as e:
            queries_logger.error(e)
            return None
