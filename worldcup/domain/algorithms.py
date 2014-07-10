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

        if len(positions) > 0:
            return Action(ActionType.STOP, positions[0].x, positions[0].y)

        # if there is any explored well
        # drill
        positions = field.GetValuableExploredPositions()

        if len(positions) > 0:
            return Action(ActionType.DRILL, positions[0].x, positions[0].y)

        # if there is any purchased well
        # explore
        positions = field.GetPurchaedPositions()

        if len(positions) > 0:
            return Action(ActionType.EXPLORE, positions[0].x, positions[0].y)

        # if there is any available well
        # purchase
        positions = field.GetAvailablePositions()

        if len(positions) > 0:
            return Action(ActionType.BUY, positions[0].x, positions[0].y)


class ComplexAlogrithm(Algorithm) :

    def NextAction(self):

        # 1. check if any position should be stop
        # 1.1 get all produced positions
        positions = field.GetUnProfitPositionsProActive()
        if len(positions) > 0:
            return Action(ActionType.STOP, positions[0].x, positions[0].y)

        # 2. check if there is an explored position and decide whether to drill it or not
        #positions = field.GetComplexValuableExploredPositions()
        positions = field.GetExploredPositions()

        if len(positions) > 0:
            return Action(ActionType.DRILL, positions[0].x, positions[0].y)

        # 3. check if there is an purchased position and explore it
        positions = field.GetPurchaedPositions()

        if len(positions) > 0:
            return Action(ActionType.EXPLORE, positions[0].x, positions[0].y)

        # 4. decide a new buy position and buy it
        if  len(to_buy_positions) == 0 :
            GenerateBuyPosition()

        if  len(to_buy_positions) > 0 :
            buy_position = to_buy_positions.pop(0)
            return Action(ActionType.BUY, buy_position.x, buy_position.y)


        pass

def GenerateBuyPosition():

    numberOfPosition = NODE_INITIAL_MONEY * 0.05 / RESERVOIR_BLOCKPRICE

    rationWidthToHeight = field.width / field.height
    numberInY = int((numberOfPosition / rationWidthToHeight) ** (1/2))
    numberInX = int((numberInY * rationWidthToHeight))
    stepInX = int(field.width / (numberInX + 1))
    stepInY = int(field.height / (numberInY + 1))

    global to_buy_positions_generation
    a = to_buy_positions_generation
    to_buy_positions_generation = a +1

    for i in range(0,numberInX):
        for j in range (0, numberInY):
            to_buy_position = Action(ActionType.BUY,(i+1) * stepInX, (j+1) * stepInY)

            sign = (-1)** (to_buy_positions_generation)

            if  field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                to_buy_position = Action(ActionType.BUY,((i+1) * stepInX + 1  + 4 *sign* (to_buy_positions_generation-1))%field.width, ((j+1) * stepInY + 1  + 5 * sign* (to_buy_positions_generation-1))%field.height)

            if not field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                to_buy_positions.append(to_buy_position)


    pass

algorithm = ComplexAlogrithm()
to_buy_positions = []
to_buy_positions_generation = 0