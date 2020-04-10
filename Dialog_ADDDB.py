# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from SH4R1NG4N import *

class Ui_ADDDB(object):

    def dialogError(errorinfo): # Shows a error dialog.
        error = QtWidgets.QDialog()
        error_dialog = Ui_ErrorDialog()
        error_dialog.setupUi(error, errorinfo)
        error.show()
        error.exec_()

    def setupUi(self, ADDDB, instancia):
        ADDDB.setObjectName("ADDDB")
        ADDDB.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/3-tomoe.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ADDDB.setWindowIcon(icon)
        ADDDB.setStyleSheet("background-color: rgb(10, 10, 10);\n"
                                "selection-background-color: rgb(17, 17, 17);\n"
                                "selection-color: rgb(32, 255, 0);\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(ADDDB)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonADD = QtWidgets.QPushButton(ADDDB)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonADD.setFont(font)
        self.buttonADD.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 17, 17);")
        self.buttonADD.setAutoDefault(False)
        self.buttonADD.setObjectName("buttonADD")
        self.gridLayout_2.addWidget(self.buttonADD, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(ADDDB)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 633, 382))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")

# ================================================================================================================================================
        group_list = []
        self.group_names = []
        label_list = []
        text_list = []
        grid_layout_groups = []
        self.reserva = []
        self.saved_labels = []
        self.saved_texts = []
        self.saved_data = []
        _translate = QtCore.QCoreApplication.translate

        filedb = open('configDB.txt', 'r')
        configDB = filedb.readline().split(';')
        filedb.close()
        try:
                con = mysql.connector.connect(user=configDB[0],password=configDB[1],host=configDB[2],database=configDB[3])
                cursor=con.cursor()
                print("Connected to MySQL")
                print("Launching: "+'SHOW TABLES;')
                cursor.execute('SHOW TABLES;')
                result = cursor.fetchall()

                for row_number, row_data in enumerate(result):
                        for colum_number, data in enumerate(row_data):
                                group_list.append(QtWidgets.QGroupBox(self.scrollAreaWidgetContents))
                                group_list[row_number].setStyleSheet("background-color: rgb(17, 17, 17);\n"
                "selection-background-color: rgb(17, 17, 17);\n"
                "color: rgb(255, 255, 255);\n"
                "selection-color: rgb(32, 255, 0);")
                                group_list[row_number].setObjectName(data)
                                group_list[row_number].setTitle(_translate("ADDDB", str(data)))
                                
                                grid_layout_groups.append(QtWidgets.QGridLayout(group_list[row_number]))
                                grid_layout_groups[row_number].setObjectName("gridLayout_"+str(data))

                                self.horizontalLayout.addWidget(group_list[row_number])
                                print('CREADO GRUPO: '+str(data))
                                self.group_names.append(data)
                counter = 0
                for name in self.group_names:
                        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}';".format(str(name)))
                        result_names = cursor.fetchall()
                        print('Mostrando datos del grupo: '+str(name))

                        for row_number, row_data in enumerate(result_names):
                                for colum_number, data in enumerate(row_data):
                                        
                                        text_list.append(QtWidgets.QTextEdit(group_list[counter]))
                                        text_list[row_number].setMaximumSize(QtCore.QSize(16777215, 20))
                                        text_list[row_number].setMinimumSize(QtCore.QSize(200, 0))
                                        font = QtGui.QFont()
                                        font.setPointSize(8)
                                        text_list[row_number].setFont(font)
                                        text_list[row_number].setStyleSheet("background-color: rgb(10, 10, 10);\n"
                                                "selection-background-color: rgb(17, 17, 17);\n"
                                                "selection-color: rgb(32, 255, 0);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "border-color: rgb(255, 255, 255);")
                                        text_list[row_number].setFrameShape(QtWidgets.QFrame.WinPanel)
                                        text_list[row_number].setFrameShadow(QtWidgets.QFrame.Plain)
                                        text_list[row_number].setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                                        text_list[row_number].setObjectName('text'+str(data))
                                        grid_layout_groups[counter].addWidget(text_list[row_number], row_number, 1, 1, 1)

                                        label_list.append(QtWidgets.QLabel(group_list[counter]))
                                        font = QtGui.QFont()
                                        font.setPointSize(7)
                                        label_list[row_number].setFont(font)
                                        label_list[row_number].setObjectName("label"+str(data))
                                        grid_layout_groups[counter].addWidget(label_list[row_number], row_number, 0, 1, 1)
                                        label_list[row_number].setText(_translate("ADDDB", str(data)))
                                        print('CREADO LABEL/TEXT: '+str(data))
                                        self.saved_data.append(data)
                        self.saved_labels.append(label_list)
                        self.saved_texts.append(text_list)
                        label_list = []
                        text_list = []
                        counter += 1

                cursor.close()
                con.close()
                print('MySQL Connection closed.')
        except Exception as err:
                Ui_ADDDB.dialogError('[!] Error connecting to database: '+str(err))
# ================================================================================================================================================

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.retranslateUi(ADDDB)
        QtCore.QMetaObject.connectSlotsByName(ADDDB)
        self.buttonADD.clicked.connect(lambda: self.connect_main(instancia))
# ================================================================================================================================================

    def connect_main(self, instancia):

        instancia.addEntry(self.saved_labels, self.saved_texts, self.saved_data, self.group_names)

        '''contador = 0
        for group_num, texts in enumerate(self.saved_texts): 
                for texts_num, text in enumerate(texts):
                        print(str(contador),': ',text)
                        text.setText(self.saved_data[contador])
                        command = 'asd'
                        Database.run(instancia, command)
                        contador += 1'''

    def retranslateUi(self, ADDDB):
        _translate = QtCore.QCoreApplication.translate
        ADDDB.setWindowTitle(_translate("ADDDB", "ADD entry to Database"))
        self.buttonADD.setText(_translate("ADDDB", "ADD"))