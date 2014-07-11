from worldcup.domain_s2.cell import CellState
from worldcup.domain_s2.cost import *


class DepletedCellList:
    cells = []

    def __init__(self, block_map, production_params):
        self.block_map = block_map
        if len(DepletedCellList.cells) == 0:
            DepletedCellList.cells = self._sort_by_depletion(self._find_depleted_cells(production_params))

    def __len__(self):
        return len(DepletedCellList.cells)

    def pop(self):
        if len(DepletedCellList.cells) == 0:
            return None
        first_cell = DepletedCellList.cells[0]
        del DepletedCellList.cells[0]
        return first_cell

    @staticmethod
    def add(cell):
        DepletedCellList.cells.append(cell)

    def _find_depleted_cells(self, production_params):
        cells = []
        for production_param in production_params:
            cell = self.block_map.find_cell(production_param.x, production_param.y)
            if cell.state != CellState.PRODUCTION:
                continue
            cell.volume_on_this_round = production_param.volume - cell.total_production
            # cell.total_production = production_param.volume
            if self._is_worth_to_produce(cell.volume_on_this_round):
                continue
            cells.append(cell)
        return cells

    def _is_worth_to_produce(self, volume_this_round):
        return volume_this_round * OIL_UNIT_PRICE > 2 * COST_OF_PRODUCTION

    def _volume_on_this_round(self, cell):
        return cell.volume_on_this_round

    def _sort_by_depletion(self, cell_list):
        return sorted(cell_list, key=self._volume_on_this_round)



