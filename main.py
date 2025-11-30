from src.hh_api import HeadHunterAPI
from src.json_storage import JSONVacancyStorage
from src.vacancy import Vacancy


def user_interaction():
    """
    Основная функция взаимодействия с пользователем.
    Предоставляет меню для работы с вакансиями с hh.ru.
    """

    hh = HeadHunterAPI()
    storage = JSONVacancyStorage()

    print("=== Программа для работы с вакансиями ===")
    keyword = input("Введите поисковой запрос (например: Python): ").strip()

    # Получаем вакансии с hh.ru
    print(f"Получаем вакансии по запросу '{keyword}'...")
    raw_vacancies = hh.get_vacancies(keyword)

    if not raw_vacancies:
        print("Ничего не найдено. Попробуйте другой запрос.")
        return

    # Преобразуем в объекты Vacancy
    vacancies = []
    for item in raw_vacancies:
        vacancy = Vacancy.from_dict(item)
        if vacancy:
            vacancies.append(vacancy)

    # Сохраняем полученные вакансии
    for vacancy in vacancies:
        storage.add_vacancy(vacancy)

    print(f"\nУспешно добавлено вакансий: {len(vacancies)}\n")

    # Меню пользователя
    while True:
        print("\nВыберите действие:")
        print("1 - Показать топ N вакансий по зарплате")
        print("2 - Поиск по ключевому слову в описании")
        print("3 - Удалить вакансию")
        print("4 - Показать все вакансии")
        print("5 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            try:
                n = int(input("Сколько топ-вакансий показать? "))
                all_vacancies = storage.get_vacancies()
                sorted_vacancies = sorted(all_vacancies, reverse=True)
                print(f"\nТоп {n} вакансий по зарплате:\n")
                for v in sorted_vacancies[:n]:
                    print(v)
            except ValueError:
                print("Введите корректное число.")

        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска в требованиях: ").lower()
            filtered = [
                v for v in storage.get_vacancies()
                if keyword in v.requirements.lower()
            ]
            print(f"\nНайдено вакансий: {len(filtered)}\n")
            for v in filtered:
                print(v)

        elif choice == "3":
            title = input("Введите название вакансии для удаления: ")
            all_vacancies = storage.get_vacancies()
            found = [v for v in all_vacancies if title.lower() in v.title.lower()]
            if found:
                for v in found:
                    storage.delete_vacancy(v)
                print(f"Удалено {len(found)} вакансий с названием '{title}'")
            else:
                print("Вакансии не найдены.")

        elif choice == "4":
            all_vacancies = storage.get_vacancies()
            print(f"\nВсе сохранённые вакансии ({len(all_vacancies)} штук):\n")
            for v in all_vacancies:
                print(v)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неизвестный выбор. Попробуйте снова.")


if __name__ == "__main__":
    user_interaction()