from worldcup.domain_s2.state import *
from worldcup.handlers.depleted import DepletedCellList


class RandomExploration:
    lastAction = None
    peakMoney = 0
    
    def __init__(self, block_map, round, money):
        self.block_map = block_map
        self.should_stop_waste = False
        if money >= RandomExploration.peakMoney:
            RandomExploration.peakMoney = money
        else:
            self.should_stop_waste = (money / RandomExploration.peakMoney < 0.8) and round > 100

    def do(self, last_operation_status, last_operation_value, production_params):
        if not last_operation_status:
            current_state = Null(self.block_map)
        else:
            current_state = self._recover_state(RandomExploration.lastAction, parse_to_bool(last_operation_status), last_operation_value, production_params)
            self._update_cell_total_production(production_params)
        RandomExploration.lastAction = current_state.next_action()
        return RandomExploration.lastAction

    @staticmethod
    def reset():
        RandomExploration.lastAction = None
        RandomExploration.peakMoney = 0

    def _recover_state(self, last_action, is_last_action_success, last_operation_value, production_params):
        if last_action.type == ActionType.STOP:
            if is_last_action_success:
                return Stopped(self.block_map, production_params, last_action.x, last_action.y)
            else:
                DepletedCellList.add(self.block_map.find_cell(last_action.x, last_action.y))
        else:
            depleted_cells = DepletedCellList(self.block_map, production_params)
            if len(depleted_cells) > 0:
                return Depleted(self.block_map, depleted_cells.pop())

        if self.should_stop_waste:
            depleted_cells = DepletedCellList(self.block_map, production_params)
            if len(depleted_cells) > 0:
                return Depleted(self.block_map, depleted_cells.pop())
            else:
                return DoNothing(self.block_map)

        if last_action.type == ActionType.BUY:
            if is_last_action_success:
                return Owned(self.block_map, last_action.x, last_action.y)
            else:
                return Occupied(self.block_map, last_action.x, last_action.y)
        elif last_action.type == ActionType.EXPLORE:
            if is_last_action_success:
                return Explored(self.block_map, last_action.x, last_action.y, float(last_operation_value))
        elif last_action.type == ActionType.DRILL:
            if is_last_action_success:
                if self._need_to_stimulate(float(last_operation_value)):
                    return Stimulated(self.block_map, last_action.x, last_action.y)
                else:
                    return Production(self.block_map, last_action.x, last_action.y)
        elif last_action.type == ActionType.STIMULATE:
            if is_last_action_success:
                return Production(self.block_map, last_action.x, last_action.y)

        return SurroundingProduction(self.block_map)

    def _update_cell_total_production(self, production_params):
        for production_param in production_params:
            cell = self.block_map.find_cell(production_param.x, production_param.y)
            if cell.state < CellState.OWNED:
                continue
            cell.total_production = production_param.volume

    def _need_to_stimulate(self, expected_reserve):
        return expected_reserve >= 7


def parse_to_bool(text):
    if text.lower() == 'true':
        return True
    return False