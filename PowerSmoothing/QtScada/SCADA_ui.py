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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1359, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 193, 193);\n"
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
        icon.addFile(u"../../../../../../../GitHub/Telecontrol_r/APE4_DC/QtScada/comprobacion-de-lista.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(312, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.lineEdit_6 = QLabel(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_6)

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
"background-color: rgb(193, 193, 193);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(193, 193, 193);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"color: rgb(0,0,0);\n"
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
        self.pushButton_gen = QPushButton(self.frame_control)
        self.pushButton_gen.setObjectName(u"pushButton_gen")
        self.pushButton_gen.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../APE4_DC/QtScada/computer-monitor-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_gen.setIcon(icon1)
        self.pushButton_gen.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_gen)

        self.pushButton_0 = QPushButton(self.frame_control)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 40))
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../APE4_DC/QtScada/estacion-de-carga.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_0.setIcon(icon2)
        self.pushButton_0.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton_0)

        self.pushButton_1 = QPushButton(self.frame_control)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../../Downloads/ESQUEMA 1 INVERSOR-eeeModel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon3)
        self.pushButton_1.setIconSize(QSize(60, 40))

        self.verticalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.frame_control)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"../../../../../../../Downloads/ESQUEMA 1 INVERSOR-Model.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_control)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"../../../../../../../Downloads/vecteezy_voltmeter-vector-icon_16223191.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(40, 40))

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
        self.stackedWidget.setMinimumSize(QSize(1100, 500))
        self.stackedWidget.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.stackedWidget.setLineWidth(1)
        self.page_general = QWidget()
        self.page_general.setObjectName(u"page_general")
        self.frame_10 = QFrame(self.page_general)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 10, 1091, 521))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: rgb(193, 193, 193);\n"
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
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1091, 311))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3 = QFrame(self.frame_10)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(470, 310, 221, 191))
        self.frame_3.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 71, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 71, 21))
        self.label_4.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 71, 21))
        self.label_5.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 121, 21))
        self.label_11.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(170, 40, 31, 21))
        self.label_16.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(170, 70, 31, 21))
        self.label_17.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 100, 31, 21))
        self.label_18.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_3 = QLabel(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_4 = QLabel(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_5 = QLabel(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 130, 71, 21))
        self.label_35.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_16 = QLabel(self.frame_3)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(90, 130, 71, 21))
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(170, 130, 31, 21))
        self.label_36.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_109 = QLabel(self.frame_3)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(10, 160, 71, 21))
        self.label_109.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_48 = QLabel(self.frame_3)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setGeometry(QRect(90, 160, 71, 21))
        self.lineEdit_48.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_110 = QLabel(self.frame_3)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(170, 160, 31, 21))
        self.label_110.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(130, 310, 221, 151))
        self.frame_9.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 40, 71, 21))
        self.label_28.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_29 = QLabel(self.frame_9)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 70, 71, 21))
        self.label_29.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 100, 71, 21))
        self.label_30.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 121, 21))
        self.label_31.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(170, 40, 31, 21))
        self.label_32.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(170, 70, 31, 21))
        self.label_33.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(170, 100, 31, 21))
        self.label_34.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_13 = QLabel(self.frame_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_14 = QLabel(self.frame_9)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_15 = QLabel(self.frame_9)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.frame_6 = QFrame(self.frame_10)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(870, 310, 221, 161))
        self.frame_6.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 40, 71, 21))
        self.label_13.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 70, 71, 21))
        self.label_15.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 100, 71, 21))
        self.label_22.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 10, 121, 21))
        self.label_23.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(170, 40, 31, 21))
        self.label_24.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 70, 31, 21))
        self.label_25.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(170, 100, 31, 21))
        self.label_27.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_10 = QLabel(self.frame_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_11 = QLabel(self.frame_6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_12 = QLabel(self.frame_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_37 = QLabel(self.frame_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 130, 71, 21))
        self.label_37.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_17 = QLabel(self.frame_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(90, 130, 71, 21))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_38 = QLabel(self.frame_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(170, 130, 31, 21))
        self.label_38.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_general)
        self.page_gr_fv = QWidget()
        self.page_gr_fv.setObjectName(u"page_gr_fv")
        self.widget_1 = QWidget(self.page_gr_fv)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setGeometry(QRect(0, 0, 881, 500))
        self.widget_1.setMinimumSize(QSize(0, 500))
        self.widget_1.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_11 = QFrame(self.page_gr_fv)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(880, 10, 221, 141))
        self.frame_11.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 40, 71, 21))
        self.label_39.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_40 = QLabel(self.frame_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 70, 71, 21))
        self.label_40.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_41 = QLabel(self.frame_11)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 100, 71, 21))
        self.label_41.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_42 = QLabel(self.frame_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 10, 121, 21))
        self.label_42.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_43 = QLabel(self.frame_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(170, 40, 31, 21))
        self.label_43.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_43.setAlignment(Qt.AlignCenter)
        self.lineEdit_18 = QLabel(self.frame_11)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_19 = QLabel(self.frame_11)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_20 = QLabel(self.frame_11)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_44 = QLabel(self.frame_11)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(170, 70, 31, 21))
        self.label_44.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.frame_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(170, 100, 31, 21))
        self.label_45.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.page_gr_fv)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(880, 150, 221, 141))
        self.frame_12.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_46 = QLabel(self.frame_12)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 40, 71, 21))
        self.label_46.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_47 = QLabel(self.frame_12)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 70, 71, 21))
        self.label_47.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_48 = QLabel(self.frame_12)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 100, 71, 21))
        self.label_48.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_49 = QLabel(self.frame_12)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 10, 121, 21))
        self.label_49.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_50 = QLabel(self.frame_12)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(170, 40, 31, 21))
        self.label_50.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_51 = QLabel(self.frame_12)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(170, 70, 31, 21))
        self.label_51.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_51.setAlignment(Qt.AlignCenter)
        self.lineEdit_21 = QLabel(self.frame_12)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_22 = QLabel(self.frame_12)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_23 = QLabel(self.frame_12)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_52 = QLabel(self.frame_12)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(170, 100, 31, 21))
        self.label_52.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_52.setAlignment(Qt.AlignCenter)
        self.frame_13 = QFrame(self.page_gr_fv)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(880, 290, 221, 141))
        self.frame_13.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_53 = QLabel(self.frame_13)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 40, 51, 21))
        self.label_53.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_54 = QLabel(self.frame_13)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 70, 51, 21))
        self.label_54.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_55 = QLabel(self.frame_13)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 100, 51, 21))
        self.label_55.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_56 = QLabel(self.frame_13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 10, 121, 21))
        self.label_56.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_59 = QLabel(self.frame_13)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(150, 40, 31, 21))
        self.label_59.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_24 = QLabel(self.frame_13)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(70, 40, 71, 21))
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_25 = QLabel(self.frame_13)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(70, 70, 71, 21))
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_26 = QLabel(self.frame_13)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(70, 100, 71, 21))
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_60 = QLabel(self.frame_13)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(150, 70, 51, 21))
        self.label_60.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_61 = QLabel(self.frame_13)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(150, 100, 41, 21))
        self.label_61.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_gr_fv)
        self.page_gr_bat = QWidget()
        self.page_gr_bat.setObjectName(u"page_gr_bat")
        self.widget_2 = QWidget(self.page_gr_bat)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 881, 500))
        self.widget_2.setMinimumSize(QSize(0, 500))
        self.widget_2.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_14 = QFrame(self.page_gr_bat)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(880, 10, 221, 141))
        self.frame_14.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.frame_14)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 40, 71, 21))
        self.label_57.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_58 = QLabel(self.frame_14)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 70, 71, 21))
        self.label_58.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_62 = QLabel(self.frame_14)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 100, 71, 21))
        self.label_62.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_63 = QLabel(self.frame_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 10, 121, 21))
        self.label_63.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_64 = QLabel(self.frame_14)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(170, 40, 31, 21))
        self.label_64.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_64.setAlignment(Qt.AlignCenter)
        self.lineEdit_27 = QLabel(self.frame_14)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_28 = QLabel(self.frame_14)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_29 = QLabel(self.frame_14)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_65 = QLabel(self.frame_14)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(170, 70, 31, 21))
        self.label_65.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_65.setAlignment(Qt.AlignCenter)
        self.label_66 = QLabel(self.frame_14)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(170, 100, 31, 21))
        self.label_66.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_66.setAlignment(Qt.AlignCenter)
        self.frame_15 = QFrame(self.page_gr_bat)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(880, 150, 221, 141))
        self.frame_15.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_67 = QLabel(self.frame_15)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(10, 40, 71, 21))
        self.label_67.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_68 = QLabel(self.frame_15)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(10, 70, 71, 21))
        self.label_68.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_69 = QLabel(self.frame_15)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 100, 71, 21))
        self.label_69.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_70 = QLabel(self.frame_15)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 10, 121, 21))
        self.label_70.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_71 = QLabel(self.frame_15)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(170, 40, 31, 21))
        self.label_71.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_72 = QLabel(self.frame_15)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(170, 70, 31, 21))
        self.label_72.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_72.setAlignment(Qt.AlignCenter)
        self.lineEdit_30 = QLabel(self.frame_15)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_31 = QLabel(self.frame_15)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_31.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_32 = QLabel(self.frame_15)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_73 = QLabel(self.frame_15)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(170, 100, 31, 21))
        self.label_73.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_73.setAlignment(Qt.AlignCenter)
        self.frame_16 = QFrame(self.page_gr_bat)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(880, 290, 221, 141))
        self.frame_16.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_74 = QLabel(self.frame_16)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(10, 40, 51, 21))
        self.label_74.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_75 = QLabel(self.frame_16)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 70, 51, 21))
        self.label_75.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_76 = QLabel(self.frame_16)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(10, 100, 51, 21))
        self.label_76.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_77 = QLabel(self.frame_16)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(10, 10, 121, 21))
        self.label_77.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_78 = QLabel(self.frame_16)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(150, 40, 31, 21))
        self.label_78.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_33 = QLabel(self.frame_16)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(QRect(70, 40, 71, 21))
        self.lineEdit_33.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_34 = QLabel(self.frame_16)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(QRect(70, 70, 71, 21))
        self.lineEdit_34.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_35 = QLabel(self.frame_16)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(QRect(70, 100, 71, 21))
        self.lineEdit_35.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_79 = QLabel(self.frame_16)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(150, 70, 51, 21))
        self.label_79.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_80 = QLabel(self.frame_16)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(150, 100, 41, 21))
        self.label_80.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.frame_20 = QFrame(self.page_gr_bat)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(880, 430, 221, 231))
        self.frame_20.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_111 = QLabel(self.frame_20)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(10, 40, 51, 21))
        self.label_111.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_112 = QLabel(self.frame_20)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(10, 70, 51, 21))
        self.label_112.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_113 = QLabel(self.frame_20)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(10, 100, 51, 21))
        self.label_113.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_114 = QLabel(self.frame_20)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(10, 10, 121, 21))
        self.label_114.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_115 = QLabel(self.frame_20)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(150, 40, 31, 21))
        self.label_115.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_49 = QLabel(self.frame_20)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setGeometry(QRect(70, 40, 71, 21))
        self.lineEdit_49.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_50 = QLabel(self.frame_20)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setGeometry(QRect(70, 70, 71, 21))
        self.lineEdit_50.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_51 = QLabel(self.frame_20)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setGeometry(QRect(70, 100, 71, 21))
        self.lineEdit_51.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_116 = QLabel(self.frame_20)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(150, 70, 51, 21))
        self.label_116.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_117 = QLabel(self.frame_20)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(150, 100, 41, 21))
        self.label_117.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_118 = QLabel(self.frame_20)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(10, 130, 51, 21))
        self.label_118.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_52 = QLabel(self.frame_20)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setGeometry(QRect(70, 130, 71, 21))
        self.lineEdit_52.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_119 = QLabel(self.frame_20)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(150, 130, 51, 21))
        self.label_119.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_120 = QLabel(self.frame_20)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(10, 160, 51, 21))
        self.label_120.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_53 = QLabel(self.frame_20)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setGeometry(QRect(70, 160, 71, 21))
        self.lineEdit_53.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_121 = QLabel(self.frame_20)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(150, 160, 51, 21))
        self.label_121.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_54 = QLabel(self.frame_20)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setGeometry(QRect(70, 190, 71, 21))
        self.lineEdit_54.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_122 = QLabel(self.frame_20)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(10, 190, 51, 21))
        self.label_122.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_123 = QLabel(self.frame_20)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(150, 190, 51, 21))
        self.label_123.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_gr_bat)
        self.page_gr_sc = QWidget()
        self.page_gr_sc.setObjectName(u"page_gr_sc")
        self.widget_3 = QWidget(self.page_gr_sc)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 881, 500))
        self.widget_3.setMinimumSize(QSize(0, 500))
        self.widget_3.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_17 = QFrame(self.page_gr_sc)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(880, 20, 221, 141))
        self.frame_17.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_88 = QLabel(self.frame_17)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(10, 40, 71, 21))
        self.label_88.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_89 = QLabel(self.frame_17)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(10, 70, 71, 21))
        self.label_89.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_90 = QLabel(self.frame_17)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(10, 100, 71, 21))
        self.label_90.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_91 = QLabel(self.frame_17)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(10, 10, 121, 21))
        self.label_91.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_92 = QLabel(self.frame_17)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(170, 40, 31, 21))
        self.label_92.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_92.setAlignment(Qt.AlignCenter)
        self.lineEdit_39 = QLabel(self.frame_17)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_39.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_40 = QLabel(self.frame_17)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_40.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_41 = QLabel(self.frame_17)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_41.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_93 = QLabel(self.frame_17)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(170, 70, 31, 21))
        self.label_93.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_93.setAlignment(Qt.AlignCenter)
        self.label_94 = QLabel(self.frame_17)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(170, 100, 31, 21))
        self.label_94.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_94.setAlignment(Qt.AlignCenter)
        self.frame_18 = QFrame(self.page_gr_sc)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(880, 160, 221, 141))
        self.frame_18.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_95 = QLabel(self.frame_18)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(10, 40, 71, 21))
        self.label_95.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_96 = QLabel(self.frame_18)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(10, 70, 71, 21))
        self.label_96.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_97 = QLabel(self.frame_18)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 100, 71, 21))
        self.label_97.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_98 = QLabel(self.frame_18)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(10, 10, 121, 21))
        self.label_98.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_99 = QLabel(self.frame_18)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(170, 40, 31, 21))
        self.label_99.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_99.setAlignment(Qt.AlignCenter)
        self.label_100 = QLabel(self.frame_18)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(170, 70, 31, 21))
        self.label_100.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_100.setAlignment(Qt.AlignCenter)
        self.lineEdit_42 = QLabel(self.frame_18)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_42.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_43 = QLabel(self.frame_18)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_43.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_44 = QLabel(self.frame_18)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_44.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_101 = QLabel(self.frame_18)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(170, 100, 31, 21))
        self.label_101.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_101.setAlignment(Qt.AlignCenter)
        self.frame_19 = QFrame(self.page_gr_sc)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(880, 300, 221, 141))
        self.frame_19.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_102 = QLabel(self.frame_19)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(10, 40, 51, 21))
        self.label_102.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_103 = QLabel(self.frame_19)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(10, 70, 51, 21))
        self.label_103.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_104 = QLabel(self.frame_19)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(10, 100, 51, 21))
        self.label_104.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_105 = QLabel(self.frame_19)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(10, 10, 121, 21))
        self.label_105.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_106 = QLabel(self.frame_19)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(150, 40, 31, 21))
        self.label_106.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.lineEdit_45 = QLabel(self.frame_19)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setGeometry(QRect(70, 40, 71, 21))
        self.lineEdit_45.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_46 = QLabel(self.frame_19)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setGeometry(QRect(70, 70, 71, 21))
        self.lineEdit_46.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_47 = QLabel(self.frame_19)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setGeometry(QRect(70, 100, 71, 21))
        self.lineEdit_47.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_107 = QLabel(self.frame_19)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(150, 70, 51, 21))
        self.label_107.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_108 = QLabel(self.frame_19)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(150, 100, 41, 21))
        self.label_108.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.frame_21 = QFrame(self.page_gr_sc)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(880, 440, 221, 171))
        self.frame_21.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_132 = QLabel(self.frame_21)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(10, 40, 71, 21))
        self.label_132.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_133 = QLabel(self.frame_21)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(10, 70, 71, 21))
        self.label_133.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_134 = QLabel(self.frame_21)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(10, 100, 71, 21))
        self.label_134.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_135 = QLabel(self.frame_21)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(10, 10, 121, 21))
        self.label_135.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_136 = QLabel(self.frame_21)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(170, 40, 31, 21))
        self.label_136.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_136.setAlignment(Qt.AlignCenter)
        self.lineEdit_58 = QLabel(self.frame_21)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setGeometry(QRect(90, 40, 71, 21))
        self.lineEdit_58.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_59 = QLabel(self.frame_21)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setGeometry(QRect(90, 70, 71, 21))
        self.lineEdit_59.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.lineEdit_60 = QLabel(self.frame_21)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setGeometry(QRect(90, 100, 71, 21))
        self.lineEdit_60.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_137 = QLabel(self.frame_21)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(170, 70, 31, 21))
        self.label_137.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_137.setAlignment(Qt.AlignCenter)
        self.label_138 = QLabel(self.frame_21)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(170, 100, 31, 21))
        self.label_138.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_138.setAlignment(Qt.AlignCenter)
        self.label_139 = QLabel(self.frame_21)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(10, 130, 71, 21))
        self.label_139.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_61 = QLabel(self.frame_21)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setGeometry(QRect(90, 130, 71, 21))
        self.lineEdit_61.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Segoe UI\";")
        self.label_140 = QLabel(self.frame_21)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(170, 130, 31, 21))
        self.label_140.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";")
        self.label_140.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_gr_sc)
        self.page_metodo_control = QWidget()
        self.page_metodo_control.setObjectName(u"page_metodo_control")
        self.horizontalLayout_3 = QHBoxLayout(self.page_metodo_control)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_04 = QWidget(self.page_metodo_control)
        self.widget_04.setObjectName(u"widget_04")
        self.widget_04.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.control_selected = QFrame(self.widget_04)
        self.control_selected.setObjectName(u"control_selected")
        self.control_selected.setGeometry(QRect(10, 20, 281, 181))
        self.control_selected.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(193, 193, 193);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(193, 193, 193);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-color:rgb(0,0,0);\n"
"color: rgb(0,0,0);\n"
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
        self.control_selected.setFrameShape(QFrame.StyledPanel)
        self.control_selected.setFrameShadow(QFrame.Raised)
        self.pushButton_activar = QPushButton(self.control_selected)
        self.pushButton_activar.setObjectName(u"pushButton_activar")
        self.pushButton_activar.setGeometry(QRect(20, 110, 101, 40))
        self.pushButton_activar.setMinimumSize(QSize(0, 40))
        self.pushButton_activar.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.pushButton_Desactivar = QPushButton(self.control_selected)
        self.pushButton_Desactivar.setObjectName(u"pushButton_Desactivar")
        self.pushButton_Desactivar.setGeometry(QRect(150, 110, 101, 40))
        self.pushButton_Desactivar.setMinimumSize(QSize(0, 40))
        self.pushButton_Desactivar.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_14 = QLabel(self.control_selected)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 141, 21))
        self.label_14.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.comboBox = QComboBox(self.control_selected)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 40, 271, 22))
        self.path_lb_7 = QLabel(self.control_selected)
        self.path_lb_7.setObjectName(u"path_lb_7")
        self.path_lb_7.setGeometry(QRect(20, 80, 191, 20))
        self.path_lb_7.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.comboBox_2 = QComboBox(self.control_selected)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 80, 271, 22))
        self.frame_5 = QFrame(self.widget_04)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 230, 311, 121))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(193, 193, 193);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(193, 193, 193);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-color:rgb(0,0,0);\n"
"color: rgb(0,0,0);\n"
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_set_pow = QPushButton(self.frame_5)
        self.pushButton_set_pow.setObjectName(u"pushButton_set_pow")
        self.pushButton_set_pow.setGeometry(QRect(10, 70, 101, 40))
        self.pushButton_set_pow.setMinimumSize(QSize(0, 40))
        self.pushButton_set_pow.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"border-bottom-color: rgb(0, 0, 0);")
        self.pushButton_13 = QPushButton(self.frame_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(140, 70, 101, 40))
        self.pushButton_13.setMinimumSize(QSize(0, 40))
        self.pushButton_13.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 141, 21))
        self.label_26.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.path_lb_6 = QLabel(self.frame_5)
        self.path_lb_6.setObjectName(u"path_lb_6")
        self.path_lb_6.setGeometry(QRect(10, 40, 261, 20))
        self.path_lb_6.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_14 = QPushButton(self.frame_5)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(280, 40, 31, 21))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(193, 193, 193);\n"
"border-top-left-radius: 2px;\n"
"border-bottom-left-radius:2px;\n"
"border-color:rgb(0,0,0);\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 2px;\n"
"border-bottom-left-radius:2px;\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\"\n"
"}")
        self.widget_0 = QWidget(self.widget_04)
        self.widget_0.setObjectName(u"widget_0")
        self.widget_0.setGeometry(QRect(330, 20, 741, 500))
        self.widget_0.setMinimumSize(QSize(0, 500))
        self.widget_0.setStyleSheet(u"background-color: rgb(193, 193, 193);")

        self.horizontalLayout_3.addWidget(self.widget_04)

        self.stackedWidget.addWidget(self.page_metodo_control)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(2, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.lineEdit_6.setText("")
        self.pushButton_gen.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"Power \n"
"Smoothing", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Fotovoltaico", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bater\u00eda", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Supercondensador", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bater\u00eda de litio", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.lineEdit_16.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"SOH", None))
        self.lineEdit_48.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Panel Fotovoltaico", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"VOLTAJE", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CORRIENTE", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"POTENCIA", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Supercondensador", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.lineEdit_17.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Vr", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Vs", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Vt", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Voltajes", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lineEdit_18.setText("")
        self.lineEdit_19.setText("")
        self.lineEdit_20.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Ir", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Is", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"It", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_24.setText("")
        self.lineEdit_25.setText("")
        self.lineEdit_26.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"kVAr", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"kVA", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Vr", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Vs", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Vt", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Voltajes", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lineEdit_27.setText("")
        self.lineEdit_28.setText("")
        self.lineEdit_29.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Ir", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Is", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"It", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineEdit_30.setText("")
        self.lineEdit_31.setText("")
        self.lineEdit_32.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_33.setText("")
        self.lineEdit_34.setText("")
        self.lineEdit_35.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"kVAr", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"kVA", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"DC", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lineEdit_49.setText("")
        self.lineEdit_50.setText("")
        self.lineEdit_51.setText("")
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.lineEdit_52.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"SOH", None))
        self.lineEdit_53.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.lineEdit_54.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"VBAT.", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Vr", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Vs", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Vt", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Voltajes", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lineEdit_39.setText("")
        self.lineEdit_40.setText("")
        self.lineEdit_41.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Ir", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Is", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"It", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Corriente", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineEdit_42.setText("")
        self.lineEdit_43.setText("")
        self.lineEdit_44.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.lineEdit_45.setText("")
        self.lineEdit_46.setText("")
        self.lineEdit_47.setText("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"kVAr", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"kVA", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"DC", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lineEdit_58.setText("")
        self.lineEdit_59.setText("")
        self.lineEdit_60.setText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.lineEdit_61.setText("")
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_activar.setText(QCoreApplication.translate("MainWindow", u"Activar ", None))
        self.pushButton_Desactivar.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo de Control", None))
        self.path_lb_7.setText("")
        self.pushButton_set_pow.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Perfil Fotovoltaico", None))
        self.path_lb_6.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

