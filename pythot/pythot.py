"""Defines the classes used to specialize the basic
Qt classes.

Pythot : main window
OperationPrompt: modal window used to ask the operation being made.
"""

from operator import add, sub, mul, truediv, inv, neg
from fractions import Fraction as F
from sympy import S

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal

from .window import Ui_MainWindow
from .operation import Ui_operation
from .equations import Operation, Equations


class Pythot(QMainWindow, Ui_MainWindow):
    """Main application window. Specializes QMainWindow.
    """
    operation_actions = {
            "actionAjouter_un_nombre": {"operator": add},
            "actionSoustraire_un_nombre": {"operator": sub},
            "actionAjouter_un_terme_en_x": {"operator": add, "x": True},
            "actionSoustraire_un_terme_en_x": {"operator": sub, "x": True},
            "actionMultiplier_par_un_nombre": {"operator": mul},
            "actionDiviser_par_un_nombre": {"operator": truediv},
            "actionIntervertir_les_deux_membres": {"operator": inv},
            "actionPrendre_l_oppos": {"operator": neg},
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mode = "decimal"
        self.equations = Equations(*args, **kwargs)

        self.setupUi(self)

    def onActionNeg(self):
        """Instanctiates an Operation on a request of negating the equation.
        """
        self.equations.update(Operation(neg))

    def onActionInv(self):
        """Instanctiates an Operation on a request of inverting the equation.
        """
        self.equations.update(Operation(inv))

    def operationPrompt(self):
        """Starts the prompt to get the current operation."""
        sender = self.sender().objectName()
        prompt = OperationPrompt(self, **Pythot.operation_actions[sender])
        prompt.exec()


class OperationPrompt(QDialog, Ui_operation):
    """Stores the operation asked in this dialog, to send it as a signal."""

    make_operation = pyqtSignal(Operation)

    def __init__(self, parent, operator, x=False):
        super().__init__(parent)

        self.operator = operator

        self.setupUi(self)

        # I am not going to allow any other mode.
        mode = self.parent().mode
        if mode == "fraction":
            self.toFraction()
        else:
            self.toDecimal()

        if x:
            self.x.show()
        else:
            self.x.hide()


    def retranslateUi(self, operation):
        """Sets the text left of the input accordingly to the
        operation we are doing.
        """
        # We specialize only the text, so let's invoke super()
        super().retranslateUi(self)

        # we might want to translate later
        _translate = QtCore.QCoreApplication.translate
        if self.operator is add:
            self.text.setText(_translate("operation", "Ajouter aux deux membres de l\'équation :"))
        if self.operator is sub:
            self.text.setText(_translate("operation", "Soustraire aux deux membres de l\'équation :"))
        if self.operator is mul:
            self.text.setText(_translate("operation", "Multiplier les deux membres de l\'équation par :"))
        if self.operator is truediv:
            self.text.setText(_translate("operation", "Diviser les deux membres de l\'équation par :"))
        # OperationPrompt should not be created for neg and inv

    def accept(self):
        """Sending signal make_operation before accepting."""
        numerator = self.numerator.text()
        denominator = self.denominator.text()

        numerator = numerator if numerator else "0"
        denominator = (
                denominator
                if denominator and self.mode == "fraction"
                else "1"
                )

        self.make_operation.emit(
            Operation(
                self.operator,
                S(F(F(numerator), F(denominator)))
            )
        )
        super().accept()

    def toDecimal(self):
        self.fraction_line.hide()
        self.denominator.hide()

    def toFraction(self):
        self.fraction_line.show()
        self.denominator.show()

# vim: fdm=indent
