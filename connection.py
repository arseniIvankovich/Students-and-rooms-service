import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    try:
        with psycopg2.connect(database=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"), 
                              password=os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST")) as connection:
            print('Connect')
            return connection
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)
