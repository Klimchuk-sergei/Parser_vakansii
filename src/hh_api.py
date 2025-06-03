import requests
from src.abstract_claasses import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}

    def get_vacancies(self, keyword: str) -> list[dict]:
        self.__params["text"] = keyword
        self.__params["page"] = 0
        vacancies = []

        while self.__params["page"] < 5:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                break
            data = response.json()
            vacancies.extend(data.get("items", []))
            self.__params["page"] += 1

        return vacancies
