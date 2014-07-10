from tornado import web
from worldcup.handlers.default_handler import DefaultHandler


class WebServiceApplication(web.Application):
    def __init__(self):
        handlers = [
            (r'/', DefaultHandler),
        ]

        settings = {
            'template_path': 'resource'
        }
        web.Application.__init__(self, handlers, **settings)