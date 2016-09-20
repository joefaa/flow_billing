from wsgiref.simple_server import make_server
from billing_app import application

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
