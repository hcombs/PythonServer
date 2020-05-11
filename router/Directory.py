import os

class Directory:
	
	@staticmethod
	def getPaths(rt):
		root = "router\public"
		listOfFiles = list()

		for dirpath, subdirs, files in os.walk(root):
			for x in files:
				if x == rt:
					return open(os.path.join(dirpath, x),"r").read().encode()


