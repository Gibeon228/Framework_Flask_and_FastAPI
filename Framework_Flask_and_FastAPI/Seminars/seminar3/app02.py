# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
import random

from flask import Flask, render_template

from models02 import db, Author, Book

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


@app.cli.command('add-author')
def add_author():
    count = 3
    for author in range(1, count + 1):
        new_author = Author(first_name=f'first_name{author}',
                            last_name=f'last_name{author}')
        db.session.add(new_author)
    db.session.commit()
    print('Add author')


@app.cli.command('add-book')
def add_book():
    count = 5
    YEAR_FIRST_BOOK = -4000
    NOW_YEARS = 2023
    MIN_INSTANCE = 1
    MAX_INSTANCE = 10000
    for book in range(1, count + 1):
        new_book = Book(name=f'name{book}',
                        year=random.randint(YEAR_FIRST_BOOK, NOW_YEARS),
                        count_instance=random.randint(MIN_INSTANCE, MAX_INSTANCE),
                        author_id=random.choice([1, 2, 3]))
        db.session.add(new_book)
    db.session.commit()
    print('Add book')


@app.route('/show-books/')
def show_books():
    books = Book.query.all()
    authors = Author.query.all()
    context = {'books': books,
               'authors': authors}
    return render_template('page02.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
