from .Directory import Directory

class Router:

	@staticmethod
	def parameterize(path):
		response = Router.setResponse(path)
		if len(path.split("?")) > 1:
			return Router.api(path)
		else:
			return Router.page(response)	

	@staticmethod
	def page(response):
		response["response"] = Directory.getPaths(response["path"])
		if not len(response["response"]):
			response["code"] = 404

		return response

	@staticmethod
	def api(path):
		#parse and set methods for GET
		data = b'<html><body><h1>GET!</h1></body></html>'
		return {
			"code":200,
			"Content-type":"text/html",
			"response": data,
			"file":False
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
		
