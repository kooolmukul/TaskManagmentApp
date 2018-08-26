# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/Task ManagementA11239.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import qdarkstyle
import smtplib
import time
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import database

class Ui_TaskManagement(object):

    def getSelectedRowData(self):
        liste = []
        if(self.tableWidget.currentRow() > -1):
            for i in range(5):
                liste.append(self.tableWidget.item(self.tableWidget.currentRow(), i).text())
        print(liste)
        return liste


    def rowSelectionEvent(self):
        items = self.getSelectedRowData()
        if(len(items) != 0):
            # data = self.tableWidget.selectedItems()
            self.taskEdit.setPlainText(items[1])
            self.assignComboBox.setCurrentIndex(self.assignComboBox.findText(items[2]))
            self.statusComboBox.setCurrentIndex(self.statusComboBox.findText(items[3]))
            formatedDate = QtCore.QDateTime.fromString( time.strftime ( '%a %b %d %H:%M:%S %Y',time.strptime(items[4], '%d-%m-%Y %I:%M %p' )))
            self.dateTimeEdit.setDateTime(formatedDate)
            
        


    def getTaskList(self):
        self.clearTableList()
        for row in database.view():
            self.addRow(list(map(str, row)) ) 

    def clearTableList(self):
         while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)

    def addBtnAction(self):
        #print(self.tableWidget.currentRow() ) 
        # a =  self.tableWidget.selectedIndexes()
        # for index in a:
        #     text = u"(%i,%i)" % (index.row(), index.column())
        #     print(text)
        if(self.taskEdit.toPlainText() != ''):
            database.insert(self.taskEdit.toPlainText(), self.assignComboBox.currentText(),time.strftime('%d-%m-%Y %I:%M %p',time.strptime(self.dateTimeEdit.dateTime().toString() ) ))
            self.getTaskList()

    def deleteBtnAction(self):
        selectedData = self.getSelectedRowData()
        if( len(selectedData) != 0 ):
            database.delete(int(selectedData[0]))
            self.getTaskList()

    def updateBtnAction(self):
        selectedData = self.getSelectedRowData()
        if( len(selectedData) != 0 ):
            formatedDate = time.strftime('%d-%m-%Y %I:%M %p',time.strptime(self.dateTimeEdit.dateTime().toString() ) )
            database.update(int(selectedData[0]),self.taskEdit.toPlainText(), self.assignComboBox.currentText(), formatedDate, self.statusComboBox.currentText())
            self.getTaskList()

    def addRow(self, row):
        _translate = QtCore.QCoreApplication.translate
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(row[0]) )
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(row[1]))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(row[2]))
        self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(row[3]))
        self.tableWidget.setItem(numRows, 4, QtWidgets.QTableWidgetItem(row[4]))
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("TaskManagement", row[0]))
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("TaskManagement", row[1]))
        # item = self.tableWidget.item(0, 2)
        # item.setText(_translate("TaskManagement", row[2]))
        # item = self.tableWidget.item(0, 3)
        # item.setText(_translate("TaskManagement", row[3] ))

    def notifyTask(self):
        nameToEmail = {'Harshit': 'harshit.gohil10@gmail.com', 'Pratik' : 'pratikghanwat7@gmail.com', 'Sandeep': 'sandeep.uniyal08@gmail.com'}
        selectedData = self.getSelectedRowData()
        if( len(selectedData) != 0 ):
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login('bakchodcommittee@gmail.com','bakchodvilla@12345')
            receivers = [nameToEmail[selectedData[2]]]
            message = '\r\n'.join(["From: BakChodVilla <noreply@from.com>",
                        "To: %s %s" % (selectedData[2], nameToEmail[selectedData[2]] ) ,
                        "MIME-Version: 1.0",
                        "Content-type: text/html",
                        "Subject: Task assignement : %s" % selectedData[1],
                        "Oye %s, <br> A Task is assigned to you by BackChodVilla committee." % selectedData[2] ,
                        "<br><b>Task : </b> %s" % selectedData[1],
                       "<br><b>Status : </b> %s" % selectedData[3],
                       "<br><b>Deadline : </b> %s" % selectedData[4],
                        "<br><br> Please complete your task ASAP for a peaceful life",
                        "<br>and",
                        "<br><b> Kripya Shanti Banaye Rakhe!!</b>",
                        "<br><br> <h1 style='color: #5e9ca0; text-align: center;'><em><span style='text-decoration: underline;'>The Committee</span></em></h1>"])
            try:
                session.sendmail('',receivers,message)
                print('Email Sent')
            except:
                print('ERROR Sending Email!!')
            session.quit()    

    def setupUi(self, TaskManagement):
        TaskManagement.setObjectName("TaskManagement")
        TaskManagement.resize(600, 350)
        self.centralwidget = QtWidgets.QWidget(TaskManagement)
        self.centralwidget.setObjectName("centralwidget")
        # self.taskComboBox = QtWidgets.QComboBox(self.centralwidget)
        # self.taskComboBox.setGeometry(QtCore.QRect(90, 10, 111, 24))
        # self.taskComboBox.setObjectName("taskComboBox")
        # self.taskComboBox.addItem("")
        # self.taskComboBox.addItem("")
        # self.taskComboBox.addItem("")
        self.taskEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.taskEdit.setGeometry(QtCore.QRect(135, 10, 181, 31))
        self.taskEdit.setObjectName("taskEdit")

        self.taskLabel = QtWidgets.QLabel(self.centralwidget)
        self.taskLabel.setGeometry(QtCore.QRect(80, 10, 51, 31))
        self.taskLabel.setObjectName("taskLabel")
        self.assignLabel = QtWidgets.QLabel(self.centralwidget)
        self.assignLabel.setGeometry(QtCore.QRect(340, 50, 81, 21))
        self.assignLabel.setObjectName("assignLabel")
        self.assignComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.assignComboBox.setGeometry(QtCore.QRect(440, 50, 101, 24))
        self.assignComboBox.setObjectName("assignComboBox")
        self.assignComboBox.addItem("")
        self.assignComboBox.addItem("")
        self.assignComboBox.addItem("")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(80, 52, 68, 21))
        self.statusLabel.setObjectName("statusLabel")
        self.statusComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.statusComboBox.setGeometry(QtCore.QRect(160, 50, 86, 24))
        self.statusComboBox.setObjectName("statusComboBox")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 90, 381, 192))
        self.tableWidget.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 3, item)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(460, 90, 101, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 83, 24))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(lambda:self.addBtnAction())
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 83, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.updateBtnAction())
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 70, 83, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.deleteBtnAction())
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 83, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda:self.notifyTask() )

        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(340, 10, 51, 31))
        self.TimeLabel.setObjectName("TimeLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(400, 10, 164, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        

        TaskManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        TaskManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TaskManagement)
        self.statusbar.setObjectName("statusbar")
        TaskManagement.setStatusBar(self.statusbar)

        self.retranslateUi(TaskManagement)
        QtCore.QMetaObject.connectSlotsByName(TaskManagement)

    def retranslateUi(self, TaskManagement):
        _translate = QtCore.QCoreApplication.translate
        TaskManagement.setWindowTitle(_translate("TaskManagement", "Task Management"))
        # self.taskComboBox.setItemText(0, _translate("TaskManagement", "Garbage"))
        # self.taskComboBox.setItemText(1, _translate("TaskManagement", "Cleaning"))
        # self.taskComboBox.setItemText(2, _translate("TaskManagement", "other"))
        self.taskLabel.setText(_translate("TaskManagement", "Task"))
        self.assignLabel.setText(_translate("TaskManagement", "AssignedTo"))
        self.assignComboBox.setItemText(0, _translate("TaskManagement", "Harshit"))
        self.assignComboBox.setItemText(1, _translate("TaskManagement", "Pratik"))
        self.assignComboBox.setItemText(2, _translate("TaskManagement", "Sandeep"))
        self.statusLabel.setText(_translate("TaskManagement", "Status"))
        self.statusComboBox.setItemText(0, _translate("TaskManagement", "Pending"))
        self.statusComboBox.setItemText(1, _translate("TaskManagement", "Completed"))

        self.TimeLabel.setText(_translate("TaskManagement", "Time"))
        # item = self.tableWidget.horizontalHeaderItem(0)   
        # item.setText(_translate("TaskManagement", "Id"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TaskManagement", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TaskManagement", "Task"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TaskManagement", "AssignedTo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TaskManagement", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TaskManagement", "Deadline"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.setColumnWidth(3, 65)
        self.tableWidget.setColumnWidth(2, 85)
        self.getTaskList()
        self.tableWidget.itemSelectionChanged.connect(self.rowSelectionEvent)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("TaskManagement", "1"))
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("TaskManagement", "Task1"))
        # item = self.tableWidget.item(0, 2)
        # item.setText(_translate("TaskManagement", "Person1"))
        # item = self.tableWidget.item(0, 3)
        # item.setText(_translate("TaskManagement", "Pending"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addButton.setText(_translate("TaskManagement", "Add Task"))
        self.pushButton_2.setText(_translate("TaskManagement", "Update"))
        self.pushButton_3.setText(_translate("TaskManagement", "Delete"))
        self.pushButton_4.setText(_translate("TaskManagement", "Notify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    TaskManagement = QtWidgets.QMainWindow()
    ui = Ui_TaskManagement()
    ui.setupUi(TaskManagement)
    TaskManagement.show()
    sys.exit(app.exec_())


