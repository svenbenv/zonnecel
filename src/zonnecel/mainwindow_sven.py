from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 728)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(150, 100, 621, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plot_widget = PlotWidget(self.verticalLayoutWidget)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout.addWidget(self.plot_widget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)

        self.initial_value = QDoubleSpinBox(self.verticalLayoutWidget)
        self.initial_value.setObjectName(u"initial_value")
        self.initial_value.setDecimals(2)
        self.initial_value.setMaximum(3.300000000000000)
        self.initial_value.setSingleStep(0.100000000000000)
        self.initial_value.setStepType(QAbstractSpinBox.DefaultStepType)

        self.gridLayout.addWidget(self.initial_value, 1, 2, 1, 1)

        self.save_button = QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName(u"save_button")

        self.gridLayout.addWidget(self.save_button, 0, 2, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.start_button = QPushButton(self.verticalLayoutWidget)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout.addWidget(self.start_button, 0, 0, 1, 1)

        self.number = QSpinBox(self.verticalLayoutWidget)
        self.number.setObjectName(u"number")
        self.number.setMinimum(1)
        self.number.setMaximum(10)
        self.number.setValue(3)

        self.gridLayout.addWidget(self.number, 3, 2, 1, 1)

        self.final_value = QDoubleSpinBox(self.verticalLayoutWidget)
        self.final_value.setObjectName(u"final_value")
        self.final_value.setDecimals(2)
        self.final_value.setMaximum(3.300000000000000)
        self.final_value.setSingleStep(0.100000000000000)
        self.final_value.setValue(3.300000000000000)

        self.gridLayout.addWidget(self.final_value, 2, 2, 1, 1)

        self.port_name = QComboBox(self.verticalLayoutWidget)
        self.port_name.setObjectName(u"port_name")

        self.gridLayout.addWidget(self.port_name, 4, 2, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 994, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Final value", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of measurements", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save as csv-file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Initial value", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start experiment", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Port name", None))
    # retranslateUi