# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить".
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где
# будет выведеное число и его квадрат


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enter_number/', methods=['GET', 'POST'])
def enter_number():
    if request.method == 'POST':
        number = request.form.get('number')
        result_number = int(number) * int(number)
        return render_template('square_number.html', number=number, result_number=result_number)
    return render_template('enter_number.html')


if __name__ == '__main__':
    app.run(debug=True)
