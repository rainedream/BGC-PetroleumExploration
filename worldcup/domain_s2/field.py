from worldcup.domain_s2.cell import Cell


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = Field.build_cells(width, height)

    @staticmethod
    def build_cells(width, height):
        cells = [[0 for x in range(height)] for x in range(width)]
        for i in range(0, width):
            for j in range(0, height):
                cells[i][j] = Cell(i, j)
        return cells

    def find_cell(self, x, y):
        return self.cells[x][y]
