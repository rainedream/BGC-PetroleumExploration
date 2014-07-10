from worldcup.domain_s2.block import BLOCK_WIDTH


CELL_NEIGHBOR_DISTANCE = 3

class ProtentialCellList:
    cells = []

    def __init__(self, block_map, center_cell):
        self.block_map = block_map
        ProtentialCellList.cells.extend(self._find_surrounded_cells(center_cell.x, center_cell.y))

    @staticmethod
    def has_cell():
        return len(ProtentialCellList.cells) > 0

    @staticmethod
    def pop():
        if not ProtentialCellList.has_cell():
            return None
        first = ProtentialCellList.cells[0]
        del ProtentialCellList.cells[0]
        return first

    def _find_surrounded_cells(self, x, y):
        step = BLOCK_WIDTH // 2
        cells = []
        self._try_to_append_cell(cells, x - step, y - step)
        self._try_to_append_cell(cells, x - step, y + step)
        self._try_to_append_cell(cells, x + step, y - step)
        self._try_to_append_cell(cells, x + step, y + step)
        return cells

    def _try_to_append_cell(self, cell_list, x, y):
        if not self.block_map.is_in_field(x, y):
            return
        if self._near_to_protential_cell(x, y):
            return
        cell = self.block_map.find_cell(x, y)
        if self.block_map.near_to_production_cell(cell, CELL_NEIGHBOR_DISTANCE):
            return
        cell_list.append(cell)

    def _near_to_protential_cell(self, x, y):
        for cell in ProtentialCellList.cells:
            if cell.x - CELL_NEIGHBOR_DISTANCE < x < cell.x + CELL_NEIGHBOR_DISTANCE \
                    and cell.y - CELL_NEIGHBOR_DISTANCE < y < cell.y + CELL_NEIGHBOR_DISTANCE:
                return True
        return False

    
