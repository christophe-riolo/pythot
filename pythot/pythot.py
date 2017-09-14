"""Defines the classes used to specialize the basic
Qt classes.

Pythot : main window
OperationPrompt: modal window used to ask the operation being made.
"""

import re
from os.path import dirname
from operator import add, sub, mul, truediv, inv, neg
from fractions import Fraction as F
from sympy import S

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget, QFileDialog, QTextBrowser
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtHelp import QHelpEngine

from .window import Ui_MainWindow
from .operation import Ui_operation
from .equations import Operation
from .about import Ui_about


def str_to_fraction(numerator, denominator="1"):
    """Simple function to make a fraction out of two strings.

    >>> str_to_fraction("3,2")
    3.2
    >>> str_to_fraction("3", "4")
    3/4
    >>> type(str_to_fraction("3", "4"))
    <class 'sympy.core.numbers.Rational'>
    """

    # Decimals may be written with a comma instead of dot (French style).
    numerator = numerator.replace(",", ".")
    denominator = denominator.replace(",", ".")

    # Imposing compulsory zero before dot/comma
    num = re.compile("-?\d+.?\d*")
    if num.fullmatch(numerator) and num.fullmatch(denominator):
        return S(F(F(numerator), F(denominator)))
    else:
        return None


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

        self.setupUi(self)
        self.toDecimal()

    def onActionNeg(self):
        """Instanctiates an Operation on a request of negating the equation.
        """
        self.equations.update(Operation(operator=neg))

    def onActionInv(self):
        """Instanctiates an Operation on a request of inverting the equation.
        """
        self.equations.update(Operation(operator=inv))

    def toFraction(self):
        self.mode = "fraction"
        self.statusbar.showMessage("Mode : fraction")

    def toDecimal(self):
        self.mode = "decimal"
        self.statusbar.showMessage("Mode : decimal")

    def operationPrompt(self):
        """Starts the prompt to get the current operation."""
        sender = self.sender().objectName()
        prompt = OperationPrompt(self, **Pythot.operation_actions[sender])
        self.actionMode_fraction.triggered.connect(prompt.toFraction)
        self.actionMode_d_cimal.triggered.connect(prompt.toDecimal)
        prompt.exec()

    def aboutWindow(self):
        about = About(self)
        about.show()

    def savePrompt(self):
        filename = QFileDialog.getSaveFileName(
                self,
                "Sauvegarder un fichier équations",
                "*.ptht",
                "Pythot files (*.ptht)")
        if filename == ('', ''):
            return
        self.equations.saveToFile(*filename)

    def openPrompt(self):
        filename = QFileDialog.getOpenFileName(
                self,
                "Ouvrir un fichier équations",
                "*.ptht",
                "Pythot files (*.ptht)")
        if filename == ('', ''):
            return
        self.equations.loadFromFile(*filename)

    def showHelp(self):
        HelpWindow().show()


class About(QDialog, Ui_about):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)


class OperationPrompt(QDialog, Ui_operation):
    """Stores the operation asked in this dialog, to send it as a signal."""

    make_operation = pyqtSignal(Operation)

    def __init__(self, parent, operator, x=False):
        super().__init__(parent)

        self.operator = operator
        self._x = S("x") if x else 1

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

        self.make_operation.connect(self.parent().equations.update)

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
                if denominator and self.parent().mode == "fraction"
                else "1"
                )

        self.make_operation.emit(
            Operation(
                operator=self.operator,
                operand=str_to_fraction(numerator, denominator) * self._x
            )
        )
        super().accept()

    def toDecimal(self):
        self.fraction_line.hide()
        self.denominator.hide()

    def toFraction(self):
        self.fraction_line.show()
        self.denominator.show()


class HelpBrowser(QTextBrowser):
    def __init__(self, help_engine):
        super().__init__()
        self.help_engine = help_engine

    def loadResource(self, type_, name):
        if name.scheme() == "qthelp":
            return self.help_engine.fileData(name)
        else:
            return super().loadResource(type_, name)


from .help import Ui_HelpWindow


class HelpWindow(QWidget, Ui_HelpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.help_engine = QHelpEngine(dirname(__file__)  + "/doc/doc.qhc")
        self.help_engine.setupData()
        self.helpBrowser = HelpBrowser(self.help_engine)
        self.contents = self.help_engine.contentWidget()
        self.index = self.help_engine.indexWidget()

from . import resources_rc

# vim: fdm=indent
