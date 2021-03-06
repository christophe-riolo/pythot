# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/thot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon1)
        self.open.setIconSize(QtCore.QSize(20, 20))
        self.open.setFlat(True)
        self.open.setObjectName("open")
        self.horizontalLayout_7.addWidget(self.open)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setIconSize(QtCore.QSize(20, 20))
        self.save.setFlat(True)
        self.save.setObjectName("save")
        self.horizontalLayout_7.addWidget(self.save)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_7.addWidget(self.line_9)
        self.new_equation = QtWidgets.QPushButton(self.centralwidget)
        self.new_equation.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_equation.setIcon(icon3)
        self.new_equation.setIconSize(QtCore.QSize(20, 20))
        self.new_equation.setFlat(True)
        self.new_equation.setObjectName("new_equation")
        self.horizontalLayout_7.addWidget(self.new_equation)
        self.random = QtWidgets.QPushButton(self.centralwidget)
        self.random.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/random.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.random.setIcon(icon4)
        self.random.setIconSize(QtCore.QSize(20, 20))
        self.random.setFlat(True)
        self.random.setObjectName("random")
        self.horizontalLayout_7.addWidget(self.random)
        self.empty = QtWidgets.QPushButton(self.centralwidget)
        self.empty.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/clear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.empty.setIcon(icon5)
        self.empty.setIconSize(QtCore.QSize(20, 20))
        self.empty.setFlat(True)
        self.empty.setObjectName("empty")
        self.horizontalLayout_7.addWidget(self.empty)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_7.addWidget(self.line_10)
        self.fraction = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fraction.setFont(font)
        self.fraction.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Q.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fraction.setIcon(icon6)
        self.fraction.setIconSize(QtCore.QSize(20, 20))
        self.fraction.setFlat(True)
        self.fraction.setObjectName("fraction")
        self.horizontalLayout_7.addWidget(self.fraction)
        self.decimal = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.decimal.setFont(font)
        self.decimal.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/D.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decimal.setIcon(icon7)
        self.decimal.setIconSize(QtCore.QSize(20, 20))
        self.decimal.setFlat(True)
        self.decimal.setObjectName("decimal")
        self.horizontalLayout_7.addWidget(self.decimal)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_7.addWidget(self.line_11)
        self.zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/zoom-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon8)
        self.zoom_in.setIconSize(QtCore.QSize(20, 20))
        self.zoom_in.setFlat(True)
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout_7.addWidget(self.zoom_in)
        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/zoom-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon9)
        self.zoom_out.setIconSize(QtCore.QSize(20, 20))
        self.zoom_out.setFlat(True)
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout_7.addWidget(self.zoom_out)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_7.addWidget(self.line_12)
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/book.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon10)
        self.help.setIconSize(QtCore.QSize(20, 20))
        self.help.setFlat(True)
        self.help.setObjectName("help")
        self.horizontalLayout_7.addWidget(self.help)
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setText("")
        self.about.setIcon(icon)
        self.about.setIconSize(QtCore.QSize(20, 20))
        self.about.setFlat(True)
        self.about.setObjectName("about")
        self.horizontalLayout_7.addWidget(self.about)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_num = QtWidgets.QPushButton(self.centralwidget)
        self.add_num.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_num.setIcon(icon11)
        self.add_num.setIconSize(QtCore.QSize(40, 40))
        self.add_num.setFlat(True)
        self.add_num.setObjectName("add_num")
        self.horizontalLayout_4.addWidget(self.add_num)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_4.addWidget(self.line_13)
        self.sub_num = QtWidgets.QPushButton(self.centralwidget)
        self.sub_num.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sub_num.setIcon(icon12)
        self.sub_num.setIconSize(QtCore.QSize(40, 40))
        self.sub_num.setFlat(True)
        self.sub_num.setObjectName("sub_num")
        self.horizontalLayout_4.addWidget(self.sub_num)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout_4.addWidget(self.line_14)
        self.add_x = QtWidgets.QPushButton(self.centralwidget)
        self.add_x.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/plus-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_x.setIcon(icon13)
        self.add_x.setIconSize(QtCore.QSize(40, 40))
        self.add_x.setFlat(True)
        self.add_x.setObjectName("add_x")
        self.horizontalLayout_4.addWidget(self.add_x)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.horizontalLayout_4.addWidget(self.line_15)
        self.sub_x = QtWidgets.QPushButton(self.centralwidget)
        self.sub_x.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/minus-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sub_x.setIcon(icon14)
        self.sub_x.setIconSize(QtCore.QSize(40, 40))
        self.sub_x.setFlat(True)
        self.sub_x.setObjectName("sub_x")
        self.horizontalLayout_4.addWidget(self.sub_x)
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout_4.addWidget(self.line_16)
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/times.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mult.setIcon(icon15)
        self.mult.setIconSize(QtCore.QSize(40, 40))
        self.mult.setFlat(True)
        self.mult.setObjectName("mult")
        self.horizontalLayout_4.addWidget(self.mult)
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.horizontalLayout_4.addWidget(self.line_17)
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/div.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.div.setIcon(icon16)
        self.div.setIconSize(QtCore.QSize(40, 40))
        self.div.setFlat(True)
        self.div.setObjectName("div")
        self.horizontalLayout_4.addWidget(self.div)
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.horizontalLayout_4.addWidget(self.line_18)
        self.exchange = QtWidgets.QPushButton(self.centralwidget)
        self.exchange.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/exchange.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exchange.setIcon(icon17)
        self.exchange.setIconSize(QtCore.QSize(40, 40))
        self.exchange.setFlat(True)
        self.exchange.setObjectName("exchange")
        self.horizontalLayout_4.addWidget(self.exchange)
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.horizontalLayout_4.addWidget(self.line_19)
        self.opposite = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.opposite.setFont(font)
        self.opposite.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/opposite.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opposite.setIcon(icon18)
        self.opposite.setIconSize(QtCore.QSize(40, 40))
        self.opposite.setFlat(True)
        self.opposite.setObjectName("opposite")
        self.horizontalLayout_4.addWidget(self.opposite)
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.horizontalLayout_4.addWidget(self.line_20)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel.setIcon(icon19)
        self.cancel.setIconSize(QtCore.QSize(40, 40))
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_4.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1020, 421))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: white;")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.equations = Equations(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.equations.setFont(font)
        self.equations.setText("")
        self.equations.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.equations.setObjectName("equations")
        self.horizontalLayout.addWidget(self.equations)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 32))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOp_rations = QtWidgets.QMenu(self.menubar)
        self.menuOp_rations.setObjectName("menuOp_rations")
        self.menuAffichage = QtWidgets.QMenu(self.menubar)
        self.menuAffichage.setObjectName("menuAffichage")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir_un_fichier_quations = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_un_fichier_quations.setIcon(icon1)
        self.actionOuvrir_un_fichier_quations.setObjectName("actionOuvrir_un_fichier_quations")
        self.actionSauvegarder_un_fichier_quation = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder_un_fichier_quation.setIcon(icon2)
        self.actionSauvegarder_un_fichier_quation.setObjectName("actionSauvegarder_un_fichier_quation")
        self.actionNouvelle_quation = QtWidgets.QAction(MainWindow)
        self.actionNouvelle_quation.setIcon(icon3)
        self.actionNouvelle_quation.setObjectName("actionNouvelle_quation")
        self.action_quation_au_hasard = QtWidgets.QAction(MainWindow)
        self.action_quation_au_hasard.setIcon(icon4)
        self.action_quation_au_hasard.setObjectName("action_quation_au_hasard")
        self.actionEffacer_l_quation = QtWidgets.QAction(MainWindow)
        self.actionEffacer_l_quation.setIcon(icon5)
        self.actionEffacer_l_quation.setObjectName("actionEffacer_l_quation")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionAjouter_un_nombre = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_nombre.setIcon(icon11)
        self.actionAjouter_un_nombre.setObjectName("actionAjouter_un_nombre")
        self.actionSoustraire_un_nombre = QtWidgets.QAction(MainWindow)
        self.actionSoustraire_un_nombre.setIcon(icon12)
        self.actionSoustraire_un_nombre.setObjectName("actionSoustraire_un_nombre")
        self.actionAjouter_un_terme_en_x = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_terme_en_x.setIcon(icon13)
        self.actionAjouter_un_terme_en_x.setObjectName("actionAjouter_un_terme_en_x")
        self.actionSoustraire_un_terme_en_x = QtWidgets.QAction(MainWindow)
        self.actionSoustraire_un_terme_en_x.setIcon(icon14)
        self.actionSoustraire_un_terme_en_x.setObjectName("actionSoustraire_un_terme_en_x")
        self.actionMultiplier_par_un_nombre = QtWidgets.QAction(MainWindow)
        self.actionMultiplier_par_un_nombre.setIcon(icon15)
        self.actionMultiplier_par_un_nombre.setObjectName("actionMultiplier_par_un_nombre")
        self.actionDiviser_par_un_nombre = QtWidgets.QAction(MainWindow)
        self.actionDiviser_par_un_nombre.setIcon(icon16)
        self.actionDiviser_par_un_nombre.setObjectName("actionDiviser_par_un_nombre")
        self.actionIntervertir_les_deux_membres = QtWidgets.QAction(MainWindow)
        self.actionIntervertir_les_deux_membres.setIcon(icon17)
        self.actionIntervertir_les_deux_membres.setObjectName("actionIntervertir_les_deux_membres")
        self.actionPrendre_l_oppos = QtWidgets.QAction(MainWindow)
        self.actionPrendre_l_oppos.setIcon(icon18)
        self.actionPrendre_l_oppos.setObjectName("actionPrendre_l_oppos")
        self.actionAnnuler = QtWidgets.QAction(MainWindow)
        self.actionAnnuler.setIcon(icon19)
        self.actionAnnuler.setObjectName("actionAnnuler")
        self.actionMode_fraction = QtWidgets.QAction(MainWindow)
        self.actionMode_fraction.setCheckable(False)
        self.actionMode_fraction.setIcon(icon6)
        self.actionMode_fraction.setObjectName("actionMode_fraction")
        self.actionMode_d_cimal = QtWidgets.QAction(MainWindow)
        self.actionMode_d_cimal.setCheckable(False)
        self.actionMode_d_cimal.setChecked(False)
        self.actionMode_d_cimal.setIcon(icon7)
        self.actionMode_d_cimal.setObjectName("actionMode_d_cimal")
        self.actionAgrandir = QtWidgets.QAction(MainWindow)
        self.actionAgrandir.setIcon(icon8)
        self.actionAgrandir.setObjectName("actionAgrandir")
        self.actionR_duire = QtWidgets.QAction(MainWindow)
        self.actionR_duire.setIcon(icon9)
        self.actionR_duire.setObjectName("actionR_duire")
        self.actionAide = QtWidgets.QAction(MainWindow)
        self.actionAide.setIcon(icon10)
        self.actionAide.setObjectName("actionAide")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setIcon(icon)
        self.actionA_propos.setObjectName("actionA_propos")
        self.menuFichier.addAction(self.actionOuvrir_un_fichier_quations)
        self.menuFichier.addAction(self.actionSauvegarder_un_fichier_quation)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionNouvelle_quation)
        self.menuFichier.addAction(self.action_quation_au_hasard)
        self.menuFichier.addAction(self.actionEffacer_l_quation)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuOp_rations.addAction(self.actionAjouter_un_nombre)
        self.menuOp_rations.addAction(self.actionSoustraire_un_nombre)
        self.menuOp_rations.addAction(self.actionAjouter_un_terme_en_x)
        self.menuOp_rations.addAction(self.actionSoustraire_un_terme_en_x)
        self.menuOp_rations.addAction(self.actionMultiplier_par_un_nombre)
        self.menuOp_rations.addAction(self.actionDiviser_par_un_nombre)
        self.menuOp_rations.addAction(self.actionIntervertir_les_deux_membres)
        self.menuOp_rations.addAction(self.actionPrendre_l_oppos)
        self.menuOp_rations.addAction(self.actionAnnuler)
        self.menuAffichage.addAction(self.actionMode_fraction)
        self.menuAffichage.addAction(self.actionMode_d_cimal)
        self.menuAffichage.addSeparator()
        self.menuAffichage.addAction(self.actionAgrandir)
        self.menuAffichage.addAction(self.actionR_duire)
        self.menu.addAction(self.actionAide)
        self.menu.addAction(self.actionA_propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOp_rations.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.open.clicked.connect(self.actionOuvrir_un_fichier_quations.trigger)
        self.save.clicked.connect(self.actionSauvegarder_un_fichier_quation.trigger)
        self.new_equation.clicked.connect(self.actionNouvelle_quation.trigger)
        self.random.clicked.connect(self.action_quation_au_hasard.trigger)
        self.empty.clicked.connect(self.actionEffacer_l_quation.trigger)
        self.about.clicked.connect(self.actionA_propos.trigger)
        self.help.clicked.connect(self.actionAide.trigger)
        self.zoom_out.clicked.connect(self.actionR_duire.trigger)
        self.zoom_in.clicked.connect(self.actionAgrandir.trigger)
        self.decimal.clicked.connect(self.actionMode_d_cimal.trigger)
        self.fraction.clicked.connect(self.actionMode_fraction.trigger)
        self.cancel.clicked.connect(self.actionAnnuler.trigger)
        self.opposite.clicked.connect(self.actionPrendre_l_oppos.trigger)
        self.exchange.clicked.connect(self.actionIntervertir_les_deux_membres.trigger)
        self.div.clicked.connect(self.actionDiviser_par_un_nombre.trigger)
        self.mult.clicked.connect(self.actionMultiplier_par_un_nombre.trigger)
        self.sub_x.clicked.connect(self.actionSoustraire_un_terme_en_x.trigger)
        self.sub_num.clicked.connect(self.actionSoustraire_un_nombre.trigger)
        self.add_x.clicked.connect(self.actionAjouter_un_terme_en_x.trigger)
        self.add_num.clicked.connect(self.actionAjouter_un_nombre.trigger)
        self.actionQuitter.triggered.connect(MainWindow.close)
        self.actionAjouter_un_nombre.triggered.connect(MainWindow.operationPrompt)
        self.actionNouvelle_quation.triggered.connect(MainWindow.equationPrompt)
        self.actionAjouter_un_terme_en_x.triggered.connect(MainWindow.operationPrompt)
        self.actionSoustraire_un_nombre.triggered.connect(MainWindow.operationPrompt)
        self.actionSoustraire_un_terme_en_x.triggered.connect(MainWindow.operationPrompt)
        self.actionMultiplier_par_un_nombre.triggered.connect(MainWindow.operationPrompt)
        self.actionDiviser_par_un_nombre.triggered.connect(MainWindow.operationPrompt)
        self.actionIntervertir_les_deux_membres.triggered.connect(MainWindow.onActionInv)
        self.actionPrendre_l_oppos.triggered.connect(MainWindow.onActionNeg)
        self.actionEffacer_l_quation.triggered.connect(self.equations.clear_equation)
        self.actionAnnuler.triggered.connect(self.equations.cancel)
        self.action_quation_au_hasard.triggered.connect(self.equations.randomEquation)
        self.actionA_propos.triggered.connect(MainWindow.aboutWindow)
        self.actionAide.triggered.connect(MainWindow.showHelp)
        self.actionOuvrir_un_fichier_quations.triggered.connect(MainWindow.openPrompt)
        self.actionSauvegarder_un_fichier_quation.triggered.connect(MainWindow.savePrompt)
        self.actionMode_fraction.triggered.connect(MainWindow.toFraction)
        self.actionMode_d_cimal.triggered.connect(MainWindow.toDecimal)
        self.actionAgrandir.triggered.connect(self.equations.zoom_in)
        self.actionR_duire.triggered.connect(self.equations.zoom_out)
        self.actionMode_d_cimal.triggered.connect(self.equations.to_decimal)
        self.actionMode_fraction.triggered.connect(self.equations.to_fraction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.add_num, self.sub_num)
        MainWindow.setTabOrder(self.sub_num, self.add_x)
        MainWindow.setTabOrder(self.add_x, self.sub_x)
        MainWindow.setTabOrder(self.sub_x, self.mult)
        MainWindow.setTabOrder(self.mult, self.div)
        MainWindow.setTabOrder(self.div, self.exchange)
        MainWindow.setTabOrder(self.exchange, self.opposite)
        MainWindow.setTabOrder(self.opposite, self.cancel)
        MainWindow.setTabOrder(self.cancel, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.open)
        MainWindow.setTabOrder(self.open, self.save)
        MainWindow.setTabOrder(self.save, self.new_equation)
        MainWindow.setTabOrder(self.new_equation, self.random)
        MainWindow.setTabOrder(self.random, self.empty)
        MainWindow.setTabOrder(self.empty, self.fraction)
        MainWindow.setTabOrder(self.fraction, self.decimal)
        MainWindow.setTabOrder(self.decimal, self.zoom_in)
        MainWindow.setTabOrder(self.zoom_in, self.zoom_out)
        MainWindow.setTabOrder(self.zoom_out, self.help)
        MainWindow.setTabOrder(self.help, self.about)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pythot"))
        self.open.setToolTip(_translate("MainWindow", "Ouvrir une équation (CTRL+O)"))
        self.save.setToolTip(_translate("MainWindow", "Enregistrer l\'équation (CTRL+S)"))
        self.new_equation.setToolTip(_translate("MainWindow", "Nouvelle équation (CTRL+N)"))
        self.random.setToolTip(_translate("MainWindow", "Équation au hasard (CTRL+H)"))
        self.empty.setToolTip(_translate("MainWindow", "Effacer l\'équation (CTRL+E)"))
        self.fraction.setToolTip(_translate("MainWindow", "Mode fraction (CTRL+F)"))
        self.decimal.setToolTip(_translate("MainWindow", "Mode  décimal (CTRL+D)"))
        self.zoom_in.setToolTip(_translate("MainWindow", "Agrandir le texte (CTRL++)"))
        self.zoom_out.setToolTip(_translate("MainWindow", "Rétrécir le texte(CTRL+-)"))
        self.help.setToolTip(_translate("MainWindow", "Aide de pythot (F1)"))
        self.about.setToolTip(_translate("MainWindow", "A propos de Pythot"))
        self.add_num.setToolTip(_translate("MainWindow", "Ajouter un nombre (+)"))
        self.sub_num.setToolTip(_translate("MainWindow", "Soustraire un nombre (-)"))
        self.add_x.setToolTip(_translate("MainWindow", "Ajouter un terme en x (P)"))
        self.sub_x.setToolTip(_translate("MainWindow", "Soustraire un terme en x (M)"))
        self.mult.setToolTip(_translate("MainWindow", "Multiplier les deux membres par un nombre (*)"))
        self.div.setToolTip(_translate("MainWindow", "Diviser les deux membres par un nombre (/)"))
        self.exchange.setToolTip(_translate("MainWindow", "Intervertir les deux membres (I)"))
        self.opposite.setToolTip(_translate("MainWindow", "Changer le signe des deux membres (O)"))
        self.cancel.setToolTip(_translate("MainWindow", "Annuler le dernier calcul (Suppr)"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fic&hier"))
        self.menuOp_rations.setTitle(_translate("MainWindow", "Opé&rations"))
        self.menuAffichage.setTitle(_translate("MainWindow", "Affichag&e"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionOuvrir_un_fichier_quations.setText(_translate("MainWindow", "&Ouvrir un fichier équations"))
        self.actionOuvrir_un_fichier_quations.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSauvegarder_un_fichier_quation.setText(_translate("MainWindow", "&Sauvegarder un fichier équation"))
        self.actionSauvegarder_un_fichier_quation.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNouvelle_quation.setText(_translate("MainWindow", "&Nouvelle équation"))
        self.actionNouvelle_quation.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_quation_au_hasard.setText(_translate("MainWindow", "&Équation au hasard"))
        self.action_quation_au_hasard.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionEffacer_l_quation.setText(_translate("MainWindow", "&Effacer l\'équation"))
        self.actionEffacer_l_quation.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuitter.setText(_translate("MainWindow", "&Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAjouter_un_nombre.setText(_translate("MainWindow", "&Ajouter un nombre"))
        self.actionAjouter_un_nombre.setShortcut(_translate("MainWindow", "+"))
        self.actionSoustraire_un_nombre.setText(_translate("MainWindow", "&Soustraire un nombre"))
        self.actionSoustraire_un_nombre.setShortcut(_translate("MainWindow", "-"))
        self.actionAjouter_un_terme_en_x.setText(_translate("MainWindow", "Ajouter &un terme en x"))
        self.actionAjouter_un_terme_en_x.setShortcut(_translate("MainWindow", "P"))
        self.actionSoustraire_un_terme_en_x.setText(_translate("MainWindow", "Soustraire un terme &en x"))
        self.actionSoustraire_un_terme_en_x.setShortcut(_translate("MainWindow", "M"))
        self.actionMultiplier_par_un_nombre.setText(_translate("MainWindow", "&Multiplier"))
        self.actionMultiplier_par_un_nombre.setShortcut(_translate("MainWindow", "*"))
        self.actionDiviser_par_un_nombre.setText(_translate("MainWindow", "&Diviser"))
        self.actionDiviser_par_un_nombre.setShortcut(_translate("MainWindow", "/"))
        self.actionIntervertir_les_deux_membres.setText(_translate("MainWindow", "&Intervertir les deux membres"))
        self.actionIntervertir_les_deux_membres.setShortcut(_translate("MainWindow", "I"))
        self.actionPrendre_l_oppos.setText(_translate("MainWindow", "&Prendre l\'opposé"))
        self.actionPrendre_l_oppos.setIconText(_translate("MainWindow", "+ / -"))
        self.actionPrendre_l_oppos.setShortcut(_translate("MainWindow", "O"))
        self.actionAnnuler.setText(_translate("MainWindow", "A&nnuler"))
        self.actionAnnuler.setShortcut(_translate("MainWindow", "Del"))
        self.actionMode_fraction.setText(_translate("MainWindow", "&Mode fraction"))
        self.actionMode_fraction.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionMode_d_cimal.setText(_translate("MainWindow", "Mode &décimal"))
        self.actionMode_d_cimal.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAgrandir.setText(_translate("MainWindow", "&Agrandir"))
        self.actionAgrandir.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionR_duire.setText(_translate("MainWindow", "&Réduire"))
        self.actionR_duire.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionAide.setText(_translate("MainWindow", "&Aide"))
        self.actionAide.setShortcut(_translate("MainWindow", "F1"))
        self.actionA_propos.setText(_translate("MainWindow", "A &propos"))

from .equations import Equations
from . import resources_rc
