# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна(шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы
# Например,# 7. Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# # Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# # Данные о новостях должны быть переданы в шаблон через контекст.
#
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()