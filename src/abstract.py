from abc import ABC, abstractmethod


class APIParser(ABC):
    """Структурируем дочерние классы"""

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def make_json_file(self, vac_list):
        pass

    @abstractmethod
    def sort_by_max_salary(self, vac_list):
        pass