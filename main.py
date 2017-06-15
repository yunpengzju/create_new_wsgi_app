import os
import sys

from paste.deploy import loadapp


def wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hi! I\'m Yunpeng Chen']


def app():
    application = loadapp('config:paste.ini')
    return application

#application = app()

if __name__ == "__main__":
    import wsgiref.simple_server as wss

    port = 18877
    server = wss.make_server('127.0.0.1', port, wsgi_app)

    print("*" * 80)
    print("STARTING test server")
    print("DANGER! For testing only, do not use in production")
    print("*" * 80)

    server.serve_forever()