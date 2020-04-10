from SH4R1NG4N_UI import *
from Dialog_ConnectDB import *
from Dialog_Error import *
from Dialog_ADDDB import *
from Dialog_Notes import *
from Dialog_Search import *

from script_amaterasu import *
from script_izanami import *
from script_izanami import *

import threading
import itertools
import mysql.connector
from mysql.connector import Error

class Database():

	lasts_commands = []

	def __init__(self, command):
		global kill_switch
		self.command = command
		filedb = open('configDB.txt', 'r')
		configDB = filedb.readline().split(';')
		filedb.close()
		try:
			self.con = mysql.connector.connect(user=configDB[0],password=configDB[1],host=configDB[2],database=configDB[3])
			self.cursor=self.con.cursor()
			print("Connected to MySQL")
			print("Launching: ",command)
			kill_switch = 1
		except Exception as err:
			kill_switch = 0
			window.dialogError('[!] Error connecting to database: '+str(err))


	def getName(self, command): # Shows the principal information on the interface by the clicked ID (person) in the table.
		return self.run(command)


	def showInfo(self, command, switch, id, window): # Shows all info of selected ID.
		if command == False: # The condition bring the opportunity of make two diferents alternatives.
			table_rec = ['CELLPHONE', 'COMPUTER', 'NOTEBOOK', 'NETWORKS', 'RED'] 
		else:
			self.cursor.execute(command)
			table_rec = self.cursor.fetchall()
		window.tableWidget.setRowCount(0)
		null_values = 0
		for table in table_rec:
			self.cursor.execute("DESC %s;" % table)
			records = self.cursor.fetchall()
			self.cursor.execute("SELECT * FROM %s WHERE "%table + "ID=%s;"%id)
			records2 = self.cursor.fetchall()
			A=0
			for row, row2 in itertools.product(records, records2):
				window.tableWidget.insertRow(A)
				if row2[A] == None: # Count the number of None tipe values, for percentage purposes.
					null_values += 1 
				if switch == 'view':
					window.tableWidget.setItem(A, 0, QtWidgets.QTableWidgetItem(str(row[0])))
					window.tableWidget.setItem(A, 1, QtWidgets.QTableWidgetItem(str(row2[A])))
				A = A + 1

		empty = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
		window.tableWidget.setHorizontalHeaderLabels(empty) # Reset the empty labels.
		return (null_values*100)/205-100

		
	def addData(self, command): # Adds data to Database.
		try:
			self.cursor.execute(command)
			self.con.commit()
		except Exception as err:
			window.dialogError('Error: '+str(err))
	def run(self, command): # Calls the main funciton of the Database.
		if kill_switch == 1: # It's important to maintain the caught of exceptions on the __init__ func.
			try:
				self.cursor.execute(command)
				result = self.cursor.fetchall()
				window.tableWidget.setRowCount(0)
				for row_number, row_data in enumerate(result):
					window.tableWidget.insertRow(row_number)
					for colum_number, data in enumerate(row_data):
						window.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

				empty = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
				window.tableWidget.setHorizontalHeaderLabels(empty) # Reset the empty labels.
				window.tableWidget.setHorizontalHeaderLabels(self.cursor.column_names)
			except Exception as err:
				window.dialogError('Error: '+str(err))
			try:
				return window.tableWidget.item(0,0).text()
			except:
				pass # Error empty information on table.
		else:
			pass


	def __del__(self):
		self.cursor.close()
		self.con.close()
		print('MySQL Connection closed.')


# =====================================================================================================================================================	#

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	index = 0
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.buttonLOAD.clicked.connect(self.dialogDB)
		self.buttonAMATERASU.clicked.connect(self.selectAMATERASU)
		self.buttonIZANAMI.clicked.connect(self.selectIZANAMI)
		self.buttonIZANAGI.clicked.connect(self.selectIZANAGI)
		self.buttonKAMUI.setEnabled(False)
		self.buttonKOTOAMATSUKAMI.setEnabled(False)
		self.buttonSUSANOO.setEnabled(False)
		self.buttonTSUKUYOMI.setEnabled(False)
		self.buttonQuery.clicked.connect(self.sendQuery)
		self.tableWidget.clicked.connect(self.viewData)
		self.buttonLOADSCRIPT.clicked.connect(self.loadScript)
		self.buttonSH1.clicked.connect(self.dialogNotes)
		self.buttonSH2.clicked.connect(self.showCustom)
		self.buttonSH3.clicked.connect(self.showAllTables)
		self.buttonADD.clicked.connect(self.addDB)
		self.buttonREFRESH.clicked.connect(self.refreshThread)
		self.verticalSlider_DATAFRAME.valueChanged.connect(self.slideFrames)
		self.buttonNEXT.clicked.connect(self.search)
		self.selectIZANAMI()
		self.refreshThread()

	def search(self, results, href):
		Searcher = QtWidgets.QDialog()
		Searcher_UI = Ui_SEARCHBOX()
		Searcher_UI.setupUi(Searcher, results, href)
		Searcher.show()
		Searcher.exec_()	

	def refreshThread(self): # Shows the data of the frames on the start if the DB is setted and connected.
		self.buttonREFRESH.setEnabled(False)
		self.threads = []
		try:
			for i in range(1,11):
				exec("hilo_{} = threading.Thread(name='hilo_frames_{}', target=self.refreshFrames, args=[{}])".format(i,i,i)) # Calls refreshFrames.
				exec("hilo_{}.start()".format(i))
				exec("self.threads.append(hilo_{})".format(i))
		except Exception as err:
			print(err)
		finally:
			for thread in self.threads:
				thread.join()
			self.buttonREFRESH.setEnabled(True)



	def refreshFrames(self, val): # Refresh the data cuantity in % showed on the frames.
		command = 'SHOW TABLES;'
		call_db = Database(command)
		percentage = call_db.showInfo(command, 'percentage', val, self)
		if percentage != -100.0:
			aux = percentage/100
			result = 0
			for time in range(100): # Soft refresh, it's only a visual effect to make the app more cute.
				result = result + aux
				sleep(0.008)
				exec('self.progressDB_{}.setValue(abs(result))'.format(val))
		else:
			pass


	def slideFrames(self): # Coordine the slider with the label to show the group of frames.
		size = self.verticalSlider_DATAFRAME.value()
		if size < 92 and size > 0:
			self.labelDATAFRAME.setText(str(size)+' - '+str(size+9))

		
	def addDB(self): # Open a dialog to add manually entrys to the Database.
		self.AddDbDialog = QtWidgets.QDialog()
		self.add_dialog_db = Ui_ADDDB()
		self.add_dialog_db.setupUi(self.AddDbDialog, self)
		self.AddDbDialog.show()
		self.AddDbDialog.exec_()

	def dialogDB(self): # Open the dialog of database configurations
		self.DialogDBLoad = QtWidgets.QDialog()
		self.ui_dialog_db = Ui_Dialog()
		self.ui_dialog_db.setupUi(self.DialogDBLoad, self)
		self.DialogDBLoad.show()
		self.DialogDBLoad.exec_()

	def dialogNotes(self): # Open a dialog with the notes of the selected ID.
		if self.lineFBID.text() != 'None':
			self.DialogNotes = QtWidgets.QDialog()
			self.ui_dialog_notes = Ui_DialogNotes()
			self.ui_dialog_notes.setupUi(self.DialogNotes, self)
			self.DialogNotes.show()
			self.DialogNotes.exec_()
		else:
			self.dialogError('Invalid FBID')

	def dialogError(self, errorinfo): # Shows a error dialog.
		error = QtWidgets.QDialog()
		error_dialog = Ui_ErrorDialog()
		error_dialog.setupUi(error, errorinfo)
		error.show()
		error.exec_()


	def addEntry(self, saved_labels, saved_texts, saved_data, group_names): # Adds manually data to Database.
		contador = 0
		for group_num, texts in enumerate(saved_texts): 
			for texts_num, text in enumerate(texts):
				if contador == 0:
					catch_ID = text.toPlainText()
				print(str(contador),': ',text)
				if saved_data[contador] == 'ID':
					if text.toPlainText() != '':
						command = "INSERT INTO {} ({}) VALUES ({});".format(group_names[group_num], saved_data[contador], text.toPlainText())
						self.call_db = Database(command)
						self.call_db.addData(command)
					else:
						command = "INSERT INTO {} ({}) VALUES ({});".format(group_names[group_num], saved_data[contador], catch_ID)
						self.call_db = Database(command)
						self.call_db.addData(command)

				else:
					if text.toPlainText() != '':
						command = "UPDATE {} SET {} = {} WHERE ID = {};".format(group_names[group_num], saved_data[contador], str(text.toPlainText()), catch_ID)
						self.call_db = Database(command)
						self.call_db.addData(command)
				contador += 1


	def connectDB(self, dialog, one, two, three, four): # Try to connect to DB, after that turns the light on, and call "SHOW TABLES;".
		filedb = open('configDB.txt', 'w')
		filedb.write(one+';'+two+';'+three+';'+four)
		filedb.close()
		filedb = open('configDB.txt', 'r')
		configDB = filedb.readline().split(';')
		filedb.close()
		try:
			mysql.connector.connect(user=configDB[0],password=configDB[1],host=configDB[2],database=configDB[3])
			dialog.buttonHELP.setIcon(dialog.icon2)
			self.refreshThread()
			
		except Exception as err:
			MainWindow.dialogError(MainWindow, str(err))
		finally:
			self.textDB.setPlainText('SHOW TABLES;')
			self.sendQuery('normal')
		

	def sendQuery(self, type_q): # Send querys to the database.
		command = self.textDB.toPlainText()
		self.call_db = Database(command)
		self.call_db.run(command)
		if type_q != 'view':
			Database.lasts_commands.insert(0,command)


	def loadScript(self): # Load the selected script.
		if self.groupBox.title() == 'SELECTED: script_amaterasu.py':
			try:
				hilo0 = threading.Thread(name='hilo_amaterasu',target=amaterasu, args=(self.textScript1.toPlainText(),self.textScript2.toPlainText(),self.textScript3.toPlainText(),self.textScript4.toPlainText()))
				hilo0.start()
			except Exception as err:
				self.dialogError('[!] Soup closed: '+str(err))

		elif self.groupBox.title() == 'SELECTED: script_izanami.py':
			try:
				#hilo1 = threading.Thread(name='hilo_izanami',target=izanami, args=(self.textScript1.toPlainText(),self.textScript2.toPlainText(),self.textScript3.toPlainText(),self.textScript4.toPlainText()+'.html', self))
				#hilo1.start()
				izanami(self.textScript1.toPlainText(),self.textScript2.toPlainText(),self.textScript3.toPlainText(),self.textScript4.toPlainText()+'.html', self)
			except Exception as err:
				self.dialogError('[!] Driver closed: '+str(err))
				print(err)

		elif self.groupBox.title() == 'SELECTED: script_izanagi.py':
			print('izanagi')

		elif self.groupBox.title() == 'SELECTED: script_kamui.py':
			print('kamui')

		elif self.groupBox.title() == 'SELECTED: script_kotoamatsukami.py':
			print('kotoamatsukami')

		elif self.groupBox.title() == 'SELECTED: script_susanoo.py':
			print('susanoo')
		
		elif self.groupBox.title() == 'SELECTED: script_tsukuyomi.py':
			print('tsukuyomi')


	def viewData(self): # Shows in the interface the information of a selected ID (person) when you click on the table.
		row = self.tableWidget.currentRow()
		try:
			getid = self.tableWidget.item(row,0).text()
			self.lcdd.display(int(getid))
			self.lineName.setText(str(Database(('SELECT NAME FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT NAME FROM GENERAL WHERE ID={};'.format(int(getid))))+' '+
								str(Database(('SELECT LASTNAME FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT LASTNAME FROM GENERAL WHERE ID={};'.format(int(getid)))))
			self.lineDNI.setText(str(Database(('SELECT DNI FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT DNI FROM GENERAL WHERE ID={};'.format(int(getid)))))
			self.lineBirthdate.setText(str(Database(('SELECT BORN_DATE FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT BORN_DATE FROM GENERAL WHERE ID={};'.format(int(getid)))))
			self.lineCountry.setText(str(Database(('SELECT NATIONALITY FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT NATIONALITY FROM GENERAL WHERE ID={};'.format(int(getid)))))
			self.lineFBID.setText(str(Database(('SELECT FaceID FROM GENERAL WHERE ID={};'.format(int(getid)))).getName('SELECT FaceID FROM GENERAL WHERE ID={};'.format(int(getid)))))
			
			id_number = window.lcdd.value()
			command = 'SHOW TABLES;'
			call_db = Database(command)
			percent = call_db.showInfo(command, 'view', id_number, self)
			print(abs(percent),' %')
			self.progressBar.setValue(abs(percent))

			command = self.textDB.toPlainText()
			call_db = Database(command)
			call_db.run(command)
		except:
			pass


	def showAllTables(self): # Shows all info of selected ID.
		id_number = window.lcdd.value()
		command = 'SHOW TABLES;'
		call_db = Database(command)
		percentage = call_db.showInfo(command, 'view', id_number, self)
		print(abs(percentage),' %')
		self.progressBar.setValue(abs(percentage))


	def showCustom(self): # Shows all info of selected ID.
		id_number = window.lcdd.value()
		command = False
		call_db = Database(command)
		call_db.showInfo(command, 'view', id_number, self)


	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Q and event.modifiers() & Qt.ControlModifier:
			self.viewBack()

		elif event.key() == Qt.Key_W and event.modifiers() & Qt.ControlModifier:
			self.viewNext()


	def viewBack(self): # Load the previous command. (CTRL+Q)
		print('Left pressed')
		if len(Database.lasts_commands) >= 2 and MainWindow.index < len(Database.lasts_commands)-1:
			MainWindow.index += 1
			print(str(MainWindow.index))	
			self.textDB.setPlainText(Database.lasts_commands[MainWindow.index])
			self.sendQuery('view')


	def viewNext(self): # Load the previous command. (CTRL+W)
		print('Right pressed')
		if len(Database.lasts_commands) >= 2 and MainWindow.index > 0:
			MainWindow.index -= 1
			print(str(MainWindow.index))
			self.textDB.setPlainText(Database.lasts_commands[MainWindow.index])
			self.sendQuery('view')

	def selectAMATERASU(self): # Shows the available settings and prepare the scripts when you click on the Icons.
		self.labelConfig1.setText('URL')
		self.labelConfig2.setText('Find')
		self.labelConfig3.setText('Save')
		self.labelConfig4.setText('Route')
		self.groupBox.setTitle('SELECTED: script_amaterasu.py')
		self.buttonLOADSCRIPT.setEnabled(True)
	def selectIZANAMI(self):
		self.labelConfig1.setText('FB Username')
		self.labelConfig2.setText('FB Password')
		# self.textScript2.setEchoMode(QtGui.QLineEdit.Password) NECESITA SER QlineEdit
		self.labelConfig3.setText('FB Target ID')
		self.labelConfig4.setText('Output file')
		self.groupBox.setTitle('SELECTED: script_izanami.py')
		self.buttonLOADSCRIPT.setEnabled(True)
	def selectIZANAGI(self):
		self.labelConfig1.setText('FB ID')
		self.labelConfig2.setText('Data Proccesing(V/F)')
		self.labelConfig3.setText('Who React(V/F)')
		self.labelConfig4.setText('IMG Downloading(V/F)')
		self.groupBox.setTitle('SELECTED: script_izanagi.py')
		self.buttonLOADSCRIPT.setEnabled(True)
	def selectKAMUI(self):
		self.labelConfig1.setText('EMAIL')
		self.labelConfig2.setText('KB to KILL')
		self.labelConfig3.setText('Capture Webcam (V/F)')
		self.labelConfig4.setText('Screenshot (V/F)')
		self.groupBox.setTitle('SELECTED: script_kamui.py')
		self.buttonLOADSCRIPT.setEnabled(False)
	def selectKOTOAMATSUKAMI(self):
		self.labelConfig1.setText('File to Venom')
		self.labelConfig2.setText('False files (V/F)')
		self.labelConfig3.setText('Encoders (0,1)')
		self.labelConfig4.setText('To Rar (V/F)')
		self.groupBox.setTitle('SELECTED: script_kotoamatsukami.py')
		self.buttonLOADSCRIPT.setEnabled(False)
	def selectSUSANOO(self):
		self.labelConfig1.setText('IP Target')
		self.labelConfig2.setText('IP Gateway')
		self.labelConfig3.setText('Interface')
		self.labelConfig4.setText('IP/Port Proxy')
		self.groupBox.setTitle('SELECTED: script_susanoo.py')
		self.buttonLOADSCRIPT.setEnabled(False)
	def selectTSUKUYOMI(self):
		self.labelConfig1.setText('USER/PASS')
		self.labelConfig2.setText('FB MAIN ID')
		self.labelConfig3.setText('Tree Analisis(1,2,3)')
		self.labelConfig4.setText('Sleep Time (00:00)')
		self.groupBox.setTitle('SELECTED: script_tsukuyomi.py')
		self.buttonLOADSCRIPT.setEnabled(False)

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()