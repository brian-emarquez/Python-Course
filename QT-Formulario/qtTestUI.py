from PySide2 import QtWidgets

from ui import formulario

class MyQtApp(formulario.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp).__init__(self)
        self.setupUi(self)

