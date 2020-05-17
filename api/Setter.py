from db.db import db 

class Setter(object):
	@staticmethod
	def setExercise(data):
		inserter = db()
		return inserter.updateState(data["values"])

		