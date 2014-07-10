
def enum(**enums):
    return type('Enum', (), enums)
CellState = enum(NULL=0, OWNED=1, EXPLORED=2, PRODUCTION=3, STIMULATED=4, STOPPED=-1)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = CellState.NULL
        self.total_production = 0
        self.volume_on_this_round = 0
