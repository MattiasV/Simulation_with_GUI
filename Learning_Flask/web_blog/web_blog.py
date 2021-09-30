import sys

from PyQt5 import QtWidgets
from flask import Flask, url_for, request, render_template, flash, redirect
from forms import RegistrationForm, LoginForm, GUI_setup

app = Flask(__name__)

app.config['SECRET_KEY'] = '71ce07a1c86cec6d5199660b9037a471'

posts = [
    {
        'author': 'Corey Shafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20 2018'
    }, {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title=register, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mattias.vandecauter@gmail.com' and form.password.data == 't':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title=login, form=form)


if __name__ == "__main__":
    app_GUI = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    app.run(debug=False, host='0.0.0.0')
    sys.exit(app_GUI.exec_())
