from tornado import web
from worldcup.domain.action import *


class ExplorationHandler(web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/xml")
        action = Action(ActionType.BUY, 1, 2)   # It will be replaced by REAL ACTION
        self.write(action.to_xml())