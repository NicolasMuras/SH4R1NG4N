from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SH4R1NG4N import *
class Window(QWidget):
    def __init__(self, val):
        super().__init__()
        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout =QFormLayout()
        groupBox = QGroupBox("This Is Group Box")
        labelLis = []
        comboList = []

        for i in  range(val):
            labelLis.append(QLabel("Label"))
            comboList.append(QPushButton("Click Me"))
            formLayout.addRow(labelLis[i], comboList[i])
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()

# ================================================================================================================================================
        group_list = []
        label_list = []
        text_list = []
        _translate = QtCore.QCoreApplication.translate

        #filedb = open('configDB.txt', 'r')
        #configDB = filedb.readline().split(';')
        #filedb.close()
        try:
        	self.con = mysql.connector.connect(user='root',password='123456789',host='127.0.0.1',database='SH4R1NG4N')
	        self.cursor=self.con.cursor()
	        print("Connected to MySQL")
	        print("Launching: "+'SHOW TABLES;')
        except Exception as err:
        	window.dialogError('[!] Error connecting to database: '+str(err))

        self.cursor.execute('SHOW TABLES;')
        result = self.cursor.fetchall()

        for row_number, row_data in enumerate(result):
                group_list.append(QtWidgets.QGroupBox(self.scrollAreaWidgetContents))
                group_list[row_number].setTitle(_translate("ADDDB", row_data))
                group_list[row_number].setStyleSheet("background-color: rgb(17, 17, 17);\n"
"selection-background-color: rgb(17, 17, 17);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(32, 255, 0);")
                group_list[row_number].setObjectName(row_data)

                for colum_number, data in enumerate(row_data):
                	window.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                        
        self.cursor.close()
        self.con.close()
        print('MySQL Connection closed.')
# ================================================================================================================================================

App = QApplication(sys.argv)
window = Window(30)
sys.exit(App.exec())