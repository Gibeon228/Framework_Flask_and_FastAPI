from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect

from form04 import RegistationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'6ac1f2535965e50a28d9af209f2707408003dff10d64054dea3414a807ac60c5'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
