from worldcup.domain.Cost import *
from worldcup.domain.position import Position


class Field:
    def __init__(self):
        self._inited = False

    def InitField(self, x,y):
        self._inited = True

        self.Positions = []
        for i in range (0, x):
            new = []
            for j in range (0, y):
                new.append(Position(i,j))
            self.Positions.append(new)

        pass

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