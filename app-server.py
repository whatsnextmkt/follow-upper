import SimpleHTTPServer as Http
import SocketServer as Socket
import os
import ssl

from config import APP_NAME, INIT_DIR

_port = 8080
_http_cert_file = 'cert/server1.example.com.key'
_http_cert_pem = 'cert/server1.example.com.pem'

class Handler(Http.SimpleHTTPRequestHandler):
    def do_POST(self):
        post_body = self.rfile.read(20)
        self.wfile.write("Received payload")

httpd = Socket.TCPServer(("", _port), Handler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, keyfile=_http_cert_file, certfile=_http_cert_pem)

print('Run server', _port)
httpd.serve_forever()
