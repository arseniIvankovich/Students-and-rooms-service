from abc import ABC, abstractmethod


class ABCRepository(ABC):
    
    @abstractmethod
    def create_room(self, items):
        raise NotImplementedError
    
    @abstractmethod
    def create_student(self, items):
        raise NotImplementedError
    
    @abstractmethod
    def get_rooms_students_count(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_multisex_rooms(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_five_rooms_with_lower_average(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_five_rooms_with_higher_differnce(self):
        raise NotImplementedError
    
    