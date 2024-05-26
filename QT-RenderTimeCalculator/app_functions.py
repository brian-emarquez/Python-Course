################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

# GUI FILE
from main import *

class Functions(MainWindow):

    ## ==> GLOBALS
    globals()['atual_render_time'] = timedelta()
    globals()['total_render_time'] = timedelta()

    ## ==> ADD RENDER TIME TO TABLE WIDGET
    ########################################################################
    def addTableRow(self):
        lineDescription = str(self.ui.lineEdit_description.text())
        table = self.ui.tableWidget_renders
        rowPosition = table.rowCount()
        atualTime = globals()['atual_render_time']

        if lineDescription != '':
            table.insertRow(rowPosition)
            description = lineDescription.upper()
            time = str(atualTime)
            deleteButton = QPushButton()
            deleteButton.clicked.connect(self.deleteClicked)
            deleteButton.setStyleSheet(Style.style_bt_delet_row)
            icon_bt_del = QIcon()
            icon_bt_del.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(16,16), QIcon.Normal, QIcon.Off)
            deleteButton.setIcon(icon_bt_del)
            deleteButton.setMaximumSize(QSize(40, 20))

            table.setItem(rowPosition, 0, QTableWidgetItem(description))
            table.setItem(rowPosition, 1, QTableWidgetItem(time))
            table.setCellWidget(rowPosition, 2, deleteButton)
            table.setRowHeight(rowPosition, 20)

            ## ==> CLEAR LINE EDIT
            self.ui.lineEdit_description.setText("")
            self.ui.lineEdit_description.setStyleSheet(Style.style_LineEdit)
            self.ui.lineEdit_description.setPlaceholderText("Description")

            ## ==> CLEAR FIELDS
            self.ui.lineEdit_hours.setText("")
            self.ui.lineEdit_minutes.setText("")
            self.ui.lineEdit_seconds.setText("")
            self.ui.lineEdit_frames.setText("")

            if not rowPosition:
                Functions.toggleTable(self)
                QtCore.QTimer.singleShot(350, lambda: self.ui.tableWidget_renders.show())
                QtCore.QTimer.singleShot(350, lambda: self.ui.label_current_render.show())

        else:
            self.ui.lineEdit_description.setStyleSheet(Style.style_LineEdit_empyt)
            self.ui.lineEdit_description.setPlaceholderText("ADD A DESCRIPTION BEFORE!")

    ## ==> TOGGLE TABLE WIDGET
    ########################################################################
    def toggleTable(self):
        height = self.ui.frame_div_table_widget.height()
        maxExtend = 170
        standard = 50

        # SET MAX WIDTH
        if height == 50:
            heightExtended = maxExtend
        else:
            heightExtended = standard

        self.animation = QPropertyAnimation(self.ui.frame_div_table_widget, b"maximumHeight")
        self.animation.setDuration(600)
        self.animation.setStartValue(height)
        self.animation.setEndValue(heightExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    ## ==> CALCULATE TIME
    ########################################################################
    def calculateTime(self):
        tableTrue = self.ui.tableWidget_renders.rowCount()

        # GET HOURS
        getHours = self.ui.lineEdit_hours.text()
        if not getHours:
            getHours = '0'

        # GET MINUTES
        getMinutes = self.ui.lineEdit_minutes.text()
        if not getMinutes:
            getMinutes = '0'
        if int(getMinutes) > 59:
            self.ui.lineEdit_minutes.setText('59')

        # GET SECONDS
        getSeconds = self.ui.lineEdit_seconds.text()
        if not getSeconds:
            getSeconds = '0'
        if int(getSeconds) > 59:
            self.ui.lineEdit_seconds.setText('59')

        # GET FRAMES
        getNumFrame = self.ui.lineEdit_frames.text()
        if not getNumFrame:
            getNumFrame = '0'

        # GET MACHINES
        getNumMachines = self.ui.lineEdit_machines.text()
        if not getNumMachines or int(getNumMachines) == 0:
            self.ui.lineEdit_machines.setText('1')
            getNumMachines = '1'

        ## ==> STANDARD TIME
        timeNow = datetime.today()
        frameTime = timedelta(hours=int(getHours), minutes=int(getMinutes), seconds=int(getSeconds))
        mathDateEnd = timeNow + (frameTime * int(getNumFrame) / int(getNumMachines))
        totalTime = mathDateEnd - timeNow

        ## ==> IF TABLE EXIST SET TOTAL RENDER TIME
        if tableTrue != 0:
            splitTime = str(totalTime).split(':')
            days = splitTime[0].replace(' days,', 'd').replace(' day,', 'd')
            strRenderRime =  days + 'h ' + splitTime[1] + 'm ' + splitTime[2][:2] + 's'
            self.ui.label_current_render.setText(strRenderRime)

            totalTimeGlobal = globals()['total_render_time']
        else:
            totalTimeGlobal = totalTime

        ## ==> SPLIT TIMES
        splitTime = str(totalTimeGlobal).split(':')
        days = splitTime[0].replace(' days,', 'd').replace(' day,', 'd')
        strRenderRime =  days + 'h ' + splitTime[1] + 'm ' + splitTime[2][:2] + 's'

        ## ==> IF TABLE EXIST SOME TIME NOW WITH TABLE
        if tableTrue != 0:
            mathDateEnd = timeNow + globals()['total_render_time']

        strDayEnd = 'Ends <b>day ' + str(mathDateEnd.day) + '</b> at <b>' + str(mathDateEnd.hour) + 'h</b>, <b>' + str(mathDateEnd.minute) + 'm</b> and <b>' + str(mathDateEnd.second)[:2] + 's</b>'

        ## ==> SET TIME ATUAL AND SUM TABLE
        globals()['atual_render_time'] = totalTime
        Functions.calculateTable(self)

        ## ==> SET RESULT
        self.ui.label_render_time.setText(strRenderRime)
        self.ui.label_current_time.setText(timeNow.strftime("%H:%M"))
        setMinutes = str(mathDateEnd.minute)
        if mathDateEnd.minute <= 9:
            setMinutes = '0' + str(mathDateEnd.minute)
        self.ui.label_finish_time.setText(str(mathDateEnd.hour) + ':' + setMinutes)
        self.ui.label_day_end.setText(strDayEnd)

    def appendTime(self):
        time = []
        rows = self.ui.tableWidget_renders.rowCount()
        table = self.ui.tableWidget_renders

        row = 0
        for t in range(0, rows):
            time.append(table.item(row, 1).text())
            row += 1
        return time

    def reconstruct_timedelta(td_string):
        seconds = pytimeparse.parse(td_string)
        return timedelta(seconds=seconds)

    def calculateTable(self):
        currentRender = globals()['atual_render_time']
        globals()['total_render_time'] = currentRender
        time = Functions.appendTime(self)

        for t in time:
            td_reconstructed = Functions.reconstruct_timedelta(t)
            sumTime = td_reconstructed + globals()['total_render_time']
            globals()['total_render_time'] = sumTime
