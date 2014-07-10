from worldcup.domain_s2.cell import Cell


class Field:
    def __init__(self, width, height):
        self.cells = Field.build_cells(width, height)

    @staticmethod
    def build_cells(width, height):
        cells = []
        for i in range(0, width):
            for j in range(0, height):
                cells.append(Cell(i, j))
        return cells

    def find_cell(self, x, y):
        pass
