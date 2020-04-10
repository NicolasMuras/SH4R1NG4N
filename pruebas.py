# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pruebas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label3 = QtWidgets.QLabel(self.groupBox)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.lineText1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineText1.setMinimumSize(QtCore.QSize(200, 0))
        self.lineText1.setObjectName("lineText1")
        self.gridLayout.addWidget(self.lineText1, 0, 2, 1, 1)
        self.lineText3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineText3.setObjectName("lineText3")
        self.gridLayout.addWidget(self.lineText3, 2, 2, 1, 1)
        self.label2 = QtWidgets.QLabel(self.groupBox)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        self.lineText2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineText2.setObjectName("lineText2")
        self.gridLayout.addWidget(self.lineText2, 1, 2, 1, 1)
        self.label4 = QtWidgets.QLabel(self.groupBox)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 3, 0, 1, 1)
        self.lineText4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineText4.setObjectName("lineText4")
        self.gridLayout.addWidget(self.lineText4, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.label3.setText(_translate("Dialog", "TextLabel"))
        self.label1.setText(_translate("Dialog", "TextLabel"))
        self.label2.setText(_translate("Dialog", "TextLabel"))
        self.label4.setText(_translate("Dialog", "TextLabel"))
