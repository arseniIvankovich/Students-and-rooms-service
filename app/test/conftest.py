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


@pytest.fixture(scope="function", autouse=True)
def create_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute(open("init_db/init.sql", "r").read())
    yield
    with connection.cursor() as cursor:
        cursor.execute('DROP TABLE "Students";')
        cursor.execute('DROP TABLE "Rooms";')
        connection.commit()


@pytest.fixture(scope="session", name="service")
def get_service(connection):
    return Service(SQLRepository(connection))
