# Создать страницу, на которой форма для ввода логина и пароля,
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход
# на страницу с ошибкой

from flask import Flask, render_template, request

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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    user_login = 'qwerty'
    user_password ='123'
    if request.method == 'POST':
        login1 = request.form['login']
        password1 = request.form['password']
        print(login1, password1)
        if login1 == user_login and password1 == user_password:
            return render_template('greetings.html', name=login1)
        return render_template('error.html')
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
