from tornado import web


class GSTHandler(web.RequestHandler):
    def get(self):
        pass

    def post(self):
        # get parameters from post action
        params = parse_parameters(str(self.request.body))

        field_width = int(params['width'])
        field_height = int(params['height'])
        # newAction =  algorithm.NextAction()
        # previousAction.x = newAction.x
        # previousAction.y = newAction.y

        # feedback the game server based on the action from the algorithms
        # self.write(newAction.to_xml())


def _decode_html(input):
    return input.replace('%2c', ',').replace('+', ' ')


def parse_parameters(request):
    items = request.split('&')
    params = dict()
    for item in items:
        key_and_value = item.split('=')
        params[key_and_value[0]] = _decode_html(key_and_value[1]).strip()
    return params
