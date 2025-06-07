import pytest
from src.vacancy import Vacancy


def test_vacancy_initialization():
    """Проверяет корректную инициализацию вакансии."""
    vacancy = Vacancy("Python Developer", "https://example.com",  {"from": 100000, "to": 150000, "currency": "RUR"}, "Опыт от 3 лет")
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.currency == "RUR"
    assert "опыт" in vacancy.requirements.lower()


def test_salary_validation():
    """Проверяет валидацию зарплаты."""
    vacancy = Vacancy("Менеджер", "https://example.com",  None, "")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.currency == "не указана"


def test_comparison_operators():
    """Проверяет сравнение вакансий по зарплате."""
    v1 = Vacancy("V1", "url", {"from": 100000}, "")
    v2 = Vacancy("V2", "url", {"from": 120000}, "")

    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_from_dict_valid():
    """Проверяет создание из словаря с валидными данными."""
    data = {
        "name": "Junior Python",
        "alternate_url": "https://hh.ru/vacancy/123",
        "salary": {"from": 80000, "to": 100000, "currency": "RUR"},
        "snippet": {"requirement": "Знание Python"}
    }
    vacancy = Vacancy.from_dict(data)
    assert vacancy.title == "Junior Python"
    assert vacancy.salary_from == 80000
    assert "python" in vacancy.requirements.lower()


def test_from_dict_invalid():
    """Проверяет обработку некорректных данных."""
    data = {
        "name": "",
        "alternate_url": ""
    }
    assert Vacancy.from_dict(data) is None