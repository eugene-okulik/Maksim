"""Есть такой список:
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.
Распечатайте из нового списка самую высокую температуру самую низкую и среднюю."""

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
                27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hot(x):
    if x > 28:
        return x


hot_days = filter(hot, temperatures)
print(list(hot_days))


hot_days_1 = filter(lambda x: x if x > 28 else None, temperatures)
hot_days_2 = list(hot_days_1)
print(hot_days_2)
print(max(hot_days_2))
print(min(hot_days_2))
print(sum(hot_days_2) / len(hot_days_2))
