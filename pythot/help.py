# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(975, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/book.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpWindow.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HelpWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.navigation = QtWidgets.QTabWidget(HelpWindow)
        self.navigation.setMaximumSize(QtCore.QSize(300, 16777215))
        self.navigation.setObjectName("navigation")
        self.contents = QtWidgets.QWidget()
        self.contents.setObjectName("contents")
        self.navigation.addTab(self.contents, "")
        self.index = QtWidgets.QWidget()
        self.index.setObjectName("index")
        self.navigation.addTab(self.index, "")
        self.horizontalLayout.addWidget(self.navigation)
        self.helpBrowser = HelpBrowser(HelpWindow)
        self.helpBrowser.setObjectName("helpBrowser")
        self.horizontalLayout.addWidget(self.helpBrowser)

        self.retranslateUi(HelpWindow)
        self.navigation.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Manuel"))
        self.navigation.setTabText(self.navigation.indexOf(self.contents), _translate("HelpWindow", "Contents"))
        self.navigation.setTabText(self.navigation.indexOf(self.index), _translate("HelpWindow", "Index"))

from pythot.pythot import HelpBrowser
from . import resources_rc
