from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def insert_rooms(self, items):
        pass

    @abstractmethod
    def insert_students(self, items):
        pass

    @abstractmethod
    def get_rooms_students_count(self):
        pass

    @abstractmethod
    def get_rooms_with_mixedSex_students(self):
        pass

    @abstractmethod
    def get_five_rooms_with_smallest_age_average(self):
        pass

    @abstractmethod
    def get_five_rooms_with_largest_age_differnce(self):
        pass

    @abstractmethod
    def create_index_on_rooms(self):
        pass
