import mysql.connector as mysql
# import creds
import os
import dotenv
import csv_files

dotenv.load_dotenv()

db = mysql.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
cursor.execute("""
    SELECT students.name, students.second_name, `groups`.title as `group`, books.title as book,
           marks.value, subjets.title as sub, lessons.title as less
    from students
    join `groups` on students.group_id = `groups`.id
    join books on books.taken_by_student_id = students.id
    join marks on marks.student_id = students.id
    JOIN lessons on lessons.id = marks.lesson_id
    JOIN subjets on lessons.subject_id = subjets.id
    
""")
data = cursor.fetchall()
# print(data)


csv_data = csv_files.csv_f()
for _ in csv_data:
    if _ in data:
        continue
    else:
        print(_)


# print(csv_data)
# db.close()
