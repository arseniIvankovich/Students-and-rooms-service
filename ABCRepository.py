from abc import ABC, abstractmethod


class ABCRepository(ABC):
    
    @abstractmethod
    def create_room(self, id, name):
        raise NotImplementedError
    
    @abstractmethod
    def create_student(self, id, name, room, birthday, sex):
        raise NotImplementedError
    
    @abstractmethod
    def get_rooms_students_count(self):
        raise NotImplementedError
    
    @abstractmethod
    def multisex_rooms(self):
        raise NotImplementedError
    
    @abstractmethod
    def five_rooms_with_lower_average(self):
        raise NotImplementedError
    
    @abstractmethod
    def five_rooms_with_higher_differnce(self):
        raise NotImplementedError
    
    