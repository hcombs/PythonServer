import sqlite3
from sqlite3 import Error

class db(object):
	def __init__(self):
		super(db, self).__init__()
		self.file = "system.db"

	def updateState(self,obj):
		con = db.__open(self.file)
		cursor = con.cursor()
		statement = self.__insertColumns
		cursor.execute(statement)
		con.commit()
		db.__close(con)

	def retrieveState(self,obj):
		con = db.__open(self.file)
		cursor = con.cursor()
		statement = self.__selectColumns
		cursor.execute(statement)
		rows = cursor.fetchall()
		db.__close(con)		
		return rows	
		
	def __insertColumns(obj):
		insertStmt = "INSERT INTO Progress (name, reps, timeVal, set, weight, date, time) VALUES"
		insertStmt += ",".join(obj)
		insertStmt += ")"
		return insertStmt

	def __selectColumns(obj):
		selectStmt = "SELECT * FROM Progress WHERE date >= "
		selectStmt += obj
		return selectStmt

	def __open(self):
		return sqlite3.connect(db.file)

	def __close(con):
		con.close()

		