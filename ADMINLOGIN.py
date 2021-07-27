# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Avor\Desktop\CPET 8\QtProjects\ADMINLOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Admin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 331, 51))
        self.label.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 481, 71))
        self.label_8.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 481, 361))
        self.label_4.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(160, 140, 251, 31))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(160, 190, 251, 31))
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 151, 51))
        self.label_3.setStyleSheet("font: 75 10pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 151, 51))
        self.label_2.setStyleSheet("font: 75 8pt \"Rockwell\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 250, 141, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 250, 101, 41))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.ImNotAnAdmin = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ImNotAnAdmin.setGeometry(QtCore.QRect(160, 250, 141, 41))
        self.ImNotAnAdmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImNotAnAdmin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.ImNotAnAdmin.setObjectName("ImNotAnAdmin")
        self.CONFIRM = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CONFIRM.setGeometry(QtCore.QRect(310, 250, 101, 41))
        self.CONFIRM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CONFIRM.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"Rockwell\";")
        self.CONFIRM.setObjectName("CONFIRM")
        self.label_4.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.Username.raise_()
        self.Password.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.ImNotAnAdmin.raise_()
        self.CONFIRM.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">I.E DEPARTMENT</span></p></body></html>"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">PASSWORD :</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:400;\">USERNAME :</span></p></body></html>"))
        self.ImNotAnAdmin.setText(_translate("MainWindow", "I\'m Not an Admin"))
        self.CONFIRM.setText(_translate("MainWindow", "CONFIRM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Admin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
