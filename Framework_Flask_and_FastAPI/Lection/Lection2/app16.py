from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'fe5f58c5922c17936fd8156ebf0dea53373e0ddc2b1591f6ffd948570a5a4b0c'


@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
