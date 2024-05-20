# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba1_registro.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(74, 92, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 401, 41))
        self.label.setStyleSheet(u"font: 36pt \"Stencil\";\n"
"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 120, 241, 20))
        self.label_2.setStyleSheet(u"font: 15pt \"Stencil\";\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 180, 141, 20))
        self.label_3.setStyleSheet(u"font: 15pt \"Stencil\";\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 210, 141, 20))
        self.label_4.setStyleSheet(u"font: 15pt \"Stencil\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 180, 191, 22))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 210, 191, 22))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 270, 101, 31))
        self.pushButton.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 350, 75, 24))
        self.pushButton_act = QPushButton(self.centralwidget)
        self.pushButton_act.setObjectName(u"pushButton_act")
        self.pushButton_act.setGeometry(QRect(430, 210, 31, 24))
        icon = QIcon()
        icon.addFile(u"oculto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_act.setIcon(icon)
        self.pushButton_act.setIconSize(QSize(30, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SCADA_Registro", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese su usuario", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.pushButton_act.setText("")
    # retranslateUi

