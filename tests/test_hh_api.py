import pytest
from src.hh_api import HeadHunterAPI


def test_get_vacancies_returns_list():
    """Проверяет, что get_vacancies возвращает список."""
    hh = HeadHunterAPI()
    result = hh.get_vacancies("Python")
    assert isinstance(result, list)


def test_get_vacancies_non_empty():
    """Проверяет, что запрос возвращает хотя бы одну вакансию."""
    hh = HeadHunterAPI()
    result = hh.get_vacancies("Python")
    assert len(result) > 0


def test_get_vacancies_has_required_fields():
    """Проверяет наличие обязательных полей в ответе."""
    hh = HeadHunterAPI()
    results = hh.get_vacancies("Python")[:3]  # Берём несколько для теста

    for item in results:
        assert "name" in item
        assert "alternate_url" in item
        assert "salary" in item