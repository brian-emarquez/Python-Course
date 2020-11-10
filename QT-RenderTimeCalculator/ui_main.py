# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Render_Time_Calculatoricgnoh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 800)
        MainWindow.setMinimumSize(QSize(500, 800))
        MainWindow.setMaximumSize(QSize(605, 800))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-av-timer.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/32x32/icons/32x32/timer-icon.png);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(400, 16777215))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_18 = QVBoxLayout(self.page_home)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_div_time_per_frame = QFrame(self.page_home)
        self.frame_div_time_per_frame.setObjectName(u"frame_div_time_per_frame")
        self.frame_div_time_per_frame.setMinimumSize(QSize(0, 140))
        self.frame_div_time_per_frame.setMaximumSize(QSize(390, 200))
        self.frame_div_time_per_frame.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")
        self.frame_div_time_per_frame.setFrameShape(QFrame.NoFrame)
        self.frame_div_time_per_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_div_time_per_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_time_per_frame)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font5)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.labelBoxBlenderInstalation_2)


        self.verticalLayout_10.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_time_per_frame)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_content_wid_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_hours = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_hours.setObjectName(u"lineEdit_hours")
        self.lineEdit_hours.setMinimumSize(QSize(100, 60))
        font6 = QFont()
        font6.setFamily(u"Roboto Thin")
        font6.setPointSize(40)
        self.lineEdit_hours.setFont(font6)
        self.lineEdit_hours.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(41, 46, 57);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(41, 45, 56);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")
        self.lineEdit_hours.setMaxLength(2)
        self.lineEdit_hours.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_hours, 0, 0, 1, 1)

        self.lineEdit_minutes = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_minutes.setObjectName(u"lineEdit_minutes")
        self.lineEdit_minutes.setMinimumSize(QSize(100, 60))
        self.lineEdit_minutes.setFont(font6)
        self.lineEdit_minutes.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(41, 46, 57);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(41, 45, 56);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")
        self.lineEdit_minutes.setMaxLength(2)
        self.lineEdit_minutes.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_minutes, 0, 1, 1, 1)

        self.lineEdit_seconds = QLineEdit(self.frame_content_wid_2)
        self.lineEdit_seconds.setObjectName(u"lineEdit_seconds")
        self.lineEdit_seconds.setMinimumSize(QSize(100, 60))
        self.lineEdit_seconds.setFont(font6)
        self.lineEdit_seconds.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(41, 46, 57);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(41, 45, 56);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")
        self.lineEdit_seconds.setMaxLength(2)
        self.lineEdit_seconds.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_seconds, 0, 2, 1, 1)

        self.label_hours = QLabel(self.frame_content_wid_2)
        self.label_hours.setObjectName(u"label_hours")
        self.label_hours.setMaximumSize(QSize(16777215, 20))
        self.label_hours.setFont(font2)
        self.label_hours.setStyleSheet(u"")
        self.label_hours.setLineWidth(1)
        self.label_hours.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_hours, 1, 0, 1, 1)

        self.label_minutes = QLabel(self.frame_content_wid_2)
        self.label_minutes.setObjectName(u"label_minutes")
        self.label_minutes.setMaximumSize(QSize(16777215, 20))
        self.label_minutes.setFont(font2)
        self.label_minutes.setStyleSheet(u"")
        self.label_minutes.setLineWidth(1)
        self.label_minutes.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_minutes, 1, 1, 1, 1)

        self.label_seconds = QLabel(self.frame_content_wid_2)
        self.label_seconds.setObjectName(u"label_seconds")
        self.label_seconds.setMaximumSize(QSize(16777215, 20))
        self.label_seconds.setFont(font2)
        self.label_seconds.setStyleSheet(u"")
        self.label_seconds.setLineWidth(1)
        self.label_seconds.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_seconds, 1, 2, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_3)


        self.verticalLayout_10.addWidget(self.frame_content_wid_2)


        self.verticalLayout_18.addWidget(self.frame_div_time_per_frame)

        self.frame_div_number_frames = QFrame(self.page_home)
        self.frame_div_number_frames.setObjectName(u"frame_div_number_frames")
        self.frame_div_number_frames.setMinimumSize(QSize(0, 170))
        self.frame_div_number_frames.setMaximumSize(QSize(390, 200))
        self.frame_div_number_frames.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")
        self.frame_div_number_frames.setFrameShape(QFrame.NoFrame)
        self.frame_div_number_frames.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_div_number_frames)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_3 = QFrame(self.frame_div_number_frames)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font5)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout_14.addWidget(self.frame_title_wid_3)

        self.frame_content_wid_3 = QFrame(self.frame_div_number_frames)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_content_wid_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_machines = QLabel(self.frame_content_wid_3)
        self.label_machines.setObjectName(u"label_machines")
        self.label_machines.setMaximumSize(QSize(16777215, 20))
        self.label_machines.setFont(font2)
        self.label_machines.setStyleSheet(u"")
        self.label_machines.setLineWidth(1)
        self.label_machines.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_machines, 1, 1, 1, 1)

        self.lineEdit_machines = QLineEdit(self.frame_content_wid_3)
        self.lineEdit_machines.setObjectName(u"lineEdit_machines")
        self.lineEdit_machines.setMinimumSize(QSize(100, 60))
        self.lineEdit_machines.setFont(font6)
        self.lineEdit_machines.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(41, 46, 57);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(41, 45, 56);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")
        self.lineEdit_machines.setMaxLength(4)
        self.lineEdit_machines.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_machines, 0, 1, 1, 1)

        self.lineEdit_frames = QLineEdit(self.frame_content_wid_3)
        self.lineEdit_frames.setObjectName(u"lineEdit_frames")
        self.lineEdit_frames.setMinimumSize(QSize(100, 60))
        self.lineEdit_frames.setFont(font6)
        self.lineEdit_frames.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(41, 46, 57);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(41, 45, 56);\n"
"	padding: 0px;\n"
"	selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(27, 29, 35);\n"
"}")
        self.lineEdit_frames.setMaxLength(8)
        self.lineEdit_frames.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_frames, 0, 0, 1, 1)

        self.label_frames = QLabel(self.frame_content_wid_3)
        self.label_frames.setObjectName(u"label_frames")
        self.label_frames.setMaximumSize(QSize(16777215, 20))
        self.label_frames.setFont(font2)
        self.label_frames.setStyleSheet(u"")
        self.label_frames.setLineWidth(1)
        self.label_frames.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_frames, 1, 0, 1, 1)

        self.label_current_render = QLabel(self.frame_content_wid_3)
        self.label_current_render.setObjectName(u"label_current_render")
        self.label_current_render.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 2px;\n"
"color: rgb(85, 255, 127);")
        self.label_current_render.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_current_render, 2, 0, 1, 2)


        self.verticalLayout_17.addLayout(self.gridLayout_4)


        self.verticalLayout_14.addWidget(self.frame_content_wid_3)


        self.verticalLayout_18.addWidget(self.frame_div_number_frames)

        self.frame_div_table_widget = QFrame(self.page_home)
        self.frame_div_table_widget.setObjectName(u"frame_div_table_widget")
        self.frame_div_table_widget.setMinimumSize(QSize(0, 40))
        self.frame_div_table_widget.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")
        self.frame_div_table_widget.setFrameShape(QFrame.StyledPanel)
        self.frame_div_table_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_div_table_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_add_render = QPushButton(self.frame_div_table_widget)
        self.pushButton_add_render.setObjectName(u"pushButton_add_render")
        self.pushButton_add_render.setMinimumSize(QSize(120, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(9)
        self.pushButton_add_render.setFont(font7)
        self.pushButton_add_render.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_render.setIcon(icon4)

        self.gridLayout_6.addWidget(self.pushButton_add_render, 0, 1, 1, 1)

        self.lineEdit_description = QLineEdit(self.frame_div_table_widget)
        self.lineEdit_description.setObjectName(u"lineEdit_description")
        self.lineEdit_description.setMinimumSize(QSize(0, 30))
        self.lineEdit_description.setFont(font2)
        self.lineEdit_description.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_description.setMaxLength(32)

        self.gridLayout_6.addWidget(self.lineEdit_description, 0, 0, 1, 1)

        self.tableWidget_renders = QTableWidget(self.frame_div_table_widget)
        if (self.tableWidget_renders.columnCount() < 3):
            self.tableWidget_renders.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_renders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_renders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"DEL");
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_renders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_renders.setObjectName(u"tableWidget_renders")
        sizePolicy.setHeightForWidth(self.tableWidget_renders.sizePolicy().hasHeightForWidth())
        self.tableWidget_renders.setSizePolicy(sizePolicy)
        self.tableWidget_renders.setMinimumSize(QSize(0, 90))
        self.tableWidget_renders.setMaximumSize(QSize(16777215, 100))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.tableWidget_renders.setPalette(palette1)
        self.tableWidget_renders.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(52, 59, 72);	\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_renders.setFrameShape(QFrame.NoFrame)
        self.tableWidget_renders.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_renders.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_renders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_renders.setAutoScroll(False)
        self.tableWidget_renders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_renders.setTabKeyNavigation(False)
        self.tableWidget_renders.setProperty("showDropIndicator", False)
        self.tableWidget_renders.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_renders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_renders.setShowGrid(True)
        self.tableWidget_renders.setGridStyle(Qt.SolidLine)
        self.tableWidget_renders.setSortingEnabled(False)
        self.tableWidget_renders.horizontalHeader().setVisible(False)
        self.tableWidget_renders.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.tableWidget_renders, 1, 0, 1, 2)


        self.verticalLayout_20.addLayout(self.gridLayout_6)


        self.verticalLayout_18.addWidget(self.frame_div_table_widget)

        self.frame_div_render_time = QFrame(self.page_home)
        self.frame_div_render_time.setObjectName(u"frame_div_render_time")
        self.frame_div_render_time.setMinimumSize(QSize(0, 160))
        self.frame_div_render_time.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 10px;\n"
"")
        self.frame_div_render_time.setFrameShape(QFrame.StyledPanel)
        self.frame_div_render_time.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_div_render_time)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_render_time = QLabel(self.frame_div_render_time)
        self.label_render_time.setObjectName(u"label_render_time")
        font8 = QFont()
        font8.setFamily(u"Roboto Thin")
        font8.setPointSize(30)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_render_time.setFont(font8)
        self.label_render_time.setStyleSheet(u"color: rgb(0, 255, 127);")
        self.label_render_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_render_time, 0, 0, 1, 2)

        self.label_machines_2 = QLabel(self.frame_div_render_time)
        self.label_machines_2.setObjectName(u"label_machines_2")
        self.label_machines_2.setMaximumSize(QSize(16777215, 20))
        self.label_machines_2.setFont(font2)
        self.label_machines_2.setStyleSheet(u"")
        self.label_machines_2.setLineWidth(1)
        self.label_machines_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_machines_2, 1, 0, 1, 2)

        self.label_current_time = QLabel(self.frame_div_render_time)
        self.label_current_time.setObjectName(u"label_current_time")
        self.label_current_time.setFont(font8)
        self.label_current_time.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_current_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_current_time, 2, 0, 1, 1)

        self.label_finish_time = QLabel(self.frame_div_render_time)
        self.label_finish_time.setObjectName(u"label_finish_time")
        self.label_finish_time.setFont(font8)
        self.label_finish_time.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.label_finish_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_finish_time, 2, 1, 1, 1)

        self.label_machines_3 = QLabel(self.frame_div_render_time)
        self.label_machines_3.setObjectName(u"label_machines_3")
        self.label_machines_3.setMaximumSize(QSize(16777215, 20))
        self.label_machines_3.setFont(font2)
        self.label_machines_3.setStyleSheet(u"")
        self.label_machines_3.setLineWidth(1)
        self.label_machines_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_machines_3, 3, 0, 1, 1)

        self.label_machines_5 = QLabel(self.frame_div_render_time)
        self.label_machines_5.setObjectName(u"label_machines_5")
        self.label_machines_5.setMaximumSize(QSize(16777215, 20))
        self.label_machines_5.setFont(font2)
        self.label_machines_5.setStyleSheet(u"")
        self.label_machines_5.setLineWidth(1)
        self.label_machines_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_machines_5, 3, 1, 1, 1)

        self.label_day_end = QLabel(self.frame_div_render_time)
        self.label_day_end.setObjectName(u"label_day_end")
        self.label_day_end.setFont(font2)
        self.label_day_end.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 8px;\n"
"color: rgb(255, 0, 127);")
        self.label_day_end.setLineWidth(1)
        self.label_day_end.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_day_end, 4, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_5)


        self.verticalLayout_18.addWidget(self.frame_div_render_time)

        self.stackedWidget.addWidget(self.page_home)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_6 = QVBoxLayout(self.page_info)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.page_info)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 500))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 450))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setStyleSheet(u"background-image: url(:/Images/images/image_about.jpg);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_version_2 = QLabel(self.frame_3)
        self.label_version_2.setObjectName(u"label_version_2")
        self.label_version_2.setGeometry(QRect(290, 170, 61, 25))
        self.label_version_2.setFont(font1)
        self.label_version_2.setStyleSheet(u"background: none;\n"
"background-color: rgba(44, 49, 60, 150);\n"
"border-radius: 5px;\n"
"")
        self.label_version_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.label_title_bar_top_2 = QLabel(self.frame)
        self.label_title_bar_top_2.setObjectName(u"label_title_bar_top_2")
        self.label_title_bar_top_2.setFont(font1)
        self.label_title_bar_top_2.setStyleSheet(u"background: transparent;\n"
"")

        self.gridLayout.addWidget(self.label_title_bar_top_2, 1, 0, 1, 1)

        self.label_credits_2 = QLabel(self.frame)
        self.label_credits_2.setObjectName(u"label_credits_2")
        self.label_credits_2.setFont(font2)
        self.label_credits_2.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.gridLayout.addWidget(self.label_credits_2, 2, 0, 1, 1)

        self.label_credits_3 = QLabel(self.frame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setFont(font2)
        self.label_credits_3.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.gridLayout.addWidget(self.label_credits_3, 3, 0, 1, 1)

        self.label_title_bar_top_4 = QLabel(self.frame)
        self.label_title_bar_top_4.setObjectName(u"label_title_bar_top_4")
        self.label_title_bar_top_4.setFont(font1)
        self.label_title_bar_top_4.setStyleSheet(u"background: transparent;\n"
"")

        self.gridLayout.addWidget(self.label_title_bar_top_4, 4, 0, 1, 1)

        self.btn_artstation = QCommandLinkButton(self.frame)
        self.btn_artstation.setObjectName(u"btn_artstation")
        self.btn_artstation.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_artstation.setIcon(icon5)

        self.gridLayout.addWidget(self.btn_artstation, 5, 0, 1, 1)

        self.label_title_bar_top_5 = QLabel(self.frame)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        self.label_title_bar_top_5.setFont(font1)
        self.label_title_bar_top_5.setStyleSheet(u"background: transparent;\n"
"")

        self.gridLayout.addWidget(self.label_title_bar_top_5, 6, 0, 1, 1)

        self.btn_gumroad = QCommandLinkButton(self.frame)
        self.btn_gumroad.setObjectName(u"btn_gumroad")
        self.btn_gumroad.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        self.btn_gumroad.setIcon(icon5)

        self.gridLayout.addWidget(self.btn_gumroad, 7, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_info)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.lineEdit_hours)
        QWidget.setTabOrder(self.lineEdit_hours, self.lineEdit_minutes)
        QWidget.setTabOrder(self.lineEdit_minutes, self.lineEdit_seconds)
        QWidget.setTabOrder(self.lineEdit_seconds, self.lineEdit_frames)
        QWidget.setTabOrder(self.lineEdit_frames, self.lineEdit_machines)
        QWidget.setTabOrder(self.lineEdit_machines, self.lineEdit_description)
        QWidget.setTabOrder(self.lineEdit_description, self.pushButton_add_render)
        QWidget.setTabOrder(self.pushButton_add_render, self.tableWidget_renders)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"RENDER TIME CALCULATOR", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Calculate a rendering time estimate", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"TIME PER FRAME", None))
        self.lineEdit_hours.setText("")
        self.lineEdit_hours.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lineEdit_minutes.setText("")
        self.lineEdit_minutes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lineEdit_seconds.setText("")
        self.lineEdit_seconds.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_hours.setText(QCoreApplication.translate("MainWindow", u"HOURS", None))
        self.label_minutes.setText(QCoreApplication.translate("MainWindow", u"MINUTES", None))
        self.label_seconds.setText(QCoreApplication.translate("MainWindow", u"SECONDS", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"NUMBER OF FRAMES AND MACHINES", None))
        self.label_machines.setText(QCoreApplication.translate("MainWindow", u"MACHINES", None))
        self.lineEdit_machines.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_machines.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_frames.setText("")
        self.lineEdit_frames.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_frames.setText(QCoreApplication.translate("MainWindow", u"FRAMES", None))
        self.label_current_render.setText(QCoreApplication.translate("MainWindow", u"RENDER ATUAL", None))
        self.pushButton_add_render.setText(QCoreApplication.translate("MainWindow", u"ADD RENDER", None))
        self.lineEdit_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        ___qtablewidgetitem = self.tableWidget_renders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION", None));
        ___qtablewidgetitem1 = self.tableWidget_renders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TIME", None));
        self.label_render_time.setText(QCoreApplication.translate("MainWindow", u"00<small>d</small> 00<small>h</small> 00<small>m</small> 00<small>s", None))
        self.label_machines_2.setText(QCoreApplication.translate("MainWindow", u"ESTIMATED RENDER TIME", None))
        self.label_current_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.label_finish_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.label_machines_3.setText(QCoreApplication.translate("MainWindow", u"CURRENT TIME", None))
        self.label_machines_5.setText(QCoreApplication.translate("MainWindow", u"FINISH TIME", None))
        self.label_day_end.setText(QCoreApplication.translate("MainWindow", u"Ends day 05 at 12h, 49 minutes and 6 seconds", None))
        self.label_version_2.setText(QCoreApplication.translate("MainWindow", u"v2.0.0", None))
        self.label_title_bar_top_2.setText(QCoreApplication.translate("MainWindow", u"RENDER TIME CALCULATOR", None))
        self.label_credits_2.setText(QCoreApplication.translate("MainWindow", u"by: Wanderson M. Pimenta", None))
        self.label_credits_3.setText(QCoreApplication.translate("MainWindow", u"A simple application to calculate rendering time estimates.\n"
"Now in version 2.0.0 it is supported on Mac, Windows and Linux.", None))
        self.label_title_bar_top_4.setText(QCoreApplication.translate("MainWindow", u"ArtStation:", None))
        self.btn_artstation.setText(QCoreApplication.translate("MainWindow", u"artstation.com/vfxonfire", None))
        self.label_title_bar_top_5.setText(QCoreApplication.translate("MainWindow", u"Gumroad:", None))
        self.btn_gumroad.setText(QCoreApplication.translate("MainWindow", u"gumroad.com/blender_addons", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v2.0.0", None))
    # retranslateUi

