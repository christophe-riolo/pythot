# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_operation(object):
    def setupUi(self, operation):
        operation.setObjectName("operation")
        operation.resize(566, 172)
        font = QtGui.QFont()
        font.setFamily("LM Roman 9")
        operation.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/thot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        operation.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(operation)
        self.gridLayout.setObjectName("gridLayout")
        self.x = QtWidgets.QLabel(operation)
        self.x.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.x.setFont(font)
        self.x.setObjectName("x")
        self.gridLayout.addWidget(self.x, 0, 2, 1, 1)
        self.value = QtWidgets.QWidget(operation)
        self.value.setMinimumSize(QtCore.QSize(0, 50))
        self.value.setMaximumSize(QtCore.QSize(50, 70))
        self.value.setObjectName("value")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.value)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.numerator = QtWidgets.QLineEdit(self.value)
        self.numerator.setMinimumSize(QtCore.QSize(0, 20))
        self.numerator.setFrame(True)
        self.numerator.setAlignment(QtCore.Qt.AlignCenter)
        self.numerator.setObjectName("numerator")
        self.verticalLayout.addWidget(self.numerator)
        self.fraction_line = QtWidgets.QFrame(self.value)
        self.fraction_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fraction_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fraction_line.setObjectName("fraction_line")
        self.verticalLayout.addWidget(self.fraction_line)
        self.denominator = QtWidgets.QLineEdit(self.value)
        self.denominator.setMinimumSize(QtCore.QSize(0, 20))
        self.denominator.setFrame(True)
        self.denominator.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator.setObjectName("denominator")
        self.verticalLayout.addWidget(self.denominator)
        self.gridLayout.addWidget(self.value, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(operation)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 3)
        self.text = QtWidgets.QLabel(operation)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Roman")
        font.setPointSize(14)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)

        self.retranslateUi(operation)
        self.buttonBox.accepted.connect(operation.accept)
        self.buttonBox.rejected.connect(operation.reject)
        self.buttonBox.rejected.connect(self.numerator.clear)
        self.buttonBox.rejected.connect(self.denominator.clear)
        QtCore.QMetaObject.connectSlotsByName(operation)

    def retranslateUi(self, operation):
        _translate = QtCore.QCoreApplication.translate
        operation.setWindowTitle(_translate("operation", "Dialog"))
        self.x.setText(_translate("operation", "x"))
        self.text.setText(_translate("operation", "Ajouter aux deux membres de l\'équation :"))

from . import resources_rc
