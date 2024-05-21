"""
Main point of app. Initialize a connection to a database using environment variables,
inserts data into the database, and performs various queries using a service layer.
"""

import os
import time

from db.connection import connect
from db.sql_repository import SQLRepository
from dotenv import load_dotenv
from service.service import StudentRoomService

load_dotenv()

if __name__ == "__main__":
    _connect = connect(
        db_name=os.environ["DATABASE_NAME"],
        db_password=os.environ["DATABASE_PASSWORD"],
        db_user=os.environ["DATABASE_USER"],
        db_host=os.environ["DATABASE_HOST"],
    )
    service = StudentRoomService(SQLRepository(_connect))
    service.insert_rooms("input/rooms.json")
    service.insert_students("input/students.json")
    service.create_index_on_rooms()
    service.get_rooms_with_mixedSex_students_json("rooms_with_different_mixed-sex_students.json")
    service.get_five_rooms_with_largest_age_differnce_json("five_rooms_with_largest_age_differnce.json")
    service.get_five_rooms_with_smallest_age_average_json("five_rooms_smallest_age_average.json")
    service.get_rooms_students_count_json("rooms_amount.json")
    service.get_rooms_with_mixedSex_students_xml("rooms_with_different_mixed-sex_students.json")
    service.get_five_rooms_with_largest_age_differnce_xml("five_rooms_with_largest_age_differnce.json")
    service.get_five_rooms_with_smallest_age_average_xml("five_rooms_smallest_age_average.json")
    service.get_rooms_students_count_xml("rooms_amount.json")
    while True:
        time.sleep(5)
