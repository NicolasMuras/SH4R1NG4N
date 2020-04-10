# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SEARCHBOX(object):
    def setupUi(self, SEARCHBOX, results, profiles):
        SEARCHBOX.setObjectName("SEARCHBOX")
        SEARCHBOX.resize(583, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/backup/Images/3-tomoe.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SEARCHBOX.setWindowIcon(icon)
        SEARCHBOX.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(SEARCHBOX)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(SEARCHBOX)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 563, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupRESULTS = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupRESULTS.setAutoFillBackground(False)
        self.groupRESULTS.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"selection-background-color: rgb(17, 17, 17);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(32, 255, 0);")
        self.groupRESULTS.setFlat(False)
        self.groupRESULTS.setCheckable(False)
        self.groupRESULTS.setObjectName("groupRESULTS")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupRESULTS)
        self.gridLayout_5.setObjectName("gridLayout_5")


        _translate = QtCore.QCoreApplication.translate
        frame = []
        label = []
        #result = result.replace('\nAgregar', '')
        #result = result.replace('\nMás opciones', '')
        counter = 0
        for i, profile in enumerate(profiles):
            label = QtWidgets.QLabel(self.groupRESULTS)
            label.setMaximumSize(QtCore.QSize(16777215, 120))
            font = QtGui.QFont()
            font.setPointSize(8)
            label.setFont(font)
            label.setObjectName("label"+str(i))
            label.setText(_translate("SEARCHBOX", str(profile)+'\n'+str(results[counter])))
            self.gridLayout_5.addWidget(label, i, 1, 1, 1)

            frame = QtWidgets.QLabel(self.groupRESULTS)
            frame.setMaximumSize(QtCore.QSize(120, 120))
            frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            frame.setText("")
            frame.setPixmap(QtGui.QPixmap("Searcher/perfil_{}.jpg".format(i)))
            frame.setScaledContents(True)
            frame.setObjectName("frame"+str(i))
            self.gridLayout_5.addWidget(frame, i, 0, 1, 1)
            counter += 1


        self.horizontalLayout.addWidget(self.groupRESULTS)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.lineLINK = QtWidgets.QLineEdit(SEARCHBOX)
        self.lineLINK.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 87, 83);")
        self.lineLINK.setFrame(False)
        self.lineLINK.setObjectName("lineLINK")
        self.verticalLayout.addWidget(self.lineLINK)
        self.buttonSELECT = QtWidgets.QPushButton(SEARCHBOX)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonSELECT.setFont(font)
        self.buttonSELECT.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 17, 17);")
        self.buttonSELECT.setAutoDefault(False)
        self.buttonSELECT.setObjectName("buttonSELECT")
        self.verticalLayout.addWidget(self.buttonSELECT)

        self.retranslateUi(SEARCHBOX)
        QtCore.QMetaObject.connectSlotsByName(SEARCHBOX)

        self.buttonSELECT.clicked.connect(self.selectUrl)
        self.switch = True
    def selectUrl(self):
        save_link = open('link.txt', 'w+')
        save_link.write('https://www.facebook.com/'+self.lineLINK.text())
        save_link.close()

    def retranslateUi(self, SEARCHBOX):
        _translate = QtCore.QCoreApplication.translate
        SEARCHBOX.setWindowTitle(_translate("SEARCHBOX", "ADD entry to Database"))
        self.groupRESULTS.setToolTip(_translate("SEARCHBOX", "Script configurations."))
        self.groupRESULTS.setTitle(_translate("SEARCHBOX", "SELECT THE PROFILE TO ANALYZE:"))
        self.buttonSELECT.setText(_translate("SEARCHBOX", "SELECT"))
