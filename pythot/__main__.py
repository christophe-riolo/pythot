#!/usr/bin/env python3
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from .import pythot


app = QApplication(sys.argv)
main_window = pythot.Pythot()

QFontDatabase.addApplicationFont(":/fonts/lmroman10-bolditalic.otf")
QFontDatabase.addApplicationFont(":/fonts/lmroman10-regular.otf")

main_window.show()
sys.exit(app.exec_())

# vim: fdm=indent
