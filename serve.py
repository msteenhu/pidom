import socket
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
   self.send_response(200) or self.end_headers() or self.wfile.write('WakqA7R4LUP88YeIBgckyi3CY2utgDlpcaKpJ67ODLQ.GZEYHZ_SknA8OdDikIyHOy0kqkz7YHJ7U4Zbw77w8kU');

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

def main():
  server = HTTPServerV6(('::', 80), MyHandler)
  server.serve_forever()

if __name__ == '__main__':
  main()
