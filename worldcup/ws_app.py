from tornado import web
from worldcup.handlers.default_handler import DefaultHandler
from worldcup.handlers.exploration_handler import ExplorationHandler


class WebServiceApplication(web.Application):
    def __init__(self):
        handlers = [
            (r'/', DefaultHandler),
            (r'/run', ExplorationHandler)
        ]

        settings = {
            'template_path': 'resource'
        }
        web.Application.__init__(self, handlers, **settings)