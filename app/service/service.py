"""
Service class provides methods to interact with a PostgreSQL database through SQLRepository.
"""
import json
import logging
import os
from logging import config

import db.sql_repository
from dateutil import parser

config.fileConfig("logging.conf", disable_existing_loggers=True, encoding=None)
logger = logging.getLogger("service_logger")


class Service:
    """
    Service class provides methods to interact with a PostgreSQL database through SQLRepository.
    """

    def __init__(self, repository: db.sql_repository.SQLRepository) -> None:
        self._repository = repository

    def insert_rooms(self, filepath: str) -> None:
        """
        Inserts room data into the database from a JSON file.
        Method call SQLRepository method to insert data.

        Args:
            filepath (str): The path to the JSON file containing room data.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified file cannot be found.
            json.JSONDecodeError: If the file cannot be decoded as JSON.
        """

        try:
            with open(filepath, encoding="utf-8") as file:
                items = [(i["id"], i["name"]) for i in json.load(file)]
                self._repository.insert_rooms(items)

        except FileNotFoundError as e:
            logger.error(f"File not found: {filepath}")
            raise e
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON file: {filepath}")
            raise e

    def insert_students(self, filepath: str) -> None:
        """
        Inserts student data into the database from a JSON file.
        Method call SQLRepository method to insert data.


        Args:
            filepath (str): The path to the JSON file containing student data.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified file cannot be found.
            json.JSONDecodeError: If the file cannot be decoded as JSON.
        """

        try:
            with open(filepath, encoding="utf-8") as file:
                items = [
                    (
                        i["id"],
                        str(parser.parse(i["birthday"])),
                        i["name"].split()[0],
                        i["name"].split()[1],
                        i["room"],
                        i["sex"],
                    )
                    for i in json.load(file)
                ]
                self._repository.insert_students(items)

        except FileNotFoundError as e:
            logger.error(f"File not found: {filepath}")
            raise e
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON file: {filepath}")
            raise e

    def get_rooms_students_count(self, filename: str) -> list[tuple]:
        """
        Retrieves the count of students in each room from the database
        and saves the result to a JSON file. Method call SQLRepository method to get data.

        Args:
            filepath (str): The name of the JSON file by which it will be saved.

        Returns:
            list[tuple]: A list of tuples containing room IDs and the count of students.
        """

        items = self._repository.get_rooms_students_count()
        list_to_json = [{"room": i[0], "amount": i[1]} for i in items]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)
        return items

    def get_rooms_with_mixedSex_students(self, filename: str) -> list[tuple]:
        """
        Retrieves rooms where students of different sexes live from the database
        and saves the result to a JSON file. Method call SQLRepository method to get data.

        Returns:
            list[tuple]: A list of tuples containing room IDs.

        Args:
            filepath (str): The name of the JSON file by which it will be saved.

        Raises:
            FileNotFoundError: If the specified file path cannot be found.
            psycopg2.Error: If an error occurs while executing the SQL query.
        """

        items = self._repository.get_rooms_with_mixedSex_students()
        list_to_json = [{"room": i[0]} for i in items]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)
        return items

    def get_five_rooms_with_smallest_age_average(self, filename: str) -> list[tuple]:
        """
        Retrieves the five rooms with the least average age of students who lives in the same room
        from the database and saves the result to a JSON file. Method call SQLRepository method to get data.

        Args:
            filepath (str): The name of the JSON file by which it will be saved.

        Returns:
            list[tuple]: A list of tuples containing room IDs.
        """

        items = self._repository.get_five_rooms_with_smallest_age_average()
        list_to_json = [{"room": i[0]} for i in items]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)
        return items

    def get_five_rooms_with_largest_age_differnce(self, filename: str) -> list[tuple]:
        """
        Retrieves the five rooms with the largest age difference among students who lives in the same room
        from the database and saves the result to a JSON file. Method call SQLRepository method to get data.

        Args:
            filepath (str): The name of the JSON file by which it will be saved.

        Returns:
            list[tuple]: A list of tuples containing room IDs.
        """
        items = self._repository.get_five_rooms_with_largest_age_differnce()
        list_to_json = [{"room": i[0]} for i in items]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(list_to_json, file, indent=4)
        return items

    def create_index_on_rooms(self) -> None:
        """
        CCreates an index on the 'Rooms' table on the 'room' field in the database.
        Method call SQLRepository method to create the index.

        Returns:
            None
        """
        return self._repository.create_index_on_rooms()
