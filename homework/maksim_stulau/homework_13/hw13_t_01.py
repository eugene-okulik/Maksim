"""Прочитать файлик, который лежит в репозитории в моей папке.
Здесь: homework/eugene_okulik/hw_13/data.txt

Файлик не копируйте и никуда не переносите.
Напишите программу, которая читает этот файл,
находит в нём даты и делает с этими датами то, что после них написано.
Опирайтесь на то, что структура каждой строки одинакова:
сначала идет номер, потом дата, потом дефис и после него текст.
У вас должен получиться код,
который находит даты и для даты под номером один в коде должно быть реализовано то действие,
которое написано в файле после этой даты. Ну и так далее для каждой даты."""

import os
import datetime


base_path = os.path.dirname(__file__)
# file_path = os.path.join(base_path, "hw13_t_01.py")
new_file_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(new_file_path, "eugene_okulik", "hw_13", "data.txt")

# print(file_path)
print(eugene_file_path)


with open(eugene_file_path) as data_file:
    for line in data_file.readlines():
        number = int(line.split('.')[0])
        date_str = line[3:29]
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        if number == 1:
            print(date + datetime.timedelta(days=7))
        elif number == 2:
            print(date.strftime('%A'))
        elif number == 3:
            today_time = datetime.datetime.now()
            num_days = (today_time - date).days
            print(num_days)


# today_time = datetime.datetime.now()
# print(today_time)
# min_week = today_time + datetime.timedelta(days=7)
# print(f"1. {min_week}")
# name_day = today_time.strftime("%A")
# print(f"2. {name_day}")
# last_date = datetime.datetime(year=2023, month=6, day=12, hour=15, minute=23, second=45, microsecond=312167)
# num_days = today_time - last_date
# print(f"3. {num_days}")
