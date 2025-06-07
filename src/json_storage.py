import json
from typing import List

from src.abstract_classes import VacancyStorage
from src.vacancy import Vacancy


class JSONVacancyStorage(VacancyStorage):
    """
    Класс для работы с хранилищем вакансий в формате JSON.
    """

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename
        self.__vacancies = []  # Приватный список вакансий
        self.__load_vacancies()  # Загружаем при инициализации

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет вакансию в список, если её ещё нет.
        """
        if vacancy is None:
            return

        if not any(v.url == vacancy.url for v in self.__vacancies):
            self.__vacancies.append(vacancy)
            self.__save_vacancies()

    def get_vacancies(self) -> List[Vacancy]:
        """
        Возвращает копию списка вакансий.
        """
        return list(self.__vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию по ссылке.
        """
        try:
            self.__vacancies.remove(vacancy)
            self.__save_vacancies()
        except ValueError:
            print(f"Вакансия '{vacancy.title}' не найдена для удаления.")

    def __save_vacancies(self) -> None:
        """
        Сохраняет список вакансий в JSON-файл.
        """
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([v.to_dict() for v in self.__vacancies], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")

    def __load_vacancies(self) -> None:
        """
        Загружает вакансии из JSON-файла.
        Если файл отсутствует или повреждён — создаёт пустой список.
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Преобразуем словари обратно в объекты Vacancy
                self.__vacancies = [Vacancy(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__vacancies = []