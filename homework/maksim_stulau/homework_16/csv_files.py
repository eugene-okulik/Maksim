import csv
import os

base_path = os.path.dirname(__file__)
new_file_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(new_file_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")


def csv_f():
    with open(eugene_file_path, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        data_csv = []
        for row in file_data:
            data_csv.append({'name': row[0],
                             'second_name': row[1],
                             'group': row[2],
                             'book': row[3],
                             'value': row[6],
                             'sub': row[4],
                             'less': row[5]})
    return data_csv[1:]


# for row in data_csv:
#     name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
    # print(f'Name: {name}, Second name {second_name}, group_title: {group_title}, Book title {book_title}, '
    #       f'Subject title {subject_title}, lesson title {lesson_title}, Mark value {mark_value}')

