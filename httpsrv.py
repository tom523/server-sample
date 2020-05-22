import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

Server = sys.argv[1]
IP = sys.argv[2]


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Server " + Server + ", IP " + IP, "utf-8"))
        return

try:
    server = HTTPServer(('', 80), myHandler)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
