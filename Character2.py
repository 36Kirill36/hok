from datetime import datetime
class Student:

    def __init__(self, name ='', year = 2000, groop = 1, mark = 12, age = 23):
        self.name = name
        self.year = year
        self.groop = groop
        self.mark = mark
        self.age = age

    def get_age(self):
        today = datetime.date.today().year
        birth = int(self.year)
        return \
             f'{today - birth}\n' \


    def __str__(self):
        return self.get_stats()

    def get_stats(self):
        return \
            f'Имя: {self.name}\n ' \
            f'Год Рождения: {self.year}\n'\
            f'Группа:{self.groop}\n'\
            f'Средняя оценка:{self.mark}\n'\
            f'возраст:{self.age}\n'


