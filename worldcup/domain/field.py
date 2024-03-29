from worldcup.domain.Cost import *
from worldcup.domain.position import Position


class Field:
    def __init__(self):
        self._inited = False

    def InitField(self, x,y):
        self._inited = True
        self.width = x
        self.height = y
        self.maxMoney = NODE_INITIAL_MONEY
        self.currentMoney = NODE_INITIAL_MONEY
        self.round = 0

        self.Positions = []
        for i in range (0, x):
            new = []
            for j in range (0, y):
                new.append(Position(i,j))
            self.Positions.append(new)

        pass

    def UpdateMoneyAndRound(self, newMoney, round):
        if  newMoney > self.maxMoney:
            self.maxMoney = newMoney

        self.round = round
        self.currentMoney = newMoney

    def CanSpendMoney(self):
        if self.round < 30 :
            return True
        elif self.round < 100 :
            return self.currentMoney/ self.maxMoney > 0.7
        else:
            return  self.currentMoney/ self.maxMoney > 0.9

    def IsInited(self):
        return self._inited

    def UpdatePositionStatus(self, x, y, lastOperation, lastOperationStatus, value):
        position = self.Positions[x][y]
        position.UpdateStatus(lastOperation, lastOperationStatus, value)

    def UpdateProduction(self, productionSummary):
        for item in productionSummary:
            position = self.Positions[item.x][item.y]
            position.UpdateProduction(item.productionVolume)
        pass

    def GetUnProfitPositions(self):
        # for position in self.Positions:
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsBelowProfit():
                    list.append(position)

        return list

    def GetUnProfitPositionsProActive(self):
        # for position in self.Positions:
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsBelowProfitProactive():
                    list.append(position)

        return list

    def GetExploredPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsExplored():
                    list.append(position)
        return list

    def GetValuableExploredPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsExplored() and position.expected_volume * OIL_UNIT_PRICE> COST_OF_SERVICE_DRILL_SLB:
                    list.append(position)
        return list

    def GetComplexValuableExploredPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsExplored():
                    if position.expected_volume * OIL_UNIT_PRICE * 0.4 > COST_OF_SERVICE_DRILL_SLB + COST_OF_PRODUCTION * 10:
                        list.append(position)
        return list

    def GetMoreComplexValuableExploredPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsExplored():
                    if position.expected_volume > 0:
                        list.append(position)
        return list

    def GetSuperPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsDrilling() and ( not position.IsStimulated()):
                    if position.expected_volume >= 7:
                        list.append(position)
        return list

    def GetSuperPositionsForNewPosition(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsDrilling():
                    if position.expected_volume >= 7:
                        list.append(position)
        return list

    def GetNextSuperDrillPositionForBuy(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsStimulated():
                    #if position.expected_volume >= 7:
                    if position.BuyAroundDirectly > 0:
                        list.append(position)

        step = 4
        for position in list :
            newPos = field.Positions[(position.x -step)%field.width][(position.y -step)%field.height]

            if newPos.IsAvailable() :
                position.BuyAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x -step)%field.width][(position.y + step)%field.height]

            if newPos.IsAvailable() :
                position.BuyAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x + step)%field.width][(position.y - step)%field.height]

            if newPos.IsAvailable() :
                position.BuyAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x + step)%field.width][(position.y +  step)%field.height]

            if newPos.IsAvailable() :
                position.BuyAroundDirectly -= 1
                return newPos

        return None

    def GetNextSuperDrillPositionForDrill(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsStimulated():
                    #if position.expected_volume >= 7:
                    if position.DrillAroundDirectly > 0:
                        list.append(position)

        step = 4
        for position in list :
            newPos = field.Positions[(position.x -step)%field.width][(position.y -step)%field.height]

            if newPos.IsPurchased() :
                position.DrillAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x -step)%field.width][(position.y + step)%field.height]

            if newPos.IsPurchased() :
                position.DrillAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x + step)%field.width][(position.y - step)%field.height]

            if newPos.IsPurchased() :
                position.DrillAroundDirectly -= 1
                return newPos

            newPos = field.Positions[(position.x + step)%field.width][(position.y +  step)%field.height]

            if newPos.IsPurchased() :
                position.DrillAroundDirectly -= 1
                return newPos
        return None

    def GetPurchaedPositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsPurchased():
                    list.append(position)

        return list

    def GetAvailablePositions(self):
        list = []
        for i in range(0, len(self.Positions)):
            for j in range(0, len(self.Positions[i])):
                position = self.Positions[i][j]
                if position.IsAvailable():
                    list.append(position)

        return list

field = Field()