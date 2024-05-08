from abc import ABC, abstractmethod


class IRepository(ABC):
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
    def get_rooms_with_different_sex(self):
        raise NotImplementedError

    @abstractmethod
    def get_five_rooms_with_least_age_average(self):
        raise NotImplementedError

    @abstractmethod
    def get_five_rooms_with_largest_age_differnce(self):
        raise NotImplementedError

    @abstractmethod
    def create_index_on_rooms(self):
        raise NotImplementedError
