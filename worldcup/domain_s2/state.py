from worldcup.domain_s2.action import *
from worldcup.domain_s2.cell import CellState
from worldcup.domain_s2.cost import *
from worldcup.domain_s2.protential_cell import ProtentialCellList, CELL_NEIGHBOR_DISTANCE
from worldcup.handlers.depleted import DepletedCellList


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
        if cell and not self.block_map.near_to_production_cell(cell, 2 * CELL_NEIGHBOR_DISTANCE):
            return Action(ActionType.BUY, cell.x, cell.y)
        else:
            return Action(ActionType.STOP, -1, -1)

    def _buy_at(self):
        block = self.block_map.get_random_block()
        if not block:
            return None
        return block.center()


class Occupied(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        self.block_map.occupy_by_other(self.x, self.y)
        return SurroundingProduction(self.block_map).next_action()


class Owned(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        cell = self.block_map.find_cell(self.x, self.y)
        cell.state = CellState.OWNED
        return Action(ActionType.EXPLORE, cell.x, cell.y)


class Explored(State):
    def __init__(self, block_map, x, y, estimated_reserve):
        super().__init__(block_map)
        self.x = x
        self.y = y
        self.estimated_reserve = estimated_reserve

    def next_action(self):
        cell = self.block_map.find_cell(self.x, self.y)
        cell.state = CellState.EXPLORED
        if self.is_worth_to_drill():
            return Action(ActionType.DRILL, cell.x, cell.y)
        else:
            return Occupied(self.block_map, cell.x, cell.y).next_action()

    def is_worth_to_drill(self):
        return (9 * self.estimated_reserve * OIL_UNIT_PRICE) > COST_OF_SERVICE_DRILL_SLB


class Production(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        cell = self.block_map.find_cell(self.x, self.y)
        cell.state = CellState.PRODUCTION
        ProtentialCellList(self.block_map, cell)
        return SurroundingProduction(self.block_map).next_action()


class Depleted(State):
    def __init__(self, block_map, depleted_cell):
        super().__init__(block_map)
        self.x = depleted_cell.x
        self.y = depleted_cell.y

    def next_action(self):
        return Action(ActionType.STOP, self.x, self.y)


class Stopped(State):
    def __init__(self, block_map, production_params, x, y):
        super().__init__(block_map)
        self.production_params = production_params
        self.x = x
        self.y = y

    def next_action(self):
        cell = self.block_map.find_cell(self.x, self.y)
        cell.state = CellState.STOPPED
        depleted_cells = DepletedCellList(self.block_map, self.production_params)
        if len(depleted_cells) > 0:
            return Depleted(self.block_map, depleted_cells.pop()).next_action()
        else:
            return SurroundingProduction(self.block_map).next_action()


class SurroundingProduction(State):
    def __init__(self, block_map):
        super().__init__(block_map)

    def next_action(self):
        if ProtentialCellList.has_cell():
            popped_cell = ProtentialCellList.pop()
            return Action(ActionType.BUY, popped_cell.x, popped_cell.y)
        else:
            return Null(self.block_map).next_action()


class Stimulated(State):
    def __init__(self, block_map, x, y):
        super().__init__(block_map)
        self.x = x
        self.y = y

    def next_action(self):
        return Action(ActionType.STIMULATE, self.x, self.y)