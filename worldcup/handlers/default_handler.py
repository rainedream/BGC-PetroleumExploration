from tornado import web
from worldcup.domain.field import *
from worldcup.domain.algorithms import *
from worldcup.domain.states.owned import *
from worldcup.domain.position import *


class DefaultHandler(web.RequestHandler):

    def get(self):

        # get parameters from post action
        newStatus = Owned
        productionVolumes = { ProductionInfo(20,20,300) }

        # update the field based on the last operation result back from game server
        if  field.IsInited() == False:
            field.InitField(100,100)
        else:
            field.UpdatePositionStatus(100,100,"new status" )
            field.UpdateProduction(productionVolumes)

        # call the algorithms (pass in the field)
        nextAction =  algorithm.NextAction()

        # feedback the game server based on the action from the algorithms




































































































































































