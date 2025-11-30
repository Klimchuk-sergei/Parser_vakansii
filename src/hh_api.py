import requests
from typing import List

from src.abstract_classes import VacancyParser
from src.vacancy import Vacancy


class HeadHunterAPI(VacancyParser):
    """
    Класс для работы с API hh.ru.
    Предоставляет методы для получения вакансий по ключевому слову.
    """

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {
            "text": "",
            "page": 0,
            "per_page": 20,
            "area": 113  # Россия
        }

    def get_vacancies(self, keyword: str) -> List[dict]:
        """
        Получает вакансии по ключевому слову из hh.ru.

        :param keyword: Ключевое слово для поиска.
        :return: Список словарей с данными о вакансиях.
        """
        self.__params["text"] = keyword
        self.__params["page"] = 0
        vacancies = []

        while self.__params["page"] < 5:
            try:
                response = requests.get(self.__base_url, headers=self.__headers, params=self.__params)
                if response.status_code != 200:
                    break

                data = response.json()
                vacancies.extend(data.get("items", []))
                self.__params["page"] += 1

            except (requests.ConnectionError, requests.Timeout) as e:
                print(f"Ошибка подключения к API: {e}")
                break

        return vacancies