import  json
import os
from typing import List
from src.vacancy_storage import VacancyStorage
from src.vacancy import Vacancy


class JSONVacancyStorage(VacancyStorage):
    """
    Сохранение данных в JSON
    """
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self._save_all(vacancies)

    def _save_all(self, vacancies: List[Vacancy]) -> None:
        """Сохраняет все вакансии в файл"""
        with open(self.__filename, "w", encoding="utf-8") as file:
            data = [v.__dict__ for v in vacancies]
            json.dump(data, file, ensure_ascii=False, indent=2)