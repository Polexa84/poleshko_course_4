class Position:
    """ Класс для представления вакансий и создания списка экземпляров вакансий для вывода на экран"""
    all_positions = []

    def __init__(self, title, url, salary_min, salary_max, description):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.description = description

        Position.all_positions.append(self)

    def __gt__(self, other):
        return int(self.salary_min) > int(other.salary_min)

    def __ge__(self, other):
        return int(self.salary_min) >= int(other.salary_min)

    def __lt__(self, other):
        return int(self.salary_min) < int(other.salary_min)

    def __le__(self, other):
        return int(self.salary_min) <= int(other.salary_min)

    def __eq__(self, other):
        return int(self.salary_min) == int(other.salary_min)

    def __str__(self):
        return f'Название вакансии: {self.title}\n' \
               f'Ссылка на вакансию: {self.url}\n' \
               f'Минимальная зарплата {self.salary_min} руб. \n' \
               f'Максимальная зарплата {self.salary_max} руб. \n' \
               f'Требования к соискателю: {self.description} \n' \


    @classmethod
    def position_item(cls, reader):
        for row in reader:
            cls(row['title'], row['url'], row['salary_min'], row['salary_max'], row['description'])