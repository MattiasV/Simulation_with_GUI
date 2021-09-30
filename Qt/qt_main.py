import sys
import _thread as thread
import threading
from time import sleep
from PyQt5 import QtWidgets

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class GUI_setup(QtWidgets.QMainWindow, threading.Thread):
    def __init__(self, variables, *args, **kwargs):
        super().__init__(*args, **kwargs)


