from Character2 import  Student

player1 = Student(name='Anton', year_of_birth= 2001, groop= 1, middle_mark= 8)
print((player1.get_stats()))

player2 = Student(name='Artem', year_of_birth= 2005, groop= 2, middle_mark= 10)
print((player2.get_stats()))

player1.get_age(22)
player2.get_age(18)

print(player1.get_stats())
print(player2.get_stats())