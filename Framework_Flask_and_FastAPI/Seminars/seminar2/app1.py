# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход
# на другую страницу с приветствием пользователя по имени

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name/')
def name():
    name1 = 'Ivan '
    return render_template('greetings.html', name=name1)


if __name__ == '__main__':
    app.run(debug=True)
