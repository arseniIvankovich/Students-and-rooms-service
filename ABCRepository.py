from abc import ABC, abstractmethod


class ABCRepository(ABC):
    
    @abstractmethod
    def insert_rooms(self, items):
        raise NotImplementedError
    
    @abstractmethod
    def insert_students(self, items):
        raise NotImplementedError
    
    @abstractmethod
    def get_rooms_students_count(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_rooms_with_different_sexs(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_five_rooms_with_lower_average(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_five_rooms_with_higher_differnce(self):
        raise NotImplementedError
    