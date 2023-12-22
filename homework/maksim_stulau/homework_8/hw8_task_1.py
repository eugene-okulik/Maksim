"""Напишите программу.
Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.
Если bonus - true, то к salary должен быть добавлен рандомный бонус.
Примеры результатов:
    10000, True - '$10255'
    25000, False - '$25000'
    600, True - '$3785'
"""

from random import choice


salary = int(input("what is your salary? "))
bonus = [True, False]
sum_bon = ["$10255", "$25000", "$3785"]
choice(sum_bon)
choice(bonus)

print(choice(sum_bon) + str(salary) if choice(bonus) is True else "$" + str(salary))
