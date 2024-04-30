import SQLRepository

class SimpleService:
    
    def __init__(self, repository) -> None:
        self._repository = repository
        
    def create_room (self, id, room):
        items = {'id': id, 'name': room}
        return self._repository.create_room(items)
    
    def create_student(self, id, name, birthday, sex, room):
        items = {'id': id, 'name': name, 'birthday': birthday, 'sex': sex, 'room': room}
        return self._repository.create_student(items)
    
    def get_rooms_students_count(self):
        return self._repository.get_rooms_students_count()
    
    def get_multisex_rooms(self):
        return self._repository.get_multisex_rooms()
    
    def get_five_rooms_with_lower_average(self):
        return self._repository.get_five_rooms_with_lower_average()
    
    def get_five_rooms_with_higher_differnce(self):
        return self._repository.get_five_rooms_with_higher_differnce()
    
    
