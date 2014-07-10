from worldcup.domain_s2.action import *
from worldcup.domain_s2.cell import CellState


class State:
    def __init__(self, block_map):
        self.block_map = block_map

    def next_action(self):
        pass


class Null(State):
    def __init__(self, block_map):
        super().__init__(block_map)

    def next_action(self):
        cell = self._buy_at()
        return Action(ActionType.BUY, cell.x, cell.y)

    def _buy_at(self):
        block = self.block_map.get_random_block()
        return block.center()


class Occupied(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        self.block_map.occupy_by_other(self.x, self.y)
        return Null(self.block_map).next_action()


class Owned(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        cell = self.block_map.find_cell(self.x, self.y)
        cell.state = CellState.OWNED
        return Action(ActionType.EXPLORE, cell.x, cell.y)