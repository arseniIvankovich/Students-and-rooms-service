from app.db.repository_interface import IRepository
from app.db.connection import connect

class SQLRepository(IRepository):
    
    def __init__(self):
        self._connection = connect()

    def insert_rooms(self,items):
        cursor = self._connection.cursor()
        cursor.executemany("INSERT INTO \"Rooms\" (id, room) VALUES (%s, %s);", items)
        self._connection.commit()
        
    def insert_students(self, items): 
        cursor = self._connection.cursor()
        cursor.executemany("INSERT INTO \"Students\" (id, birthday, first_name, second_name, room, sex) VALUES (%s, %s, %s, %s, %s, %s);", items)
        self._connection.commit()
        
    def get_rooms_students_count(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT rooms.room, COUNT(students.id) AS amount FROM \"Rooms\" AS rooms \
                       LEFT JOIN \"Students\" AS students ON students.room = rooms.id \
                       GROUP BY rooms.room ORDER BY amount DESC;")
        result = cursor.fetchall()
        return result 
    
    def get_rooms_with_different_sexes(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT rooms.room FROM \"Rooms\" AS rooms \
                       LEFT JOIN \"Students\" AS students ON students.room = rooms.id \
	                   GROUP BY rooms.room HAVING COUNT(DISTINCT sex) > 1")
        result = cursor.fetchall()
        return result 
    
    def get_five_rooms_with_least_age_average(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT room FROM ( \
                            SELECT rooms.room, ROUND(CAST(AVG(DATE_PART('year', AGE(birthday)))as numeric),2) AS avg_age \
                            FROM \"Rooms\" AS rooms \
                            LEFT JOIN \"Students\" AS students ON students.room = rooms.id \
                            GROUP BY rooms.room ORDER BY avg_age \
                            ) AS inner_query LIMIT 5;")
        result = cursor.fetchall()
        return result 
    
    def get_five_rooms_with_largest_age_differnce(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT room FROM ( \
                        SELECT rooms.room, DATE_PART('year', MAX(AGE(birthday))) - DATE_PART('year', MIN(AGE(birthday))) AS max_min_sub_age \
                        FROM \"Rooms\" AS rooms \
                        LEFT JOIN \"Students\" AS students ON students.room = rooms.id \
                        GROUP BY rooms.room ORDER BY max_min_sub_age DESC) AS inner_query LIMIT 5;")
        result = cursor.fetchall()
        return result 
    

