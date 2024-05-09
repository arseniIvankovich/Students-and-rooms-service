# Students and rooms service
A service that loads data from json files into a database and retrieves data from it, saves the result as json files:
* A list of rooms and the number of students in each room
* 5 rooms with the smallest average age of students
* 5 rooms with the largest difference in the age of students
* List of rooms with mixed-sex students
## Folder Structure
```bash
├── app
│   ├── db
│   │   ├── connection.py
│   │   ├── __init__.py
│   │   ├── repository_interface.py
│   │   └── sql_repository.py
│   ├── Dockerfile
│   ├── init_db
│   │   └── init.sql
│   ├── input
│   │   ├── rooms.json
│   │   ├── students.json
│   │   ├── test_rooms_1.json
│   │   ├── test_rooms_2.json
│   │   ├── test_students_1.json
│   │   └── test_students_2.json
│   ├── logging.conf
│   ├── main.py
│   ├── requirements.txt
│   ├── service
│   │   ├── __init__.py
│   │   └── service.py
│   └── test
│       ├── conftest.py
│       ├── __init__.py
│       └── test_service.py
├── docker-compose.yml
├── pyproject.toml
└── README.md

```
- `app` - Folder contains main logic of application. Used for build app.
- `app.db.repository_interface.py` - Interface that defines the methods implemented by the sql repository class.
- `app.db.sql_repository.py` - Contains the implementation of a repository interface that interacts with a database.
- `logging.conf` - Configuration file for loggers.
- `app/init_db` - Folder contains sql script for creation  tables.
- `app/test` - Folder contains test for service.
- `app/Dockerfile` - File is used to build a Docker image for application.
- `app/input` - Directory contains JSON files that contain input data for application. And also contians data for tests.
- `app/requirements.txt` - File lists the Python dependencies required by application.
- `app.mian.py` - Main entry point of  application.
- `app/service` - Folder contains the business logic of application.
- `app/test` - Folder contains tests for service logic.
- `docker-compose.yml` - File defines services, networks, and volumes for your Docker application.

## Installation

### Prerequisites
You need to have docker installed on your machine.</

Build and lauch containers of the docker compose:
```
docker-compose up --build
```
### Testing
If you want to launch tests, you can do it directly on the container.
```
 docker exec -it <container> sh
 pytest test/
 ```
