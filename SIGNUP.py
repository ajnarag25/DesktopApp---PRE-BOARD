# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Levy Batario\Desktop\SIGN UP.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Signup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 481, 71))
        self.label_8.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 151, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 151, 51))
        self.label_3.setStyleSheet("font: 75 10pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 151, 51))
        self.label_6.setStyleSheet("font: 75 10pt \"Rockwell\";\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.firstshift = QtWidgets.QRadioButton(self.centralwidget)
        self.firstshift.setGeometry(QtCore.QRect(200, 230, 81, 31))
        self.firstshift.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firstshift.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.firstshift.setObjectName("firstshift")
        self.Firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.Firstname.setGeometry(QtCore.QRect(170, 150, 251, 31))
        self.Firstname.setText("")
        self.Firstname.setFrame(True)
        self.Firstname.setReadOnly(False)
        self.Firstname.setObjectName("Firstname")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 400, 141, 41))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(170, 270, 251, 31))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 331, 51))
        self.label.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.Middlename = QtWidgets.QLineEdit(self.centralwidget)
        self.Middlename.setGeometry(QtCore.QRect(170, 190, 251, 31))
        self.Middlename.setText("")
        self.Middlename.setFrame(True)
        self.Middlename.setReadOnly(False)
        self.Middlename.setObjectName("Middlename")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 151, 51))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.label_9.setObjectName("label_9")
        self.ConfirmButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ConfirmButton.setGeometry(QtCore.QRect(300, 400, 111, 41))
        self.ConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Rockwell\";\n"
"background-color: rgb(170, 0, 0);")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.secondshift = QtWidgets.QRadioButton(self.centralwidget)
        self.secondshift.setGeometry(QtCore.QRect(290, 230, 91, 31))
        self.secondshift.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.secondshift.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"")
        self.secondshift.setObjectName("secondshift")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 491, 461))
        self.label_4.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 151, 51))
        self.label_2.setStyleSheet("font: 75 8pt \"Rockwell\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 350, 161, 31))
        self.label_10.setStyleSheet("font: 75 10pt \"Rockwell\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.Lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.Lastname.setGeometry(QtCore.QRect(170, 110, 251, 31))
        self.Lastname.setText("")
        self.Lastname.setFrame(True)
        self.Lastname.setReadOnly(False)
        self.Lastname.setObjectName("Lastname")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 151, 51))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.label_7.setObjectName("label_7")
        self.ConfirmPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.ConfirmPassword.setGeometry(QtCore.QRect(170, 350, 251, 31))
        self.ConfirmPassword.setText("")
        self.ConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassword.setObjectName("ConfirmPassword")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(170, 310, 251, 31))
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.ConfirmButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ConfirmButton_2.setGeometry(QtCore.QRect(30, 400, 141, 41))
        self.ConfirmButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Rockwell\";\n"
"background-color: rgb(170, 0, 0);")
        self.ConfirmButton_2.setObjectName("ConfirmButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(300, 400, 111, 41))
        self.label_12.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.firstshift.raise_()
        self.Firstname.raise_()
        self.Username.raise_()
        self.Middlename.raise_()
        self.label_9.raise_()
        self.secondshift.raise_()
        self.label_2.raise_()
        self.label_10.raise_()
        self.Lastname.raise_()
        self.label_7.raise_()
        self.ConfirmPassword.raise_()
        self.Password.raise_()
        self.label.raise_()
        self.label_11.raise_()
        self.label_3.raise_()
        self.ConfirmButton_2.raise_()
        self.label_12.raise_()
        self.ConfirmButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">LAST NAME :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">PASSWORD :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">SHIFT :</span></p></body></html>"))
        self.firstshift.setText(_translate("MainWindow", "1st Shift"))
        self.Firstname.setPlaceholderText(_translate("MainWindow", "FirstName"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">I.E DEPARTMENT</span></p></body></html>"))
        self.Middlename.setPlaceholderText(_translate("MainWindow", "MiddleName"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">MIDDLE NAME :</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("MainWindow", "CONFIRM"))
        self.secondshift.setText(_translate("MainWindow", "2nd Shift"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">USERNAME :</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CONFIRM :</span></p></body></html>"))
        self.Lastname.setPlaceholderText(_translate("MainWindow", "LastName"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">FIRST NAME :</span></p></body></html>"))
        self.ConfirmPassword.setPlaceholderText(_translate("MainWindow", "ConfirmPassword"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.ConfirmButton_2.setText(_translate("MainWindow", "BACK TO LOGIN"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
