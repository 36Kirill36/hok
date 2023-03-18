class Student:
    # Поля класса
    name = ''
    year_of_birth = 2000
    groop = 2
    middle_mark = 8

    def __str__(self):
        return self.get_stats()

    def get_stats(self):
        return \
            f'Имя: {self.name}\n ' \
            f'Год Рождения: {self.year_of_birth}\n'\
            f'Группа:{self.groop}\n'\
            f'Средняя оценка:{self.middle_mark}\n'

    def get_age(self, year_of_birth):
        import datetime
        datetime.date.today().year  # 2023