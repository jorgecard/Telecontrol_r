# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SCADA.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(764, 534)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color:rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"comprobacion-de-lista.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"minimizar-ventana.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_minimizar)

        self.bt_comprimir = QPushButton(self.frame_superior)
        self.bt_comprimir.setObjectName(u"bt_comprimir")
        self.bt_comprimir.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"comprimir-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_comprimir.setIcon(icon2)
        self.bt_comprimir.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_comprimir)

        self.bt_expandir = QPushButton(self.frame_superior)
        self.bt_expandir.setObjectName(u"bt_expandir")
        self.bt_expandir.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"expandir-flechas.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_expandir.setIcon(icon3)
        self.bt_expandir.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_expandir)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMinimumSize(QSize(40, 40))
        self.bt_cerrar.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"cruz.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"background-color: rgb(173,216,230)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 206, 235);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color: rgb(255,255,255);\n"
"font: 77 10pt \"Arial Black\"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\"\n"
"}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame_control)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"registrar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_control)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"estacion-de-carga.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_control)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        icon7 = QIcon()
        icon7.addFile(u"sentron.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
"background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 20pt \"Arial Black\";\n"
"background-color:  rgb(0, 206, 235);\n"
"color: white;\n"
"border:0px solid #14C8DC;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 0px;\n"
"color: rgb(255,255,255);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt \"Times New Roman\"\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: white;\n"
"border: 0px;\n"
"color: rgb(255,255,255);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt \"Times New Roman\"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 206, 235);\n"
"border-radius: 20px;\n"
"color: rgb(255,255,255);\n"
"font: 77 20pt \"Arial Black\"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: white;\n"
"color: rgb(0,0,0);\n"
"gridline-color: rgb(0,206,255);\n"
"font-size: 12;\n"
""
                        "color: #000000;\n"
"}\n"
"\n"
"QHeaderView {\n"
"background-color: rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"font-size: 12;\n"
"}\n"
"")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.Contrasena = QTextEdit(self.page_login)
        self.Contrasena.setObjectName(u"Contrasena")
        self.Contrasena.setGeometry(QRect(100, 130, 231, 91))
        self.label = QLabel(self.page_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 311, 51))
        self.label.setAlignment(Qt.AlignCenter)
        self.bt_registrar = QPushButton(self.page_login)
        self.bt_registrar.setObjectName(u"bt_registrar")
        self.bt_registrar.setGeometry(QRect(110, 280, 211, 80))
        self.bt_registrar.setMinimumSize(QSize(150, 80))
        self.stackedWidget.addWidget(self.page_login)
        self.page_sentron = QWidget()
        self.page_sentron.setObjectName(u"page_sentron")
        self.stackedWidget.addWidget(self.page_sentron)
        self.page_ampere = QWidget()
        self.page_ampere.setObjectName(u"page_ampere")
        self.frame_2 = QFrame(self.page_ampere)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 10, 201, 191))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 161, 41))
        self.frame_3 = QFrame(self.page_ampere)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 10, 211, 191))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 151, 41))
        self.frame_4 = QFrame(self.page_ampere)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 220, 201, 191))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 161, 41))
        self.frame_5 = QFrame(self.page_ampere)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(240, 220, 211, 191))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 161, 41))
        self.stackedWidget.addWidget(self.page_ampere)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.bt_minimizar.setText("")
        self.bt_comprimir.setText("")
        self.bt_expandir.setText("")
        self.bt_cerrar.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ampere", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sentron", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicio de Sesi\u00f3n", None))
        self.bt_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Voltajes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"THD", None))
    # retranslateUi

