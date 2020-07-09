from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
from router.Router import Router

class GetHandler(SimpleHTTPRequestHandler):

        def do_GET(self):
            respObj = Router.parameterize(self.path)
            self.send_response(200)
            self.send_header('Content-type',respObj['Content-type'])
            self.end_headers()
            self.wfile.write(respObj['response'])                

        def do_POST(self):
            respObj = Router.api("/test",{"test":"test"})
            self.send_response(200)    
            self.send_header('Content-type',respObj['Content-type'])
            self.end_headers()
            self.wfile.write(respObj['response'])   

            return




Handler = GetHandler

httpd = HTTPServer(("localhost", 8080), Handler)
httpd.serve_forever()