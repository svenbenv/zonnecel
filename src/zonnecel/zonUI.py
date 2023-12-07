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

        # central layout
        vbox = QtWidgets.QVBoxLayout(central_widget)
        # self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.plot_widget)
        hbox = QtWidgets.QHBoxLayout()
        hbox1 = QtWidgets.QHBoxLayout()
        hbox2 = QtWidgets.QHBoxLayout()
        hbox3 = QtWidgets.QHBoxLayout()
        hboxcombo = QtWidgets.QHBoxLayout()
        hboxpoortlabel = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hboxpoortlabel)
        vbox.addLayout(hboxcombo)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        #button
        self.start_value = QtWidgets.QDoubleSpinBox()
        self.start_value.setRange(0,10)
        self.start_value.setSingleStep(0.1)
        self.start_value.setValue(0)
        hbox1.addWidget(self.start_value)

        self.stop_value = QtWidgets.QDoubleSpinBox()
        # label stoplabel = QLabel()
        self.stop_value.setRange(0,10)
        self.stop_value.setSingleStep(0.1)
        self.stop_value.setValue(10)
        hbox1.addWidget(self.stop_value)

        self.repeat_times = QtWidgets.QSpinBox()
        self.repeat_times.setValue(1)
        self.repeat_times.setRange(1, 30)
        hbox1.addWidget(self.repeat_times)

        graph_button = QtWidgets.QPushButton("graph")
        hbox2.addWidget(graph_button)

        clear_button = QtWidgets.QPushButton("clear")
        hbox2.addWidget(clear_button)

        save_button = QtWidgets.QPushButton("save")
        hbox3.addWidget(save_button)

        Quit_button = QtWidgets.QPushButton("quit")
        hbox3.addWidget(Quit_button)

        self.selectplot = QtWidgets.QComboBox()
        item = ["UI", "PR"]
        self.selectplot.addItems(item)
        hboxcombo.addWidget(self.selectplot)


        #poort comboButton
        # self.selectAD = QtWidgets.QComboBox()
        # poort = list_devices()
        # for item in poort:
        #     self.selectAD.addItem(item)
        # hbox2.addWidget(self.selectAD)

        #Push buttons

    
        #labels
        label_start = QtWidgets.QLabel("start")
        hbox.addWidget(label_start)

        label_stop = QtWidgets.QLabel("stop")
        hbox.addWidget(label_stop)

        label_repeat = QtWidgets.QLabel("times repeat")
        hbox.addWidget(label_repeat)



        #clicked
        graph_button.clicked.connect(self.UI_plot)
        save_button.clicked.connect(self.save_data)
        clear_button.clicked.connect(self.clear)
        Quit_button.clicked.connect(self.close)
#@Slot
    def UI_plot():
        """plot UI-diagram
        """
        self.plot_widget.clear() 
        measurement = DiodeExperiment(port = self.selectAD.currentText())
        self.voltageLED, self.amperage, self.Aerror, self.Verror = measurement.scan(
            start=int(self.start_value.value() / 3.3 * 1024), 
            stop= int(self.stop_value.value()/ 3.3 * 1024),
            n=self.repeat_times.value())

        # plot voltageLED over amperage
        
        self.plot_widget.setLabel("left", "Voltage in V")
        self.plot_widget.setLabel("bottom", "Current in A")

        self.plot_widget.plot(self.voltageLED, self.amperage, symbol="o", symbolSize=5, pen=None)
        error_bars = pg.ErrorBarItem(x=np.array(self.voltageLED), y=np.array(self.amperage), width=2 * np.array(self.Verror), height=2 * np.array(self.Aerror))
        self.plot_widget.addItem(error_bars)

        #close device
        measurement.close()

    
    def clear(self):
        """
        clear up the plot widget
        """
        self.plot_widget.clear() 
    
    def save_data(self):
        """
        Save measured data in Csv-sile
        """
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        print(filename)
        with open(f"{filename}", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["V", "A","V_err","A_err"])
            for a, b, c, d in zip(self.voltageLED, self.amperage, self.Verror, self.Aerror):
                writer.writerow([a, b, c, d])

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  