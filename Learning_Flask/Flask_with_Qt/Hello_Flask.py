import sys

from PyQt5 import QtWidgets
from flask import Flask
from flask_restful import Resource, Api

from qt_ui import Ui_Form

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world', 'Hey': 'hoi'}

class GUI_setup(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app_GUI = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    api.add_resource(HelloWorld, '/')
    app.run(debug=True)