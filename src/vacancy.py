class Vacancy:
    __slots__ = ("title", "url", "salary", "requirements")

    def __init__(self, title: str, url: str, salary: int, requirements: str):
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.requirements = requirements

    def __repr__(self):
        return f"{self.title}({self.salary} руб.)\n{self.url}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    @staticmethod
    def __validate_salary(salary):
        if isinstance(salary, int) and salary > 0:
            return salary
        return 0

    @classmethod
    def cast_from_dict(cls, data: dict):
        title = data.get("name", "Без названия")
        url = data.get("alternate_url", "Нет ссылки")
        salary_info = data.get("salary")
        salary = salary_info.get("from", 0)  if salary_info else 0
        req = data.get("snippet", {}).get("requirement", "")
        return cls(title, url, salary, req)