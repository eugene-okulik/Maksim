"""Напишите функцию-генератор, которая генерирует список чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
"""


def generate(limit=1000000000000):
    a, b = 0, 1
    count1 = 0

    while count1 < limit:
        yield a
        a, b = b, a + b
        count1 += 1


# print(list(generate(10)))


count = 1
f_list = []

for number in generate():
    if count == 5:
        f_list.append(number)
    elif count == 200:
        f_list.append(number)
    elif count == 1000:
        f_list.append(number)
    elif count == 100000:
        f_list.append(number)
        break
    count += 1

print(f_list[:3])
