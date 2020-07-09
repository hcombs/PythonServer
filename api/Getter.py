from db.db import db 

class Getter:	
	@staticmethod
	def exercises(data):
		selector = db()
		return selector.retrieveState("""SELECT o.NAME, e.day, e.dID, e.eID FROM exercises o, groups e where o.exID = e.eID""")


