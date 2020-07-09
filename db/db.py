import json
import sqlite3

class db:

	def __init__(self):
		self.file = "db\system.db"

	def __open(self):
		self.con = sqlite3.connect(self.file)
		self.con.row_factory = db.dict_factory	

	def __close(self):
		self.con.close()	

	def __statement(self,sql):
		c = self.con.cursor()	
		c.execute(sql)
		return c

	def updateState(self,sql):
		db.__open(self)
		db.__statement(self,sql)
		self.con.commit()
		db.__close(self)	

	def retrieveState(self,sql):
		db.__open(self)
		rows = db.__statement(self,sql)
		result = rows.fetchall()
		db.__close(self)
		return json.dumps(result)

	def dict_factory(cursor,rows):
		d ={}
		for idx,col in enumerate(cursor.description):
			d[col[0]] = rows[idx]
		return d

#sql = """SELECT o.NAME, e.day, e.dID, e.eID FROM exercises o, groups e where o.exID = e.eID and day = 4"""



    
    