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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 529)
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
        icon1 = QIcon()
        icon1.addFile(u"registrar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_gen = QPushButton(self.frame_control)
        self.pushButton_gen.setObjectName(u"pushButton_gen")

        self.verticalLayout_3.addWidget(self.pushButton_gen)

        self.pushButton_1 = QPushButton(self.frame_control)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 40))
        icon2 = QIcon()
        icon2.addFile(u"estacion-de-carga.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.frame_control)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u"sentron.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_alarms = QPushButton(self.frame_control)
        self.pushButton_alarms.setObjectName(u"pushButton_alarms")

        self.verticalLayout_3.addWidget(self.pushButton_alarms)

        self.pushButton_log_ins = QPushButton(self.frame_control)
        self.pushButton_log_ins.setObjectName(u"pushButton_log_ins")
        self.pushButton_log_ins.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"hoja.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_log_ins.setIcon(icon4)
        self.pushButton_log_ins.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_log_ins)


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
        self.label = QLabel(self.page_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 441, 51))
        self.label.setAlignment(Qt.AlignCenter)
        self.bt_log_in = QPushButton(self.page_login)
        self.bt_log_in.setObjectName(u"bt_log_in")
        self.bt_log_in.setGeometry(QRect(260, 270, 211, 80))
        self.bt_log_in.setMinimumSize(QSize(150, 80))
        self.label_6 = QLabel(self.page_login)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 100, 201, 51))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.page_login)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 160, 201, 51))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton_eye = QPushButton(self.page_login)
        self.pushButton_eye.setObjectName(u"pushButton_eye")
        self.pushButton_eye.setGeometry(QRect(494, 170, 32, 32))
        self.pushButton_eye.setMinimumSize(QSize(32, 32))
        self.pushButton_eye.setMaximumSize(QSize(32, 32))
        self.pushButton_eye.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);")
        icon5 = QIcon()
        icon5.addFile(u"OJO.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_eye.setIcon(icon5)
        self.pushButton_eye.setIconSize(QSize(30, 30))
        self.username = QLineEdit(self.page_login)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(260, 101, 191, 51))
        self.username.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.password = QLineEdit(self.page_login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(260, 160, 191, 51))
        self.password.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.message_lg = QLabel(self.page_login)
        self.message_lg.setObjectName(u"message_lg")
        self.message_lg.setGeometry(QRect(200, 230, 211, 21))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        font.setWeight(QFont.)
        font.setItalic(False)
        self.message_lg.setFont(font)
        self.message_lg.setStyleSheet(u"color:rgba(255, 255, 255, 140);")
        self.stackedWidget.addWidget(self.page_login)
        self.page_registros = QWidget()
        self.page_registros.setObjectName(u"page_registros")
        self.horizontalLayout_5 = QHBoxLayout(self.page_registros)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.page_registros)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(50, 390))
        self.lineEdit.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_registros)
        self.page_log_ins = QWidget()
        self.page_log_ins.setObjectName(u"page_log_ins")
        self.frame_5 = QFrame(self.page_log_ins)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 537, 401))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.table_log_in = QTableWidget(self.frame_5)
        self.table_log_in.setObjectName(u"table_log_in")

        self.horizontalLayout_7.addWidget(self.table_log_in)

        self.bt_usernames = QPushButton(self.page_log_ins)
        self.bt_usernames.setObjectName(u"bt_usernames")
        self.bt_usernames.setGeometry(QRect(20, 490, 181, 80))
        self.bt_usernames.setMinimumSize(QSize(150, 80))
        self.stackedWidget.addWidget(self.page_log_ins)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_4.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout_3 = QHBoxLayout(self.page_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.page_1)
        self.widget.setObjectName(u"widget")
        self.varn1_2 = QLabel(self.widget)
        self.varn1_2.setObjectName(u"varn1_2")
        self.varn1_2.setGeometry(QRect(220, 380, 91, 31))
        self.varn1_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.varn1 = QLabel(self.widget)
        self.varn1.setObjectName(u"varn1")
        self.varn1.setGeometry(QRect(50, 380, 141, 31))
        self.varn1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_1)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.pushButton_gen.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Ampere", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sentron", None))
        self.pushButton_alarms.setText(QCoreApplication.translate("MainWindow", u"Alarmas", None))
        self.pushButton_log_ins.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicio de Sesi\u00f3n", None))
        self.bt_log_in.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.pushButton_eye.setText("")
        self.username.setText("")
        self.message_lg.setText(QCoreApplication.translate("MainWindow", u"Forgot your User Name or Password? ", None))
        self.bt_usernames.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.varn1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.varn1.setText(QCoreApplication.translate("MainWindow", u"Energ\u00eda", None))
    # retranslateUi

