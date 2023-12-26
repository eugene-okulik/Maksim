"""Дана такая дата: "Jan 15, 2023 - 12:05:33"
Преобразуйте эту дату в питоновский формат, после этого:
1. Распечатайте полное название месяца из этой даты
2. Распечатайте дату в таком формате: "15.01.2023, 12:05"""

import datetime

# print(datetime.datetime.now())

in_time = "Jan 15, 2023 - 12:05:33"
p_date = datetime.datetime.strptime(in_time, '%b %d, %Y - %H:%M:%S')
print(p_date)

h_date = p_date.strftime('%B %d, %Y - %H:%M:%S')
print(h_date)

new_h_date = p_date.strftime('%d.%m.%Y, - %H:%M')
print(new_h_date)
