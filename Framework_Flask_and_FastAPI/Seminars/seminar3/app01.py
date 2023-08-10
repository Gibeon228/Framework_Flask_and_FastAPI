# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
import random

from flask import Flask, render_template

from models01 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello world!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-faculty')
def add_faculty():
    count = 2
    for faculty in range(1, count + 1):
        new_faculty = Faculty(name=f'name{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('Add faculty')


@app.cli.command('add-student')
def add_student():
    count = 5
    for student in range(1, count + 1):
        new_student = Student(first_name=f'first_name{student}',
                              last_name=f'last_name{student}',
                              age=random.randint(16, 30),
                              gender=random.choice(['male', 'female']),
                              group=random.choice(['1A', '2B', '3C']),
                              faculty_id=random.choice([1, 2]))
        db.session.add(new_student)
    db.session.commit()
    print('Add student')

@app.route('/show-students/')
def show_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('page01.html', **context)



if __name__ == '__main__':
    app.run(debug=True)
