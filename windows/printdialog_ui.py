# Form implementation generated from reading ui file 'c:\Users\AdminHome\Documents\GitHub\bewertungsrechner\windows\printdialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_print_dialog(object):
    def setupUi(self, print_dialog):
        print_dialog.setObjectName("print_dialog")
        print_dialog.resize(400, 322)
        self.student_list = QtWidgets.QListWidget(parent=print_dialog)
        self.student_list.setGeometry(QtCore.QRect(10, 10, 381, 201))
        self.student_list.setStyleSheet("border-style: outset;\n"
"border-radius:  10px;\n"
"font: 14px;")
        self.student_list.setObjectName("student_list")
        self.selectall_button = QtWidgets.QPushButton(parent=print_dialog)
        self.selectall_button.setGeometry(QtCore.QRect(10, 260, 381, 23))
        self.selectall_button.setStyleSheet("background-color: rgb(216, 204, 231);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:  10px;\n"
"border-color: black;\n"
"border-color: gray;\n"
"font: 14px;")
        self.selectall_button.setObjectName("selectall_button")
        self.printoverview_button = QtWidgets.QPushButton(parent=print_dialog)
        self.printoverview_button.setGeometry(QtCore.QRect(10, 290, 151, 23))
        self.printoverview_button.setStyleSheet("background-color: rgb(127, 169, 112);\n"
"border-style: outset;\n"
"border-radius:  10px;\n"
"border-color: white;\n"
"font: bold 14px;")
        self.printoverview_button.setObjectName("printoverview_button")
        self.exit_button = QtWidgets.QPushButton(parent=print_dialog)
        self.exit_button.setGeometry(QtCore.QRect(270, 220, 120, 23))
        self.exit_button.setStyleSheet("background-color: rgb(127, 169, 112);\n"
"border-style: outset;\n"
"border-radius:  10px;\n"
"border-color: white;\n"
"font: bold 14px;")
        self.exit_button.setObjectName("exit_button")
        self.printstudent_button = QtWidgets.QPushButton(parent=print_dialog)
        self.printstudent_button.setGeometry(QtCore.QRect(270, 290, 120, 23))
        self.printstudent_button.setStyleSheet("background-color: rgb(127, 169, 112);\n"
"border-style: outset;\n"
"border-radius:  10px;\n"
"border-color: white;\n"
"font: bold 14px;")
        self.printstudent_button.setObjectName("printstudent_button")
        self.resultname_label = QtWidgets.QLabel(parent=print_dialog)
        self.resultname_label.setEnabled(True)
        self.resultname_label.setGeometry(QtCore.QRect(200, 100, 47, 13))
        self.resultname_label.setText("")
        self.resultname_label.setObjectName("resultname_label")
        self.CheckBoxDurchschnitt = QtWidgets.QCheckBox(parent=print_dialog)
        self.CheckBoxDurchschnitt.setGeometry(QtCore.QRect(20, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.CheckBoxDurchschnitt.setFont(font)
        self.CheckBoxDurchschnitt.setStyleSheet("background-color: rgb(216, 204, 231);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:  10px;\n"
"border-color: black;\n"
"border-color: gray;\n"
"font: 14px;")
        self.CheckBoxDurchschnitt.setObjectName("CheckBoxDurchschnitt")
        self.resultname_label.raise_()
        self.student_list.raise_()
        self.selectall_button.raise_()
        self.printoverview_button.raise_()
        self.exit_button.raise_()
        self.printstudent_button.raise_()
        self.CheckBoxDurchschnitt.raise_()

        self.retranslateUi(print_dialog)
        self.exit_button.clicked.connect(print_dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(print_dialog)

    def retranslateUi(self, print_dialog):
        _translate = QtCore.QCoreApplication.translate
        print_dialog.setWindowTitle(_translate("print_dialog", "Drucken"))
        self.selectall_button.setText(_translate("print_dialog", "Alle auswählen"))
        self.printoverview_button.setText(_translate("print_dialog", "Auswertung Drucken"))
        self.exit_button.setText(_translate("print_dialog", "Abbrechen"))
        self.printstudent_button.setText(_translate("print_dialog", "Schüler Drucken"))
        self.CheckBoxDurchschnitt.setText(_translate("print_dialog", "Durchschnitt"))
