from tornado import web


class ExplorationHandler(web.RequestHandler):
    def post(self):
        self.write("Got POST request")