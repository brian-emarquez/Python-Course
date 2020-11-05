from PySide2 import QtWidgets

import formulario

class MyQtApp(formulario.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("My Qt Aplication - Build 252")
        self.populate_tree_widget()

    def populate_tree_widget(self):
        self.my_treeWidget.clear()
        x =["applee", "banana", "mango", "orange"]
        item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)

        for e in x:
            item.setText(0, e)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


