class Vacancy:
    """
    Класс для представления вакансии.
    """

    __slots__ = ("title", "url", "salary_from", "salary_to", "currency", "requirements")

    def __init__(self, title: str, url: str, salary: dict | None, requirements: str):
        self.title = title
        self.url = url
        self.salary_from, self.salary_to, self.currency = self.__validate_salary(salary)
        self.requirements = requirements

    def __validate_salary(self, salary: dict | None) -> tuple[int, int, str]:
        """
        Приватный метод валидации зарплаты.
        Возвращает кортеж (from, to, currency).
        """
        if not isinstance(salary, dict):
            return 0, 0, "не указана"

        try:
            salary_from = int(salary.get("from") or 0)
            salary_to = int(salary.get("to") or 0)
            currency = salary.get("currency", "RUB")
        except (TypeError, ValueError):
            return 0, 0, "не указана"

        return max(0, salary_from), max(0, salary_to), currency

    def validate(self) -> None:
        """
        Публичный метод проверки атрибутов.
        Вызывает исключение, если данные некорректны.
        """
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Название вакансии не может быть пустым.")
        if not isinstance(self.url, str) or not self.url.startswith("http"):
            raise ValueError("Ссылка на вакансию должна быть корректной.")

    def to_dict(self) -> dict:
        """
        Преобразует вакансию в словарь для сохранения в JSON.
        """
        return {
            "title": self.title,
            "url": self.url,
            "salary": {
                "from": self.salary_from,
                "to": self.salary_to,
                "currency": self.currency
            },
            "requirements": self.requirements
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vacancy | None":
        """
        Создаёт объект Vacancy из словаря.
        Возвращает None, если данные невалидны.
        """
        title = data.get("name") or data.get("title")
        url = data.get("alternate_url") or data.get("url")

        if not title or not url:
            return None

        salary = data.get("salary")
        snippet = data.get("snippet", {}) or {}
        requirements = snippet.get("requirement", "")

        return cls(
            title=title,
            url=url,
            salary=salary,
            requirements=requirements
        )

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по нижней границе зарплаты.
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from

    def __gt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по нижней границе зарплаты.
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from > other.salary_from

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает вакансии по нижней границе зарплаты.
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from

    def __str__(self) -> str:
        """
        Человекочитаемое представление вакансии.
        """
        salary_str = f"{self.salary_from}-{self.salary_to} {self.currency}" \
            if self.salary_from or self.salary_to else "не указана"
        return f"{self.title}\nЗарплата: {salary_str}\nТребования: {self.requirements[:100]}...\n{self.url}"