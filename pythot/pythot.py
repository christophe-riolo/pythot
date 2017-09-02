#!/usr/bin/env python3
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow

from .window import Ui_MainWindow
from . import equations


class Pythot(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Pythot()

    QFontDatabase.addApplicationFont(":/fonts/lmroman10-bolditalic.otf")
    QFontDatabase.addApplicationFont(":/fonts/lmroman10-regular.otf")

    main_window.show()
    sys.exit(app.exec_())

# vim: fdm=indent
