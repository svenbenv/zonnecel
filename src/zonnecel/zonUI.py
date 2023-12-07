import sys
import csv
import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

#from  import 


# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
       
        super().__init__()
        self.plot_widget = pg.PlotWidget()
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.plot_widget.setLabel("left", "Voltage in V")
        self.plot_widget.setLabel("bottom", "Current in A")

        # central layout
        vbox = QtWidgets.QVBoxLayout(central_widget)
        # self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.plot_widget)
        hbox = QtWidgets.QHBoxLayout()
        hbox1 = QtWidgets.QHBoxLayout()
        hbox2 = QtWidgets.QHBoxLayout()
        hbox3 = QtWidgets.QHBoxLayout()
        hbox4 = QtWidgets.QHBoxLayout()
        hboxpoortlabel = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)
        vbox.addLayout(hboxpoortlabel)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

