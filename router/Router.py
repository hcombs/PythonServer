from .Directory import Directory

class Router:

	@staticmethod
	def parameterize(path):
		return Router.setResponse(path)

	@staticmethod
	def routes(key):
		route = {
			"/":Router.page
		}
		return route[key]()

	@staticmethod
	def page(response):
		response["code"] = 200
		#need to set types
		response["Content-type"] = "text/html"
		x = Directory.getPaths("router\public")

		a = open(x[0],"r")
		f = a.read()

		response["response"] = f.encode()
		
		return response

	@staticmethod
	def api():
		data = b'<html><body><h1>GET!</h1></body></html>'
		return {
			"code":200,
			"Content-type":"text/html",
			"response": data,
			"file":False
		}

	@staticmethod
	def setResponse(path):
		response = {"code":"","Content-type":"","response":""}
		return Router.page(response)
