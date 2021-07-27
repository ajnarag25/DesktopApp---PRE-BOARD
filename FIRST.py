# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Avor\Desktop\CPET 8\QtProjects\FIRST.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class First(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 331, 51))
        self.label.setStyleSheet("font: 75 12pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 541, 71))
        self.label_8.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 541, 411))
        self.label_4.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 261, 211))
        self.label_2.setStyleSheet("image: url(:/Student/output-onlinepngtools.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 90, 261, 241))
        self.label_3.setStyleSheet("image: url(:/Admin/pic.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Student = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Student.setGeometry(QtCore.QRect(80, 340, 121, 41))
        self.Student.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Student.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 12pt \"Rockwell\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Avor\\Desktop\\CPET 8\\QtProjects\\download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Student.setIcon(icon)
        self.Student.setObjectName("Student")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 340, 121, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 340, 111, 41))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.Admin = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Admin.setGeometry(QtCore.QRect(340, 340, 111, 41))
        self.Admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 12pt \"Rockwell\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Avor\\Desktop\\CPET 8\\QtProjects\\admin-icon-trendy-design-style-isolated-white-background-vector-simple-modern-flat-symbol-web-site-mobile-logo-app-135742404.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Admin.setIcon(icon1)
        self.Admin.setObjectName("Admin")
        self.label_4.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Student.raise_()
        self.label_6.raise_()
        self.Admin.raise_()
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
        self.Student.setText(_translate("MainWindow", "STUDENT"))
        self.Admin.setText(_translate("MainWindow", "ADMIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = First()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
