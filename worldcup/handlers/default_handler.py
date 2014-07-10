from tornado import web
from worldcup.domain.field import *
from worldcup.domain.algorithms import *
from worldcup.domain.states.owned import *
from worldcup.domain.position import *
from worldcup.domain.action import *


class DefaultHandler(web.RequestHandler):

    def get(self):
        pass

    def post(self):
        # get parameters from post action
        params = parse_parameters(self.request.body)

        field_width = params['width']
        field_height = params['height']
        last_operation =params['lastoperation']
        last_operation_status =params['lastoperationstatus']
        last_operation_value =params['lastoperationvalue']
        productionVolumes = parse_production(params['Production'])

        # update the field based on the last operation result back from game server
        if  field.IsInited() == False:
            field.InitField(field_width,field_height)
        else:
            field.UpdatePositionStatus(previousAction.x, previousAction.y,last_operation,last_operation_status,last_operation_value)
            field.UpdateProduction(productionVolumes)

        # call the algorithms (pass in the field)
        newAction =  algorithm.NextAction()
        previousAction.x = newAction.x
        previousAction.y = newAction.y

        # feedback the game server based on the action from the algorithms
        self.write(newAction.to_xml())


def parse_parameters(request):
    items = request.split('&')
    params = dict()
    for item in items:
        key_and_value = item.split('=')
        params[key_and_value[0]] = key_and_value[1]
    return params

def parse_production(request):
    items = request.split(' ')

    for item in items:
        values = item.split(',')
        list.append(ProductionInfo(int(values[0]),int(values[1]),int(values[2])))




































































































































































