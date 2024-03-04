import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor()
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('C2C_02', 'okt 2023', 'aprl 2024')
cursor.execute(query, values)
group_id = cursor.lastrowid
print(group_id)

query = "insert INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
values = ('GLEB', 'SARATAS', group_id)
cursor.execute(query, values)
student_id = cursor.lastrowid

query = "INSERT INTO books (title, taken_by_student_id) values (%s, %s)"
values = ('Second', student_id)
cursor.execute(query, values)

query = "INSERT  into subjets (title) values (%s)"
values = ('Bukvar',)
cursor.execute(query, values)
subject_id = cursor.lastrowid

query = "INSERT  INTO lessons (title, subject_id) values (%s, %s)"
values = ('lesson 201', subject_id)
cursor.execute(query, values)
lesson_id = cursor.lastrowid

query = "INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)"
values = ('DONE', lesson_id, student_id)
cursor.execute(query, values)

db.commit()

cursor.execute("""
    SELECT students.name, `groups`.title as `group`, books.title as book,
           marks.value, subjets.title as sub, lessons.title as less
    from students
    join `groups` on students.group_id = `groups`.id
    join books on books.taken_by_student_id = students.id
    join marks on marks.student_id = students.id
    JOIN lessons on lessons.id = marks.lesson_id
    JOIN subjets on lessons.subject_id = subjets.id
    where students.name = 'GLEB'
""")
result = cursor.fetchone()
print("Results of the joined data:")
for data in result:
    print(data)
db.close()
