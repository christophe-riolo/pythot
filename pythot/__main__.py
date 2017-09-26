#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from . import pythot


app = QApplication(sys.argv)

QFontDatabase.addApplicationFont(":/fonts/lmmath.otf")
QFontDatabase.addApplicationFont(":/fonts/lmregular.otf")

main_window = pythot.Pythot()
main_window.show()

# Dirty hack to finally display the first equation.
main_window.actionAnnuler.trigger()
sys.exit(app.exec_())

# vim: fdm=indent
