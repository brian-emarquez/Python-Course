################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator)
from PySide2.QtWidgets import *
from datetime import datetime, timedelta
import pytimeparse
import webbrowser

# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT QSS CUSTOM
from ui_styles import Style
# IMPORT FUNCTIONS
from ui_functions import *

# print(platform.system())
# print(platform.release())

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('RENDER TIME CALCULATOR')
        UIFunctions.labelTitle(self, 'RENDER TIME CALCULATOR')
        UIFunctions.labelDescription(self, 'Calculate a rendering time estimate')
        ## ==> END ##

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## REMOVE ==> STANDARD TITLE BAR
        self.resize(500, 800)
        self.setMinimumSize(QSize(500, 800))
        UIFunctions.enableMaximumSize(self, 500, 800)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        #self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################


        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 240, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(400)
        UIFunctions.addNewMenu(self, "Render Time Calculator", "btn_home", "url(:/16x16/icons/16x16/cil-av-timer.png)", True)
        UIFunctions.addNewMenu(self, "About", "btn_settings", "url(:/16x16/icons/16x16/cil-options.png)", False)

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")

        #UIFunctions.selectMenu(getButton.objectName().styleSheet())
        ## ==> END ##

        ## ==> START PAGE
        ########################################################################
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.label_user_icon.hide()
        ## ==> END ##

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget_renders.hide()
        self.ui.label_current_render.hide()
        self.ui.frame_div_table_widget.setMaximumSize(400, 50)
        self.ui.tableWidget_renders.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_renders.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_renders.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.tableWidget_renders.setColumnWidth(0, QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_renders.setColumnWidth(1, 120)
        self.ui.tableWidget_renders.setColumnWidth(2, 50)
        delegate = AlignDelegate(self.ui.tableWidget_renders)
        self.ui.tableWidget_renders.setItemDelegateForColumn(1, delegate)
        self.ui.tableWidget_renders.setItemDelegateForColumn(2, delegate)
        ## ==> END ##

        ## ==> ADD NEW ROW
        self.ui.pushButton_add_render.clicked.connect(lambda: Functions.addTableRow(self))

        ## ==> JUST NUMBERS
        self.onlyInt = QIntValidator()
        # FIELDS
        self.ui.lineEdit_hours.setValidator(self.onlyInt)
        self.ui.lineEdit_minutes.setValidator(self.onlyInt)
        self.ui.lineEdit_seconds.setValidator(self.onlyInt)
        self.ui.lineEdit_frames.setValidator(self.onlyInt)
        self.ui.lineEdit_machines.setValidator(self.onlyInt)

        ## ==> AUTO UPDATE
        Functions.calculateTime(self)
        self.timer = QtCore.QTimer(self)
        self.timer.start(500)
        self.timer.timeout.connect(lambda: Functions.calculateTime(self))

        ## ==> OPEN LINKS
        self.ui.btn_artstation.clicked.connect(lambda: webbrowser.open('https://www.artstation.com/vfxonfire'))
        self.ui.btn_gumroad.clicked.connect(lambda: webbrowser.open('https://gumroad.com/blender_addons'))


        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ########################################################################
    ## TABLE WIDGET ==> FUNCTIONS
    ########################################################################
    def deleteClicked(self):
        button = self.sender()
        table = self.ui.tableWidget_renders
        count = table.rowCount()

        if button:
            row = self.ui.tableWidget_renders.indexAt(button.pos()).row()
            self.ui.tableWidget_renders.removeRow(row)

        if count == 1:
            Functions.toggleTable(self)
            QtCore.QTimer.singleShot(600, lambda: self.ui.tableWidget_renders.hide())
            QtCore.QTimer.singleShot(600, lambda: self.ui.label_current_render.hide())

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):

        # GET BT CLICKED
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_info)
            UIFunctions.resetStyle(self, "btn_settings")
            UIFunctions.labelPage(self, "About")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, obj, event):
        pass
        # if isinstance(obj, QLineEdit) and event.type() == QEvent.keyPressEvent:
        #     i = obj.property("index")
        #     self.keyPressEvent.emit(i)
        # return QWidget.eventFilter(self, obj, event)
    ## ==> END ##

    ## ==> keyReleaseEvent
    ########################################################################
    def keyReleaseEvent(self, event):
        pass
        #Functions.calculateTime(self)

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')
        # if event.buttons() == Qt.MidButton:
        #     print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        pass
        # print('Text Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        pass
        # print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(':/Fonts/fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont(':/Fonts/fonts/segoeuib.ttf')
    QtGui.QFontDatabase.addApplicationFont(':/Fonts/fonts/Roboto-Regular.ttf')
    QtGui.QFontDatabase.addApplicationFont(':/Fonts/fonts/Roboto-Thin.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
