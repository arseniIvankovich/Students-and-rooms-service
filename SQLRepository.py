import ABCRepository
from connection import connect
class SQLRepository(ABCRepository):
    
    def __init__(self, connection):
        self._connection = connect()
    
    def create_room(self, id, name):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO public.\"Rooms\"(id, room) VALUES (?, ?);", (id , name))
        result = cursor.fetchone()
        return result if result is not None else None
        
    def create_student(self, id, name, room, birthday, sex): 
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO public.\"Students\"(id, birthday, name, room, sex) VALUES (?, ?, ?, ?, ?);", (id , birthday, name, room, sex))
        result = cursor.fetchone()
        return result if result is not None else None

    def get_rooms_students_count(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT rooms.room, COUNT(students.id) FROM public.\"Rooms\" AS rooms \
                       RIGHT JOIN public.\"Students\" as students ON students.room = rooms.id \
                       GROUP BY rooms.room;")
        result = cursor.fetchone()
        return result if result is not None else None
    
    def multisex_rooms(self):
        cursor = self._connection.cursor()
        cursor.execute("")
        result = cursor.fetchone()
        return result if result is not None else None
    
    def five_rooms_with_lower_average(self):
        cursor = self._connection.cursor()
        cursor.execute("")
        result = cursor.fetchone()
        return result if result is not None else None
    
    def five_rooms_with_higher_differnce(self):
        cursor = self._connection.cursor()
        cursor.execute("")
        result = cursor.fetchone()
        return result if result is not None else None
    
