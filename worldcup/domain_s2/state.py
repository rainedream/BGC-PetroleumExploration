from worldcup.domain_s2.action import *


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

