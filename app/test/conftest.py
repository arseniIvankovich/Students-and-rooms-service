import os

import pytest
from db.connection import connect
from db.sql_repository import SQLRepository
from dotenv import load_dotenv
from service.service import Service

load_dotenv()


@pytest.fixture(scope="session", name="connection")
def get_connection():
    return connect(
        db_name=os.environ["DATABASE_NAME_TEST"],
        db_password=os.environ["DATABASE_PASSWORD"],
        db_user=os.environ["DATABASE_USER"],
        db_host=os.environ["DATABASE_HOST_TEST"],
    )


@pytest.fixture(scope="session", autouse=True)
def create_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute(open("test/init.sql", "r").read())


@pytest.fixture(scope="session", name="service")
def get_service(connection):
    return Service(SQLRepository(connection))


@pytest.fixture(scope="function", autouse=True)
def clear_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute('Truncate "Students";')
        cursor.execute('TRUNCATE "Rooms" CASCADE;')
        connection.commit()


@pytest.fixture(scope="module", autouse=True)
def clear_tables_module(connection):
    with connection.cursor() as cursor:
        cursor.execute('Truncate "Students";')
        cursor.execute('TRUNCATE "Rooms" CASCADE;')
        connection.commit()
