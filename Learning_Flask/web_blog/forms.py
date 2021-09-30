import sys

from PyQt5 import QtWidgets
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo

from Qt.qt_ui import Ui_Form


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               length(min=2, max=20)
                           ])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()
                                    ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired()
                             ])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Login')


class GUI_setup(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setup()

    def setup_thread(self):

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    sys.exit(app.exec_())

