from worldcup.domain.field import *
from worldcup.domain.action import *

class Algorithm :
    def __init__(self ):
        pass

    def NextAction(self):
        pass

class SimpleAlogrithm(Algorithm) :

    def NextAction(self):
        #if there is an any produced well, not get profit any more
        # shutdown
        positions = field.GetUnProfitPositions()

        if ( positions.Count > 0):
            return Action(ActionType.STOP, positions[0].x, positions[0].y)

        # if there is any explored well
        # drill
        positions = field.GetExploredPositions()

        if ( positions.Count > 0):
            return Action(ActionType.DRILL, positions[0].x, positions[0].y)

        # if there is any purchased well
        # explore
        positions = field.GetPurchaedPositions()

        if ( positions.Count > 0):
            return Action(ActionType.EXPLORE, positions[0].x, positions[0].y)

        # if there is any available well
        # purchase
        positions = field.GetAvailablePositions()

        if ( positions.Count > 0):
            return Action(ActionType.BUY, positions[0].x, positions[0].y)
        pass



algorithm = Algorithm()