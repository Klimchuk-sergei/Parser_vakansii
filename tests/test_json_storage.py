import os
import pytest
import json
from src.json_storage import JSONVacancyStorage
from src.vacancy import Vacancy


@pytest.fixture
def storage(tmpdir):
    """Создает временное хранилище."""
    tmp_file = tmpdir.join("test_vacancies.json")
    return JSONVacancyStorage(str(tmp_file))


def test_add_and_get_vacancy(storage):
    """Проверяет добавление и получение вакансии."""
    vacancy = Vacancy("Test", "http://test.com", {"from": 50000}, "Требования")
    storage.add_vacancy(vacancy)

    vacancies = storage.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].title == "Test"


def test_delete_vacancy(storage):
    """Проверяет удаление вакансии."""
    vacancy = Vacancy("Test", "http://test.com", {"from": 50000}, "Требования")
    storage.add_vacancy(vacancy)
    storage.delete_vacancy(vacancy)

    assert len(storage.get_vacancies()) == 0


def test_duplicate_prevention(storage):
    """Проверяет защиту от дубликатов."""
    vacancy = Vacancy("Test", "http://test.com", {"from": 50000}, "Требования")
    storage.add_vacancy(vacancy)
    storage.add_vacancy(vacancy)

    assert len(storage.get_vacancies()) == 1


def test_file_created(tmpdir):
    """Проверяет, что файл создаётся при добавлении."""
    tmp_file = tmpdir.join("test_vacancies.json")
    storage = JSONVacancyStorage(str(tmp_file))
    vacancy = Vacancy("Test", "http://test.com", {"from": 50000}, "Требования")
    storage.add_vacancy(vacancy)

    assert os.path.exists(str(tmp_file))
    with open(str(tmp_file), "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 1