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

    def Update(self, x, y, newStatus):
        pass
        pass


field = Field()