# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма загрузки изображений

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name/')
def name():
    name1 = 'Ivan '
    return render_template('greetings.html', name=name1)

@app.route('/pic/')
def pic_page():
    return render_template('pic.html')

@app.route('/upload/')
def upload():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
