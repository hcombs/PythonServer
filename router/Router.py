from frontend.Directory import Directory
from api.Getter import Getter
from api.Setter import Setter

class Router:

	@staticmethod
	def parameterize(path):
		if len(path.split("?")) > 1:
			return Router.parseApi(path)
		else:
			return Router.page(path)	

	@staticmethod
	def page(path):
		response = Router.setResponse(path)
		response["response"] = Directory.getPaths(response["path"])
		return response

	@staticmethod
	def parseApi(path):
		params = path.split("?")
		getMethod = params[0].split("api")[1]
		params = params[1].split("&")
		data = {}

		for i in range(len(params)):
			parts = params[i].split("=")
			data[parts[0]] = parts[1]

		return Router.api(getMethod,data)

	@staticmethod	
	def api(method,data):	
		apiMethods = {
			"/exercises":Getter.exercises,
			"/update":Setter.setExercise,
		}
		
		return {
			"code":200,
			"Content-type":"application/json",
			"response":apiMethods[method](data).encode()
		}

	@staticmethod
	def setResponse(path):
		if path == "/":
			path = "index.html"
		else:
			sections = path.split("/")
			path = sections[len(sections) - 1]

		contentType = "text/" + path.split(".")[1]

		return {"code":200,"Content-type":contentType,"response":"","path":path}
