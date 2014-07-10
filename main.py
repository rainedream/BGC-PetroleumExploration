from tornado import httpserver, ioloop
from worldcup.ws_app import WebServiceApplication


if __name__ == '__main__':
    ws_app = WebServiceApplication()
    server = httpserver.HTTPServer(ws_app)
    server.listen(8000)
    ioloop.IOLoop.instance().start()
