# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 492)
        icon = QIcon()
        icon.addFile(u":/icons/icons/board.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon1)
        self.actionReloaded = QAction(MainWindow)
        self.actionReloaded.setObjectName(u"actionReloaded")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/upgrande.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReloaded.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.my_treeWidget = QTreeWidget(self.frame_4)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        QTreeWidgetItem(self.my_treeWidget)
        self.my_treeWidget.setObjectName(u"my_treeWidget")

        self.gridLayout_4.addWidget(self.my_treeWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget = QListWidget(self.frame_3)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(92, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(80, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(13, 13))

        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionClose)
        self.menuMenu.addAction(self.actionReloaded)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QT-Formulario", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionReloaded.setText(QCoreApplication.translate("MainWindow", u"Reloaded", None))
        ___qtreewidgetitem = self.my_treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"New Column", None));

        __sortingEnabled = self.my_treeWidget.isSortingEnabled()
        self.my_treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.my_treeWidget.topLevelItem(1)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem2 = self.my_treeWidget.topLevelItem(2)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem3 = self.my_treeWidget.topLevelItem(3)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem4 = self.my_treeWidget.topLevelItem(4)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        self.my_treeWidget.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"C++", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C#", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Python", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PHP", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"HTML", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.lineEdit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Submit", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

