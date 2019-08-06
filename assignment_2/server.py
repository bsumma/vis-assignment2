
import http.server
import socketserver

class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/shutdown":
            self.send_error(202,"Shutting down...")
            serv.shutdown()
        else:
            super(GetHandler,self).do_GET()
            return

class ThreadHTTPServer(socketserver.ThreadingMixIn,http.server.HTTPServer):
    pass

port = input("Please select a port (default: 8080):")
if len(port):
    port = int(port)
else:
    port = 8080

    
serv = ThreadHTTPServer(("localhost",port),GetHandler,True)
print("When finished with this server, go "+
      "to localhost:"+str(port)+"/shutdown to stop server")
serv.serve_forever()
