#!/usr/bin/env python3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

import resources
import equations

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("pythot.ui")

    QFontDatabase.addApplicationFont(":/fonts/lmroman10-bolditalic.otf")
    QFontDatabase.addApplicationFont(":/fonts/lmroman10-regular.otf")

    main_window = ui.window()
    main_window.show()
    sys.exit(app.exec_())

# vim: fdm=indent
