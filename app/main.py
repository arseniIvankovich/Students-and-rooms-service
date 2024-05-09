"""_summary_
"""
import os
import time

from db.connection import connect
from db.sql_repository import SQLRepository
from dotenv import load_dotenv
from service.service import Service

load_dotenv()

if __name__ == "__main__":
    _connect = connect(
        db_name=os.environ["DATABASE_NAME"],
        db_password=os.environ["DATABASE_PASSWORD"],
        db_user=os.environ["DATABASE_USER"],
        db_host=os.environ["DATABASE_HOST"],
    )
    service = Service(SQLRepository(_connect))
    # service.insert_rooms("input/rooms.json")
    # service.insert_students("input/students.json")
    service.create_index_on_rooms()
    service.get_rooms_with_different_sex()
    service.get_five_rooms_with_largest_age_differnce()
    service.get_five_rooms_with_least_age_average()
    service.get_rooms_students_count()
    while True:
        time.sleep(5)
