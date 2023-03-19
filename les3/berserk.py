from Character import Character
from colorama import  Fore


class Berserk(Character):

    def __init__(self,name='', health=100,damage=1,defence=0,color=Fore.LIGHTBLUE_EX):
        Character.__init__(self,name,health,damage,defence,color)
        self.max_health = health

    def get_additional_damage(self):
        return int(self.health * (1 - self.health / self.max_health))
    def attack(self, target):
       target.take_damage(self.damage + self.get_additional_damage())

    def get_stats(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здровье: {self.health}  (+{self.get_additional_damage()}\n'\
            f'Урон: {self.damage}\n ' \
            f'Защита {self.defence}\n'