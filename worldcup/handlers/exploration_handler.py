from tornado import web
from worldcup.domain.action import *


class ExplorationHandler(web.RequestHandler):
    def get(self):
        pass

    def post(self):
        # round=193&money=980000&width=96&height=96&index=0&production=1%2c2%2c0+&do=execute&lastoperation=Buy&lastoperationstatus=False&lastoperationvalue=
        params = parse_parameters(self.request.body)

        # TODO: use params

        self.set_header("Content-Type", "application/xml")
        action = Action(ActionType.BUY, 1, 2)   # It will be replaced by REAL ACTION
        self.write(action.to_xml())


def parse_parameters(request):
    items = request.split('&')
    params = dict()
    for item in items:
        key_and_value = item.split('=')
        params[key_and_value[0]] = key_and_value[1]
    return params

