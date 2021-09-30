import sys
from PyQt5 import QtWidgets
from qt_ui import Ui_Form


class GUI_setup(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GUI_setup()
    w.show()
    sys.exit(app.exec_())

