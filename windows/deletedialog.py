# Form implementation generated from reading ui file 'windows/deletedialog.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_delete_dialog(object):
    def setupUi(self, delete_dialog):
        delete_dialog.setObjectName("delete_dialog")
        delete_dialog.resize(319, 69)
        delete_dialog.setStyleSheet("background-color: rgb(206, 211, 196);")
        self.select_box = QtWidgets.QComboBox(parent=delete_dialog)
        self.select_box.setGeometry(QtCore.QRect(10, 10, 301, 22))
        self.select_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(151, 145, 174);")
        self.select_box.setObjectName("select_box")
        self.delete_button = QtWidgets.QPushButton(parent=delete_dialog)
        self.delete_button.setGeometry(QtCore.QRect(10, 40, 141, 23))
        self.delete_button.setStyleSheet("background-color: rgb(127, 169, 112);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:  10px;\n"
"border-color: white;\n"
"font: bold 14px;")
        self.delete_button.setObjectName("delete_button")
        self.exit_button = QtWidgets.QPushButton(parent=delete_dialog)
        self.exit_button.setGeometry(QtCore.QRect(170, 40, 141, 23))
        self.exit_button.setStyleSheet("background-color: rgb(127, 169, 112);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:  10px;\n"
"border-color: white;\n"
"font: bold 14px;")
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(delete_dialog)
        self.exit_button.clicked.connect(delete_dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(delete_dialog)

    def retranslateUi(self, delete_dialog):
        _translate = QtCore.QCoreApplication.translate
        delete_dialog.setWindowTitle(_translate("delete_dialog", "Delete"))
        self.delete_button.setText(_translate("delete_dialog", "Löschen"))
        self.exit_button.setText(_translate("delete_dialog", "Abbrechen"))
