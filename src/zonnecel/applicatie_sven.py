# 4-12-2023
# Sven Verhaaf
# 14641399

import csv
import sys

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

from zonnecel.controller_sven import list_devices
from zonnecel.model_sven import DiodeExperiment
from zonnecel.mainwindow_sven import Ui_MainWindow

# Color of background and foreground of the graph is set
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

# Class of graphical user interface
class UserInterface(QtWidgets.QMainWindow):

    """Graphical User Interface class to plot UI-characteristic for a certain device."""

    def __init__(self):

        """Defines initial functions.
        A portname can be chosen in the GUI (graphical user interface).
        When the start button is clicked, the experiment is started.
        The save button saves the data as csv-file.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.port_name.addItems(list_devices())

        self.ui.start_button.clicked.connect(self.ui.plot_widget.clear)
        self.ui.start_button.clicked.connect(self.plot)
        self.ui.save_button.clicked.connect(self.save)

    def plot(self):
        """The plot function is defined, where the user can choose the range and number of experiments."""

        self.diode = DiodeExperiment(
            self.ui.initial_value.value(),
            self.ui.final_value.value(),
            self.ui.number.value(),
        )
        self.diode.scan(self.ui.port_name.currentText())
        self.ui.plot_widget.plot(
            self.diode.average_U_list,
            self.diode.average_I_list,
            symbol="o",
            symbolSize=5,
            pen=None,
        )
        self.ui.plot_widget.setLabel("left", "current in Ampère")
        self.ui.plot_widget.setLabel("bottom", "voltage in Volt")
        error_bars = pg.ErrorBarItem(
            x=np.array(self.diode.average_U_list),
            y=np.array(self.diode.average_I_list),
            width=2 * np.array(self.diode.U_error),
            height=2 * np.array(self.diode.I_error),
        )

        self.ui.plot_widget.addItem(error_bars)
        self.show()

    def save(self):
        """The save function is defined, where the data is saved in a csv-file."""
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        with open(f"{filename}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for a, b, c, d in zip(
                self.diode.average_U_list,
                self.diode.U_error,
                self.diode.average_I_list,
                self.diode.I_error,
            ):
                writer.writerow([a, b, c, d])


def main():
    """Activates application"""
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()