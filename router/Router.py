class Router:

	@staticmethod
	def parameterize(path):
		return Router.routes(path)

	@staticmethod
	def routes(key):
		route = {
			"/exercise.html":Router.page
		}
		return route[key]()

	@staticmethod
	def page():
		return {
			"code":200,
			"Content-type":"text/html",
			"file":True
		}

	@staticmethod
	def api():
		data = b'<html><body><h1>GET!</h1></body></html>'
		return {
			"code":200,
			"Content-type":"text/html",
			"response": data,
			"file":False
		}
