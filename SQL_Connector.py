import mysql.connector
import itertools
import os
import re
from mysql.connector import Error

try:
	con = mysql.connector.connect(
		user="root",
		password="543582",
		host="127.0.0.1",
		database="SH4R1NG4N")

	cursor=con.cursor()

	def mangekyo(self): # Muestra toda la informacion del objetivo.
		COMMAND=self
		cursor.execute("SHOW TABLES;")
		table_rec = cursor.fetchall()

		for table in table_rec:
			cursor.execute("DESC %s;" % table)
			records = cursor.fetchall()
			cursor.execute("SELECT * FROM %s WHERE "%table + "ID=%s;"%COMMAND)
			records2 = cursor.fetchall()
			f = open ('archivo2.txt', "a+")
			print("\n----------------- %s -----------------"%table)
			A=0
			for row, row2 in itertools.product(records, records2):
				print(row[0] + " = ", row2[A])
				if row2[A] and row2[A] != 1:
					f.write('%s \n' % row2[A])
				A = A + 1
			f.close()

	def izanagi(target):
		try:
			target_dir = str(os.getcwd())+"/"+target
			dir_name, subdir_list, file_list = os.walk(target_dir)

			def extract_info(file_name):
				if "info" in str(file_name): 
					f = open (file_name, "r")
					date_pattern = r"^[1-31](\s)(de)(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)(de)(\n)[1900-2019]$"
					date_match = re.match(date_pattern,f)
					print("Date pattern found: "+date_match)

			for file in file_list:
				extract_info(file) 

		except Exception as err:
			print(err)

	CMD = input("COMMAND > ")
	if CMD[:8] == "mangekyo":
		mangekyo(CMD[9:])

except Error as e:
	print("Error reading data from MySQL table", e)
finally:
	if (con.is_connected()):
		con.close()
		cursor.close()
		print("MySQL connection is closed")

