#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import resources

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("pythot.ui")
    main_window = ui.window()
    main_window.show()
    sys.exit(app.exec_())
