from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """
    Класс для api с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass


class VacancySaver(ABC):
    """
    Класс для сохранения вакансий
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self) -> list:
        pass
