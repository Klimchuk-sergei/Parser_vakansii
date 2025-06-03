from abc import ABC, abstractmethod
from typing import List
from src.vacancy import Vacancy

class VacancyStorage(ABC):
    """
    Клас для работы с вакансиями в сохраненых данных
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass