# 1. Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, world!"
# 2. Добавьте две дополнительных страницы: "about", "contact"
# 3. Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму
# 4. Написать функцию, которая будет принимать на вход строку и выводить на экран её длину
# 5. Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая страница"
# и абзацем "Привет, мир!"
# 6. Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл"
# Данные о студентах должны быть переданы в шаблон через контекст

# 7. Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.
from flask import Flask
# 5.
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/about/')
def about():
    return "#"


@app.route('/contact/')
def contact():
    return "#"


@app.route('/sum/<int:num1>/<int:num2>/')
def sum(num1, num2):
    return f'Сумма чисел {num1} и {num2} = {num1 + num2}'


@app.route('/<str>')
def len_str(str):
    return f'Длина строки {str} = {len(str)}'


# 5.
@app.route('/index/')
def index():
    return render_template('index.html')


# 6.
@app.route('/table/')
def table():
    context_1 = [
        {'name': 'Ivan',
         'lastname': 'Ivanov',
         'age': 21,
         'average_score': 4.5},
        {'name': 'John',
         'lastname': 'Johnson',
         'age': 33,
         'average_score': 4.0},
        {'name': 'Alisa',
         'lastname': 'Seleznova',
         'age': 28,
         'average_score': 5.0}
    ]
    return render_template('table.html', context=context_1)

@app.route('/news/')
def news():
    news = [
        {'name': 'news1',
         'description': 'description1',
         'data': '21.12.2023'},
        {'name': 'news2',
         'description': 'description2',
         'data': '21.11.2023'},
        {'name': 'news3',
         'description': 'description3',
         'data': '21.10.2023'}
    ]
    return render_template('news.html', context=news)


if __name__ == '__main__':
    app.run()
