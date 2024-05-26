# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.iu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_registerMain(object):
    def setupUi(self, registerMain):
        if not registerMain.objectName():
            registerMain.setObjectName(u"registerMain")
        registerMain.setEnabled(True)
        registerMain.resize(432, 740)
        registerMain.setStyleSheet(u"*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/images/images/background.jpg);\n"
"}\n"
"\n"
"QFrame#contenedor{\n"
"background:#060921;\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#27587B;\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLabel#registro{\n"
"color: white;\n"
"font-size: 24px;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"font-weight: bold;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#27587B;\n"
"color: white;\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#0E5386;\n"
"color: white;\n"
"border-radius: 15px;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(registerMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.contenedor = QFrame(self.centralwidget)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(10, 10, 411, 721))
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.icon = QToolButton(self.contenedor)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(180, 40, 51, 51))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(30, 30))
        self.registro = QLabel(self.contenedor)
        self.registro.setObjectName(u"registro")
        self.registro.setEnabled(True)
        self.registro.setGeometry(QRect(60, 140, 131, 41))
        self.label = QLabel(self.contenedor)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 190, 61, 16))
        self.lineEdit = QLineEdit(self.contenedor)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 220, 291, 20))
        self.lineEdit.setMaxLength(16)
        self.label_4 = QLabel(self.contenedor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 270, 61, 16))
        self.lineEdit_4 = QLineEdit(self.contenedor)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(60, 300, 291, 20))
        self.lineEdit_4.setMaxLength(16)
        self.label_5 = QLabel(self.contenedor)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 360, 41, 16))
        self.lineEdit_5 = QLineEdit(self.contenedor)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(60, 390, 291, 20))
        self.lineEdit_5.setMaxLength(25)
        self.label_6 = QLabel(self.contenedor)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 440, 71, 16))
        self.lineEdit_6 = QLineEdit(self.contenedor)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(60, 470, 291, 20))
        self.lineEdit_6.setMaxLength(12)
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.contenedor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(54, 550, 291, 31))
        registerMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(registerMain)

        QMetaObject.connectSlotsByName(registerMain)
    # setupUi

    def retranslateUi(self, registerMain):
        registerMain.setWindowTitle(QCoreApplication.translate("registerMain", u"Register", None))
        self.icon.setText(QCoreApplication.translate("registerMain", u"...", None))
        self.registro.setText(QCoreApplication.translate("registerMain", u"REGISTRO", None))
        self.label.setText(QCoreApplication.translate("registerMain", u"Nombre/s", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("registerMain", u"Nombre/s", None))
        self.label_4.setText(QCoreApplication.translate("registerMain", u"Apellidos", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("registerMain", u"Apellidos", None))
        self.label_5.setText(QCoreApplication.translate("registerMain", u"Email", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("registerMain", u"example@mail.com", None))
        self.label_6.setText(QCoreApplication.translate("registerMain", u"Contrase\u00f1a", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("registerMain", u"************", None))
        self.pushButton.setText(QCoreApplication.translate("registerMain", u"CREAR CUENTA", None))
    # retranslateUi

