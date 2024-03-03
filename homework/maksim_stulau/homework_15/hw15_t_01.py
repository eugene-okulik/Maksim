import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor()
cursor.execute("INSERT INTO `groups`(title, start_date, end_date) values ('C2C_02', 'okt 2023', 'aprl 2024')")
group_id = cursor.lastrowid
print(group_id)
cursor.execute(f"insert INTO students (name, second_name, group_id) VALUES ('GLEB', 'SARATAS', {group_id})")
student_id = cursor.lastrowid
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Second', {student_id})")
cursor.execute("INSERT  into subjets (title) values ('Bukvar')")
subject_id = cursor.lastrowid
cursor.execute(f"INSERT  INTO lessons (title, subject_id) values ('lesson 201', {subject_id})")
lesson_id = cursor.lastrowid
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('DONE', {lesson_id}, {student_id})")

db.commit()
db.close()
