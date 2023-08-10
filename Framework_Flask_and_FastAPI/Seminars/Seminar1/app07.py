# 7. Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

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
