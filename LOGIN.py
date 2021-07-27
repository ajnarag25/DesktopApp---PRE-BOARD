# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\AVOR\Desktop\CPET 8\QtProjects\LOG IN.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 501, 71))
        self.label_9.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 501, 361))
        self.label_4.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(160, 190, 251, 31))
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 151, 51))
        self.label_3.setStyleSheet("font: 75 10pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(160, 140, 251, 31))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 151, 51))
        self.label_2.setStyleSheet("font: 75 8pt \"Rockwell\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 250, 101, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 250, 101, 41))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 331, 51))
        self.label.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.SIGNUP = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.SIGNUP.setGeometry(QtCore.QRect(160, 250, 101, 41))
        self.SIGNUP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SIGNUP.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.SIGNUP.setObjectName("SIGNUP")
        self.CONFIRM = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CONFIRM.setGeometry(QtCore.QRect(310, 250, 101, 41))
        self.CONFIRM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CONFIRM.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.CONFIRM.setObjectName("CONFIRM")
        self.RETURN = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.RETURN.setGeometry(QtCore.QRect(380, 20, 91, 41))
        self.RETURN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RETURN.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\AVOR\\Desktop\\CPET 8\\QtProjects\\istockphoto-827252562-612x612.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RETURN.setIcon(icon)
        self.RETURN.setObjectName("RETURN")
        self.label_4.raise_()
        self.label_9.raise_()
        self.Password.raise_()
        self.label_3.raise_()
        self.Username.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.SIGNUP.raise_()
        self.CONFIRM.raise_()
        self.RETURN.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">PASSWORD :</span></p></body></html>"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">USERNAME :</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">I.E DEPARTMENT</span></p></body></html>"))
        self.SIGNUP.setText(_translate("MainWindow", "SIGNUP"))
        self.CONFIRM.setText(_translate("MainWindow", "CONFIRM"))
        self.RETURN.setText(_translate("MainWindow", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
