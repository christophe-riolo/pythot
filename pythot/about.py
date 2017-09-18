# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(508, 345)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/thot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about.setWindowIcon(icon)
        about.setAutoFillBackground(False)
        about.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(about)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(about)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(about)
        self.pushButton.clicked.connect(about.accept)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "Dialog"))
        self.label.setText(_translate("about", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Pythot v1.0.1bbb</span></p><p align=\"center\"><span style=\" font-size:12pt;\">17/09/2017</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Based on </span><a href=\"http://www.emmanuelmorand.net/thot/presentation.php\"><span style=\" font-size:12pt; text-decoration: underline; color:#2980b9;\">software Thot</span></a><span style=\" font-size:12pt;\"> by Emmanuel Morand,<br/>whom we thank for his authorization.</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Source code at : </span><a href=\"https://github.com/christophe-riolo/pythot\"><span style=\" font-size:12pt; text-decoration: underline; color:#2980b9;\">https://github.com/christophe-riolo/pythot</span></a></p><p align=\"center\">Icons made by <a href=\"https://www.flaticon.com/authors/madebyoliver\"><span style=\" text-decoration: underline; color:#2980b9;\">Madebyoliver</span></a>, <a href=\"https://www.flaticon.com/authors/vignesh-oviyan\"><span style=\" text-decoration: underline; color:#2980b9;\">Vignesh Oviyan</span></a>, <a href=\"http://www.freepik.com\"><span style=\" text-decoration: underline; color:#2980b9;\">Freepik</span></a>, <a href=\"https://www.flaticon.com/authors/vaadin\"><span style=\" text-decoration: underline; color:#2980b9;\">Vaadin</span></a>, <a href=\"https://www.flaticon.com/authors/those-icons\"><span style=\" text-decoration: underline; color:#2980b9;\">Those Icons</span></a><br/>from <a href=\"https://www.flaticon.com/\"><span style=\" text-decoration: underline; color:#2980b9;\">www.flaticon.com</span></a> are licensed by <a href=\"http://creativecommons.org/licenses/by/3.0/\"><span style=\" text-decoration: underline; color:#2980b9;\">CC 3.0 BY</span></a></p></body></html>"))
        self.pushButton.setText(_translate("about", "Ok"))

from . import resources_rc
