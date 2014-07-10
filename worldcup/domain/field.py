from worldcup.domain.position import Position


class Field:
    def __init__(self):
        self._inited = False

    def at(self, x, y):
        return Position()

    def InitField(self, x,y):
        self._inited = True
        self.Positions = []
        self.Positions = [[Position(x,y) for x in range(x)] for y in range(y)]

    def IsInited(self):
        return self._inited

    def UpdatePositionStatus(self, x, y, newStatus):
        position = self.Positions[x][y]
        position.UpdateStatusf(newStatus)

    def UpdateProduction(self, productionSummary):
        for item in productionSummary:
            position = self.Positions[item.x][item.y]
            position.UpdateProduction(item.productionVolume)
        pass

    def GetUnProfitPositions(self):
        for position in self.Positions:
            if ( position.IsUnderProfit()):
                list.append(position)

        return list

    def GetExploredPositions(self):
        for position in self.Positions:
            if ( position.IsExplored()):
                list.append(position)

        return

    def GetPurchaedPositions(self):
        for position in self.Positions:
            if ( position.IsPurchased()):
                list.append(position)

        return list

    def GetAvailablePositions(self):
        for position in self.Positions:
            if ( position.IsAvailable()):
                list.append(position)

        return list

field = Field()