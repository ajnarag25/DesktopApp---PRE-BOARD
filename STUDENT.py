# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Avor\Desktop\CPET 8\QtProjects\STUDENT.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Student(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EXAMframe = QtWidgets.QFrame(self.centralwidget)
        self.EXAMframe.setGeometry(QtCore.QRect(180, 80, 861, 471))
        self.EXAMframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EXAMframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EXAMframe.setObjectName("EXAMframe")
        self.SAVE = QtWidgets.QCommandLinkButton(self.EXAMframe)
        self.SAVE.setGeometry(QtCore.QRect(560, 390, 211, 41))
        self.SAVE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SAVE.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Rockwell\";")
        self.SAVE.setObjectName("SAVE")
        self.label_3 = QtWidgets.QLabel(self.EXAMframe)
        self.label_3.setGeometry(QtCore.QRect(560, 390, 211, 41))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.EXAMframe)
        self.label_6.setGeometry(QtCore.QRect(570, 270, 191, 61))
        self.label_6.setStyleSheet("font: 75 15pt \"Rockwell\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.TAKEEXAM = QtWidgets.QCommandLinkButton(self.EXAMframe)
        self.TAKEEXAM.setGeometry(QtCore.QRect(240, 150, 381, 91))
        self.TAKEEXAM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TAKEEXAM.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 48pt \"Rockwell\";")
        icon = QtGui.QIcon.fromTheme("none")
        self.TAKEEXAM.setIcon(icon)
        self.TAKEEXAM.setObjectName("TAKEEXAM")
        self.label_5 = QtWidgets.QLabel(self.EXAMframe)
        self.label_5.setGeometry(QtCore.QRect(0, 150, 861, 91))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_42 = QtWidgets.QLabel(self.EXAMframe)
        self.label_42.setGeometry(QtCore.QRect(0, 10, 861, 131))
        self.label_42.setStyleSheet("image: url(:/Student/output-onlinepngtools.png);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.EXAMframe)
        self.label_43.setGeometry(QtCore.QRect(130, 270, 361, 151))
        self.label_43.setStyleSheet("font: 75 15pt \"Rockwell\";\n"
"")
        self.label_43.setObjectName("label_43")
        self.dateEdit = QtWidgets.QDateEdit(self.EXAMframe)
        self.dateEdit.setGeometry(QtCore.QRect(560, 351, 211, 41))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_3.raise_()
        self.SAVE.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.TAKEEXAM.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.dateEdit.raise_()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1041, 551))
        self.label_4.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1041, 81))
        self.label.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 1041, 61))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 181, 471))
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 130, 181, 91))
        self.label_8.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.EXAM = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.EXAM.setGeometry(QtCore.QRect(0, 150, 181, 51))
        self.EXAM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EXAM.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 20pt \"Rockwell\";")
        self.EXAM.setObjectName("EXAM")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 280, 181, 91))
        self.label_9.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.RESULTS = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.RESULTS.setGeometry(QtCore.QRect(0, 300, 181, 51))
        self.RESULTS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RESULTS.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 20pt \"Rockwell\";")
        self.RESULTS.setObjectName("RESULTS")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 161, 111))
        self.label_10.setStyleSheet("image: url(:/Python/5848152fcef1014c0b5e4967.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.StudentResults = QtWidgets.QFrame(self.centralwidget)
        self.StudentResults.setGeometry(QtCore.QRect(180, 80, 861, 471))
        self.StudentResults.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StudentResults.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StudentResults.setObjectName("StudentResults")
        self.label_23 = QtWidgets.QLabel(self.StudentResults)
        self.label_23.setGeometry(QtCore.QRect(140, 200, 331, 81))
        self.label_23.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.StudentResults)
        self.label_24.setGeometry(QtCore.QRect(0, 10, 861, 151))
        self.label_24.setStyleSheet("image: url(:/Student/output-onlinepngtools.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.THERESULT = QtWidgets.QLabel(self.StudentResults)
        self.THERESULT.setGeometry(QtCore.QRect(470, 210, 241, 61))
        self.THERESULT.setStyleSheet("font: 75 25pt \"Rockwell\";")
        self.THERESULT.setText("")
        self.THERESULT.setObjectName("THERESULT")
        self.FEEDBACK = QtWidgets.QCommandLinkButton(self.StudentResults)
        self.FEEDBACK.setGeometry(QtCore.QRect(260, 330, 361, 91))
        self.FEEDBACK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FEEDBACK.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 48pt \"Rockwell\";")
        icon = QtGui.QIcon.fromTheme("none")
        self.FEEDBACK.setIcon(icon)
        self.FEEDBACK.setObjectName("FEEDBACK")
        self.label_25 = QtWidgets.QLabel(self.StudentResults)
        self.label_25.setGeometry(QtCore.QRect(-10, 330, 871, 91))
        self.label_25.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_23.raise_()
        self.label_24.raise_()
        self.THERESULT.raise_()
        self.label_25.raise_()
        self.FEEDBACK.raise_()
        self.HOME = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.HOME.setGeometry(QtCore.QRect(80, 20, 101, 41))
        self.HOME.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HOME.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Rockwell\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Avor\\Desktop\\CPET 8\\QtProjects\\83684799-premium-home-icon-or-logo-in-line-style-high-quality-sign-and-symbol-on-a-white-background-vector-ou.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HOME.setIcon(icon)
        self.HOME.setObjectName("HOME")
        self.LOGOUT = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LOGOUT.setGeometry(QtCore.QRect(860, 20, 131, 41))
        self.LOGOUT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LOGOUT.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Rockwell\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Avor\\Desktop\\CPET 8\\QtProjects\\istockphoto-827252562-612x612.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGOUT.setIcon(icon1)
        self.LOGOUT.setObjectName("LOGOUT")
        self.HOMEframe = QtWidgets.QFrame(self.centralwidget)
        self.HOMEframe.setGeometry(QtCore.QRect(180, 80, 861, 471))
        self.HOMEframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HOMEframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HOMEframe.setObjectName("HOMEframe")
        self.label_11 = QtWidgets.QLabel(self.HOMEframe)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 861, 71))
        self.label_11.setStyleSheet("font: 75 25pt \"Rockwell\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.HOMEframe)
        self.label_12.setGeometry(QtCore.QRect(70, 40, 211, 151))
        self.label_12.setStyleSheet("image: url(:/Student/output-onlinepngtools.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.HOMEframe)
        self.label_13.setGeometry(QtCore.QRect(0, 120, 861, 51))
        self.label_13.setStyleSheet("font: 75 12pt \"Rockwell\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.HOMEframe)
        self.label_14.setGeometry(QtCore.QRect(620, 400, 61, 16))
        self.label_14.setStyleSheet("font: 75 12pt \"Rockwell\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.HOMEframe)
        self.label_15.setGeometry(QtCore.QRect(0, 210, 861, 191))
        self.label_15.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_15.setObjectName("label_15")
        self.DATE = QtWidgets.QLabel(self.HOMEframe)
        self.DATE.setGeometry(QtCore.QRect(690, 400, 131, 16))
        self.DATE.setText("")
        self.DATE.setObjectName("DATE")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.EXAM.raise_()
        self.label_9.raise_()
        self.RESULTS.raise_()
        self.label_10.raise_()
        self.HOME.raise_()
        self.LOGOUT.raise_()
        self.HOMEframe.raise_()
        self.EXAMframe.raise_()
        self.StudentResults.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StudentMain"))
        self.SAVE.setText(_translate("MainWindow", "SAVE"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NOT TAKING THE</p><p align=\"center\"> EXAM FOR NOW :</p></body></html>"))
        self.TAKEEXAM.setText(_translate("MainWindow", "TAKE EXAM"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NOTE: </p><p align=\"center\">Students can set a date of examination, </p><p align=\"center\">but be sure</p><p align=\"center\">that you will take it on time.</p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">I.E DEPARTMENT</span></p></body></html>"))
        self.EXAM.setText(_translate("MainWindow", "EXAM"))
        self.RESULTS.setText(_translate("MainWindow", "RESULTS"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">YOUR RESULT IS :</span></p></body></html>"))
        self.FEEDBACK.setText(_translate("MainWindow", "FEEDBACK"))
        self.HOME.setText(_translate("MainWindow", "HOME"))
        self.LOGOUT.setText(_translate("MainWindow", "LOG OUT"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">WELCOME</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">STUDENT</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "DATE :"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\'Welcome student, here you can now access the system</span></p><p align=\"center\"><span style=\" font-size:18pt;\">by taking the exam or setting a date to your exam. You can </span></p><p align=\"center\"><span style=\" font-size:18pt;\">also show/view the results of your examination. </span></p><p align=\"center\"><span style=\" font-size:18pt;\">Have a great day.\'</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Student()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
