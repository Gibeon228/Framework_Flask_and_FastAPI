# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить".
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом
# или на страницу с ошибкой в случае некорректного возраста


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Не совсем понятно, что имеется в виду под корректным возрастом, я выбрал больше 18.
# Можно было, конечно, сделать возможным ввод текста, но зачем.
@app.route('/name_age/', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        COMING_OF_AGE = 18
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= COMING_OF_AGE:
            return render_template('greetings.html', name=name)
        return render_template('error.html')
    return render_template('name_age.html')


if __name__ == '__main__':
    app.run(debug=True)
