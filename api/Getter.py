from db.db import db 

class Getter:
	
	@staticmethod
	def exercises(data):
		selector = db()
		return selector.retrieveState(data["values"])


