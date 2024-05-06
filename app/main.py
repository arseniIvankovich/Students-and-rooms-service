"""_summary_
"""

from db.sql_repository import SQLRepository
from service.service import Service

if __name__ == "__main__":
    service = Service(SQLRepository())
    service.get_rooms_with_different_sexes()
    service.get_five_rooms_with_largest_age_differnce()
    service.get_five_rooms_with_least_age_average()
    service.get_rooms_students_count()
