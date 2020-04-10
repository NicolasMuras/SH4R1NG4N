# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Notes.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SH4R1NG4N import *
import os
import sys

class Ui_DialogNotes(object):
    def setupUi(self, DialogNotes, instancia):
        DialogNotes.setObjectName("DialogNotes")
        DialogNotes.resize(372, 378)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        DialogNotes.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/3-tomoe.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogNotes.setWindowIcon(icon)
        self.buttonSAVE = QtWidgets.QPushButton(DialogNotes)
        self.buttonSAVE.setGeometry(QtCore.QRect(10, 340, 91, 31))
        self.buttonSAVE.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 17, 17);")
        self.buttonSAVE.setAutoDefault(False)
        self.buttonSAVE.setObjectName("buttonSAVE")
        self.textNOTE = QtWidgets.QTextEdit(DialogNotes)
        self.textNOTE.setGeometry(QtCore.QRect(10, 10, 351, 321))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textNOTE.setFont(font)
        self.textNOTE.setStyleSheet("background-color: rgb(10, 10, 10);\n"
"selection-background-color: rgb(17, 17, 17);\n"
"selection-color: rgb(32, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.textNOTE.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textNOTE.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textNOTE.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textNOTE.setObjectName("textNOTE")

        self.retranslateUi(DialogNotes)
        QtCore.QMetaObject.connectSlotsByName(DialogNotes)
# ============================================================== SISTEMA DE NOTAS =====================================================
        self.buttonSAVE.clicked.connect(self.connection)
        self.id_number = instancia.lineFBID.text()
        self.instancia = instancia
        if os.path.isdir(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/') == False:
            os.mkdir(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/')
        if os.path.isfile(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/'+str(self.id_number)+'_note.txt') == False:
            pass
        else:
            file_n = open(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/'+str(self.id_number)+'_note.txt', 'r')
            result = file_n.read()
            self.textNOTE.setText(str(result))
            file_n.close()

    def connection(self):
        try:
            if os.path.isdir(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/') == False:
                os.mkdir(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/')
            file_n = open(str(os.getcwd())+'/IDs/'+str(self.id_number)+'/'+str(self.id_number)+'_note.txt', 'w+')
            file_n.write(self.textNOTE.toPlainText())
            file_n.close()
        except:
             self.instancia.dialogError('Error at save !')

        
    def retranslateUi(self, DialogNotes):
        _translate = QtCore.QCoreApplication.translate
        DialogNotes.setWindowTitle(_translate("DialogNotes", "NOTE"))
        self.buttonSAVE.setText(_translate("DialogNotes", "SAVE"))
