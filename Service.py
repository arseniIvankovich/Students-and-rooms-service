from SQLRepository import SQLRepository
import json
from dateutil import parser

def hinted_tuple_hook(obj):
        if '__tuple__' in obj:
            return tuple(obj['items'])
        else:
            return obj
        
class Service:
    
    def __init__(self, repository) -> None:
        self._repository = repository
        
    def insert_all_rooms (self):
        with open('rooms.json') as file:
            items = [(i['id'], i['name']) for i in json.load(file)]
            return self._repository.insert_rooms(items)
    
    def insert_all_students(self):
         with open('students.json') as file:
            items = [(i['id'], str(parser.parse(i['birthday'])), i['name'].split()[0],  i['name'].split()[1], i['room'], i['sex']) for i in json.load(file)]
            return self._repository.insert_students(items)
    
    def get_rooms_students_count(self):
        return self._repository.get_rooms_students_count()
    
    def get_rooms_with_different_sexs(self):
        return self._repository.get_rooms_with_different_sexs()
    
    def get_five_rooms_with_lower_average(self):
        return self._repository.get_five_rooms_with_lower_average()
    
    def get_five_rooms_with_higher_differnce(self):
        return self._repository.get_five_rooms_with_higher_differnce()
    

simple_service = Service(SQLRepository())
print(simple_service.get_five_rooms_with_higher_differnce())
