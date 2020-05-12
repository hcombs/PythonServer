from .Directory import Directory
from .Getter import Getter


class Router:

	@staticmethod
	def parameterize(path):
		if len(path.split("?")) > 1:
			return Router.parseApi(path)
		else:
			response = Router.setResponse(path)
			return Router.page(response)	

	@staticmethod
	def page(response):
		response["response"] = Directory.getPaths(response["path"])
		if not len(response["response"]):
			response["code"] = 404

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

	
	def api(method,data):	
		print(method)
		getMethods = {
			"/exercises":Getter.exercises
		}
		
		return {
			"code":200,
			"Content-type":"application/json",
			"response":getMethods[method](data).encode()
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
		
