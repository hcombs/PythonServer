import os

class Directory:
	
	@staticmethod
	def getPaths(rt):
		print(rt)
		listOfFiles = list()
		for (dirpath, dirnames, filenames) in os.walk(rt):
			listOfFiles += [os.path.join(dirpath,file) for file in filenames]

		return listOfFiles
