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
        items = self._repository.get_rooms_students_count()
        list_to_json = [{'room': i[0], 'amount' : i[1]} for i in items]
        with open('rooms_amount.json','w') as file:
            json.dump(list_to_json, file, indent=4)   
    
    def get_rooms_with_different_sexes(self):
        items = self._repository.get_rooms_with_different_sexes()
        list_to_json = [{'room': i[0]} for i in items]
        with open('rooms_with_different_sexes.json','w') as file:
            json.dump(list_to_json, file, indent=4) 
    
    def get_five_rooms_with_least_age_average(self):
        items = self._repository.get_five_rooms_with_lower_age_average()
        list_to_json = [{'room': i[0]} for i in items]
        with open('five_rooms_lower_age_average.json','w') as file:
            json.dump(list_to_json, file, indent=4) 
    
    def get_five_rooms_with_largest_age_differnce(self):
        items = self._repository.get_five_rooms_with_largest_age_differnce()
        list_to_json = [{'room': i[0]} for i in items]
        with open('five_rooms_with_largest_age_differnce.json','w') as file:
            json.dump(list_to_json, file, indent=4) 
    

simple_service = Service(SQLRepository())
print(simple_service.get_five_rooms_with_largest_age_differnce())
