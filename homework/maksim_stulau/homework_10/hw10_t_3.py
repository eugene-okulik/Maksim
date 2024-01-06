"""Напишите программу: Есть функция которая делает одну из арифметических операций
с переданными ей числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....

Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

    если числа равны, то функция calc вызывается с операцией сложения этих чисел
    если первое больше второго, то происходит вычитание второго из певрого
    если второе больше первого - деление первого на второе
    если одно из чисел отрицательное - умножение
"""


def decor(func):
    def wrapper(*args):

        first = args[0]
        second = args[1]
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


x = int(input("first num: "))
y = int(input("second num: "))


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


result = calc(x, y)
print(result)
