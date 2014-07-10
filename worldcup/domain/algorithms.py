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

        # 1.5 check if need stimulate
        positions = field.GetSuperPositions()
        if len(positions) > 0:
            return Action(ActionType.STIMULATE, positions[0].x, positions[0].y)

        # 1.7 any position can be drill without exploration
        position = field.GetDrillPositionWithoutExplore()
        if not (position == None):
            return Action(ActionType.DRILL, position.x, position.y)

        # 2. check if there is an explored position and decide whether to drill it or not
        #positions = field.GetComplexValuableExploredPositions()
        positions = field.GetMoreComplexValuableExploredPositions()

        if len(positions) > 0:
            produced_positions.append(positions[0])
            return Action(ActionType.DRILL, positions[0].x, positions[0].y)

        # 3. check if there is an purchased position and explore it
        positions = field.GetPurchaedPositions()

        if len(positions) > 0:
            return Action(ActionType.EXPLORE, positions[0].x, positions[0].y)

        # 4. decide a new buy position and buy it
        if  len(to_buy_positions) == 0 :
            GenerateBuyPositionBasedOnProductionPosition()

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
    to_buy_positions_generation = to_buy_positions_generation +1

    for i in range(0,numberInX):
        for j in range (0, numberInY):
            to_buy_position = Action(ActionType.BUY,(i+1) * stepInX, (j+1) * stepInY)

            sign = (-1)** (to_buy_positions_generation)

            if  field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                to_buy_position = Action(ActionType.BUY,((i+1) * stepInX + 1  + 4 *sign* (to_buy_positions_generation-1))%field.width, ((j+1) * stepInY + 1  + 5 * sign* (to_buy_positions_generation-1))%field.height)

            if not field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                to_buy_positions.append(to_buy_position)


    pass

def GenerateBuyPositionBasedOnProductionPosition():

    if len(produced_positions) == 0 :
        numberOfPosition = NODE_INITIAL_MONEY * 0.05 / RESERVOIR_BLOCKPRICE

        rationWidthToHeight = field.width / field.height
        numberInY = int((numberOfPosition / rationWidthToHeight) ** (1/2)) + 1
        numberInX = int((numberInY * rationWidthToHeight)) + 1
        stepInX = int(field.width / (numberInX + 1))
        stepInY = int(field.height / (numberInY + 1))

        while stepInX < 6 or stepInY < 6:
            numberInY -= 1
            numberInX -= 1
            stepInX = int(field.width / (numberInX + 1))
            stepInY = int(field.height / (numberInY + 1))


        while (stepInX > 60 or stepInY > 60) and (numberInY * numberInX) < 46:
            numberInY += 1
            numberInX += 1
            stepInX = int(field.width / (numberInX + 1))
            stepInY = int(field.height / (numberInY + 1))

        global to_buy_positions_generation
        to_buy_positions_generation = to_buy_positions_generation +1

        for i in range(0,numberInX):
            for j in range (0, numberInY):
                to_buy_position = Action(ActionType.BUY,(i+1) * stepInX, (j+1) * stepInY)

                if  field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                    to_buy_position = Action(ActionType.BUY,((i+1) * stepInX + 1  + 4 * (to_buy_positions_generation-1))%field.width, ((j+1) * stepInY + 1  + 5 * (to_buy_positions_generation-1))%field.height)

                if not field.Positions[to_buy_position.x][to_buy_position.y].IsOccupied() :
                    to_buy_positions.append(to_buy_position)
    else :
        newlist = getmostproductionCapabilityPositions()
        produced_positions[:] = []

        for newpos in reversed(newlist):
            produced_positions.append(newpos)
        i = 0
        count = 0
        step = 4

        low_filter = 3
        half = int(len(produced_positions)/4+1)
        for produced_position in produced_positions:
            if ( count/4 > half ):
                break

            if ( i > low_filter):
                lowPos = field.Positions[produced_position.x][produced_position.y]
                if (lowPos.expected_volume < 1):
                    break

            count +=addAvailablePositionToBuyPosition( Action(ActionType.BUY,(produced_position.x - step)%field.width, (produced_position. y - step)%field.height))
            count +=addAvailablePositionToBuyPosition( Action(ActionType.BUY,(produced_position.x -step)%field.width, (produced_position. y + step)%field.height))
            count +=addAvailablePositionToBuyPosition( Action(ActionType.BUY,(produced_position.x +step)%field.width, (produced_position. y - step)%field.height))
            count +=addAvailablePositionToBuyPosition( Action(ActionType.BUY,(produced_position.x + step)%field.width, (produced_position. y + step)%field.height))
            i = i +1


    print ("put "  + str(len(to_buy_positions)) + " into queue")
    pass

def getmostproductionCapabilityPositions():
    return sorted( produced_positions, key=productionCapability)

def productionCapability(position):
    positionInField =  field.Positions[position.x][position.y]
    return positionInField.expected_volume

def addAvailablePositionToBuyPosition(to_buy_position) :
    position =  field.Positions[to_buy_position.x][to_buy_position.y]
    if position.IsAvailable():
        to_buy_positions.append(position)
        return 1
    else:
        position =  field.Positions[(to_buy_position.x)%field.width ][(to_buy_position.y)%field.height]
        if position.IsAvailable():
            to_buy_positions.append(position)
            return 1

    return 0
    pass

algorithm = ComplexAlogrithm()
to_buy_positions = []
produced_positions = []
to_buy_positions_generation = 0