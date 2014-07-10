from tornado import web

from worldcup.domain.algorithms import *
from worldcup.domain.action import *
from worldcup.domain.position import ProductionInfo


class ExplorationHandler(web.RequestHandler):
    def get(self):
        pass

    def post(self):
        # get parameters from post action
        params = parse_parameters(str(self.request.body))

        field_width = int(params['width'])
        field_height = int(params['height'])

        # update the field based on the last operation result back from game server
        if not field.IsInited():
            field.InitField(field_width,field_height)
        else:
            if params.contains('lastoperation'):
                last_operation = params['lastoperation']
                last_operation_status = params['lastoperationstatus']
                last_operation_value = params['lastoperationvalue']
                field.UpdatePositionStatus(previousAction.x, previousAction.y,last_operation,last_operation_status,last_operation_value)

            productionVolumes = parse_production(params['production'])
            field.UpdateProduction(productionVolumes)

        # call the algorithms (pass in the field)
        newAction =  algorithm.NextAction()
        previousAction.x = newAction.x
        previousAction.y = newAction.y

        # feedback the game server based on the action from the algorithms
        self.write(newAction.to_xml())


def _decode_html(input):
    return input.replace('%2c', ',').replace('+', ' ')

def parse_parameters(request):
    items = request.split('&')
    params = dict()
    for item in items:
        key_and_value = item.split('=')
        params[key_and_value[0]] = _decode_html(key_and_value[1]).strip()
    return params

def parse_production(request):
    list = []
    if request.strip() == '':
        return list

    items = request.split(' ')
    for item in items:
        values = item.split(',')
        list.append(ProductionInfo(int(values[0]),int(values[1]),int(values[2])))
    return list