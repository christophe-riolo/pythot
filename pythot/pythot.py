from PyQt5.QtWidgets import QMainWindow

from .window import Ui_MainWindow
from . import equations


class Pythot(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# vim: fdm=indent
