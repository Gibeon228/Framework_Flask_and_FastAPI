# Создать страницу, на которой будет форма для ввода двух чисел и
# выбор операции(сложение, вычитание, умножение и деление).
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу
# с результатом


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calc_page():
    if request.method == 'POST':
        numbers1 = request.form.get('number1')
        numbers2 = request.form.get('number2')
        if request.form.get('sum') is not None:
            operation = " + "
            numbers_result = int(numbers1) + int(numbers2)
        elif request.form.get('sub') is not None:
            operation = " - "
            numbers_result = int(numbers1) - int(numbers2)
        elif request.form.get('mult') is not None:
            operation = " * "
            numbers_result = int(numbers1) * int(numbers2)
        else:
            operation = " / "
            numbers_result = int(numbers1) / int(numbers2)
        return render_template('two_numbers_result.html', numbers1=numbers1, numbers2=numbers2,
                               numbers_result=numbers_result, operation=operation)
    return render_template('input_two_numbers.html')


if __name__ == '__main__':
    app.run(debug=True)
