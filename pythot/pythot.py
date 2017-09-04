from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal

from .window import Ui_MainWindow
from .operation import Ui_operation
from . import equations


class Pythot(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class OperationPrompt(QDialog, Ui_operation):
    """Stores the operation asked in this dialog, to send it as a signal."""

    make_operation = pyqtSignal(equations.Operation)

    def __init__(self, operation):
        super().__init__()
        self.operation = operation
        self.setupUi(self)

    def accept(self):
        """Sending signal make_operation before accepting."""
        self.make_operation.emit(self.operation)
        super().accept()

# vim: fdm=indent
