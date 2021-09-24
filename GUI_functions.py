import sys
import _thread as thread
import threading
from time import sleep
from PyQt5 import QtWidgets
from Variables import VAR_class
from GUI import Ui_Sim
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class GUI_setup(QtWidgets.QMainWindow, threading.Thread):
    def __init__(self, variables, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vars = variables

        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.ui = Ui_Sim()
        self.ui.setupUi(self)
        self.ui.amountBotsSlider.valueChanged.connect(self.botSlider)
        self.ui.amountBotsSlider_2.valueChanged.connect(self.mutationRate)
        self.ui.FPSSlider.valueChanged.connect(self.FPS)
        self.ui.maxVelocitySlider.valueChanged.connect(self.velocity)

    def showUI(self):
        self.show()

    def plotThreading(self, x, y):
        thr = threading.Thread(target=plot, args=(x,y,))
        thr.start()

    def plot(self, x, y):
        self.graphWidget.plot(x, y)

    def velocity(self):
        self.vars.params.max_vel = self.ui.maxVelocitySlider.value()

    def FPS(self):
        self.vars.params.fps = self.ui.FPSSlider.value()
        print(self.vars.params.fps)

    def mutationRate(self):
        self.vars.params.mutation_rate = self.ui.amountBotsSlider_2.value()

    def botSlider(self):
        slider_bots = self.ui.amountBotsSlider.value()
        self.vars.params.min_bots = slider_bots