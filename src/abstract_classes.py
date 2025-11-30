from abc import ABC, abstractmethod
from typing import List


class VacancyParser(ABC):
    """
    Абстрактный класс для получения вакансий через API.
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[dict]:
        """
        Получает вакансии по ключевому слову.

        :param keyword: Ключевое слово для поиска.
        :return: Список вакансий в формате dict.
        """
        pass


class VacancyEntity(ABC):
    """
    Абстрактный класс для работы с вакансиями.
    """

    @abstractmethod
    def validate(self) -> None:
        """
        Проверяет корректность данных вакансии.
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Преобразует вакансию в словарь.
        """
        pass


class VacancyStorage(ABC):
    """
    Абстрактный класс для работы с хранилищем вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: VacancyEntity) -> None:
        """
        Добавляет вакансию в хранилище.

        :param vacancy: Объект вакансии.
        """
        pass

    @abstractmethod
    def get_vacancies(self) -> List[VacancyEntity]:
        """
        Возвращает список вакансий.

        :return: Список объектов типа VacancyEntity.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: VacancyEntity) -> None:
        """
        Удаляет указанную вакансию.

        :param vacancy: Объект вакансии.
        """
        pass