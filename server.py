from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
#from getController import GetRouter
from router.Router import Router

class GetHandler(SimpleHTTPRequestHandler):

        def do_GET(self):
            respObj = Router.parameterize(self.path)

            if not respObj["file"]:
                self.send_response(200)
                self.send_header('Content-type',respObj['Content-type'])
                self.end_headers()
                self.wfile.write(respObj['response'])                
            else:    
                SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))

            data = b'<html><body><h1>POST!</h1></body></html>'
            self.wfile.write(bytes(data))
            return




Handler = GetHandler

httpd = HTTPServer(("localhost", 8080), Handler)
httpd.serve_forever()