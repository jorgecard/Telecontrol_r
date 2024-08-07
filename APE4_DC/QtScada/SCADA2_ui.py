# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SCADA2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Scada_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1460, 893)
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
        self.pushButton_gen.setMinimumSize(QSize(0, 40))
        icon2 = QIcon()
        icon2.addFile(u"computer-monitor-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_gen.setIcon(icon2)
        self.pushButton_gen.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_gen)

        self.pushButton_1 = QPushButton(self.frame_control)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u"estacion-de-carga.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon3)
        self.pushButton_1.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.frame_control)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"sentron.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_alarms = QPushButton(self.frame_control)
        self.pushButton_alarms.setObjectName(u"pushButton_alarms")
        self.pushButton_alarms.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"alarm-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_alarms.setIcon(icon5)
        self.pushButton_alarms.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_alarms)

        self.pushButton_log_ins = QPushButton(self.frame_control)
        self.pushButton_log_ins.setObjectName(u"pushButton_log_ins")
        self.pushButton_log_ins.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"hoja.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_log_ins.setIcon(icon6)
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
        self.stackedWidget.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.stackedWidget.setLineWidth(1)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.frame_11 = QFrame(self.page_login)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(200, 130, 571, 391))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 441, 51))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 201, 51))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 180, 201, 51))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.username = QLineEdit(self.frame_11)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(230, 110, 191, 51))
        self.username.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.password = QLineEdit(self.frame_11)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(230, 180, 191, 51))
        self.password.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_eye = QPushButton(self.frame_11)
        self.pushButton_eye.setObjectName(u"pushButton_eye")
        self.pushButton_eye.setGeometry(QRect(450, 190, 32, 32))
        self.pushButton_eye.setMinimumSize(QSize(32, 32))
        self.pushButton_eye.setMaximumSize(QSize(32, 32))
        self.pushButton_eye.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(245, 245, 245);")
        icon7 = QIcon()
        icon7.addFile(u"OJO.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_eye.setIcon(icon7)
        self.pushButton_eye.setIconSize(QSize(30, 30))
        self.message_lg = QLabel(self.frame_11)
        self.message_lg.setObjectName(u"message_lg")
        self.message_lg.setGeometry(QRect(220, 240, 231, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.message_lg.setFont(font)
        self.message_lg.setStyleSheet(u"color:rgba(255, 255, 255, 140);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.bt_log_in = QPushButton(self.frame_11)
        self.bt_log_in.setObjectName(u"bt_log_in")
        self.bt_log_in.setGeometry(QRect(230, 280, 211, 80))
        self.bt_log_in.setMinimumSize(QSize(150, 80))
        self.stackedWidget.addWidget(self.page_login)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 570, 1171, 212))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_8.addWidget(self.tableWidget)

        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 10, 1171, 551))
        self.frame_10.setStyleSheet(u"background-color: rgb(125,125,125);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 1091, 361))
        self.label_2.setStyleSheet(u"background-image: url(:/prefijoNuevo/esquema4.png);\n"
"background-image: url(:/prefijoNuevo/esquema3.png);")
        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(900, 200, 271, 161))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:rgb(84, 84, 84);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 206, 235);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-color:rgb(0,0,0);\n"
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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 110, 101, 40))
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 110, 101, 40))
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 40, 89, 20))
        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 70, 89, 20))
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 70, 131, 22))
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 40, 131, 22))
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(240, 40, 31, 21))
        self.label_25.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 91, 21))
        self.label_12.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.frame_3 = QFrame(self.frame_10)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 200, 221, 221))
        self.frame_3.setStyleSheet(u"background-color:rgb(84, 84, 84);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 71, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 71, 21))
        self.label_4.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 71, 21))
        self.label_5.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 130, 71, 21))
        self.label_8.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 160, 71, 21))
        self.label_9.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 190, 81, 21))
        self.label_10.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 40, 71, 22))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 91, 21))
        self.label_11.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 70, 71, 22))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 100, 71, 22))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(90, 130, 71, 22))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(90, 160, 71, 22))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_8 = QLineEdit(self.frame_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(90, 190, 71, 22))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(170, 40, 31, 21))
        self.label_16.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(170, 70, 31, 21))
        self.label_17.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 100, 31, 21))
        self.label_18.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 130, 31, 21))
        self.label_19.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 160, 31, 21))
        self.label_20.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(170, 190, 31, 21))
        self.label_21.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(900, 360, 271, 101))
        self.frame_12.setStyleSheet(u"background-color:rgb(84, 84, 84);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 71, 21))
        self.label_22.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 40, 71, 21))
        self.label_23.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 70, 71, 21))
        self.label_24.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_12 = QLineEdit(self.frame_12)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(90, 10, 71, 22))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_13 = QLineEdit(self.frame_12)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(90, 40, 71, 22))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_14 = QLineEdit(self.frame_12)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(90, 70, 71, 22))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_35 = QLabel(self.frame_12)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(170, 10, 31, 21))
        self.label_35.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_36 = QLabel(self.frame_12)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(170, 40, 31, 21))
        self.label_36.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_37 = QLabel(self.frame_12)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(170, 70, 31, 21))
        self.label_37.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(630, 290, 231, 221))
        self.frame_13.setStyleSheet(u"background-color:rgb(84, 84, 84);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 40, 91, 21))
        self.label_31.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 70, 91, 21))
        self.label_32.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_33 = QLabel(self.frame_13)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 100, 91, 21))
        self.label_33.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_34 = QLabel(self.frame_13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 130, 91, 21))
        self.label_34.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_38 = QLabel(self.frame_13)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 160, 91, 21))
        self.label_38.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_39 = QLabel(self.frame_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 190, 91, 21))
        self.label_39.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_15 = QLineEdit(self.frame_13)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(120, 40, 71, 22))
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 10, 91, 21))
        self.label_40.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_16 = QLineEdit(self.frame_13)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(120, 70, 71, 22))
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_17 = QLineEdit(self.frame_13)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(120, 100, 71, 22))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_18 = QLineEdit(self.frame_13)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(120, 130, 71, 22))
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_19 = QLineEdit(self.frame_13)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(120, 160, 71, 22))
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_20 = QLineEdit(self.frame_13)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(120, 190, 71, 22))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_41 = QLabel(self.frame_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(200, 40, 31, 21))
        self.label_41.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.frame_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(200, 70, 31, 21))
        self.label_42.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_43 = QLabel(self.frame_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(200, 100, 31, 21))
        self.label_43.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_44 = QLabel(self.frame_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(200, 130, 31, 21))
        self.label_44.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(200, 160, 31, 21))
        self.label_45.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.frame_13)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(200, 190, 31, 21))
        self.label_46.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_46.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.frame_10.raise_()
        self.frame_6.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_7 = QFrame(self.page_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 120, 811, 421))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.tableWidget_2 = QTableWidget(self.frame_7)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 20, 781, 192))
        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 30, 801, 80))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 20, 231, 41))
        self.label_26.setStyleSheet(u"background-color: rgb(0, 206, 235);\n"
"font: 28pt \"Segoe UI\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color: rgb(255,255,255);\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
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
        self.widget_1 = QWidget(self.page_1)
        self.widget_1.setObjectName(u"widget_1")
        self.varn1_2 = QLabel(self.widget_1)
        self.varn1_2.setObjectName(u"varn1_2")
        self.varn1_2.setGeometry(QRect(220, 380, 91, 31))
        self.varn1_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.varn1 = QLabel(self.widget_1)
        self.varn1.setObjectName(u"varn1")
        self.varn1.setGeometry(QRect(50, 380, 141, 31))
        self.varn1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.widget_1)

        self.stackedWidget.addWidget(self.page_1)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.username.setText("")
        self.pushButton_eye.setText("")
        self.message_lg.setText(QCoreApplication.translate("MainWindow", u"Forgot your User Name or Password? ", None))
        self.bt_log_in.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Mascara de tiempo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Acci\u00f3n", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Aqui los datos", None));
        self.label_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Constante", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"txt", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"KW", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Carga", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ENERG\u00cdA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"EFICIENCIA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"GENERADOR", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Kwh", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"VENTILADORES", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"FLUJO DE H2", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"HIDR\u00d3GENO", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mascara de tiempo", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Acci\u00f3n", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Aqui los datos", None));
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Alarmas", None))
        self.bt_usernames.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.varn1_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.varn1.setText(QCoreApplication.translate("MainWindow", u"Energ\u00eda", None))
    # retranslateUi

