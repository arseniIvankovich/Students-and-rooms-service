from app.service.service import Service
from app.db.sql_repository  import SQLRepository


if __name__ == "__main__":
    service = Service(SQLRepository())
    print(service.get_five_rooms_with_largest_age_differnce())