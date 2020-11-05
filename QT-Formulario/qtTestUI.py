from PySide2 import QtWidgets

import formulario

class MyQtApp(formulario.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("My Qt Aplication - Build 252")
        self.populate_tree_widget()
        self.populate_list_widget()
        self.submit_PB.clicked.connect(self.fill_form)
        self.toolButton.clicked.connect(self.select_photo)

    def populate_tree_widget(self):
        self.my_treeWidget.setHeaderLabels(["ID", "NAME", "COLOR"])
        self.my_treeWidget.clear()
        x =["applee", "banana", "mango", "orange"]

        for i, e in enumerate(x):
            item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
            item.setText(0, str(i))
            item.setText(1, e)

    def populate_list_widget(self):
        self.listWidget.clear()
        item = ["a", "b", "c"]
        self.listWidget.addItems(item)

    # Message warning
    def fill_form(self):
        name = self.name_LE.text()
        #print(name)
        if not name:
            QtWidgets.QMessageBox.about(self,"Name Requiered", "Hey ! fill the name")
            return
        photo = self.photo_LE.text()

    # show archive route
    def select_photo(self):
        photo_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, "Select Photo")
        if photo_path:
            self.photo_LE.setText(photo_path)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


