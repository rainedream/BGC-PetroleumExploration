import random
from worldcup.domain_s2.cell import CellState


BLOCK_WIDTH = 7


class BlockMap:
    def __init__(self, field):
        self.field = field
        self._new()

    def create_blocks(self, field):
        x_count = field.width // self.block_width
        y_count = field.height // self.block_width
        blocks = []
        for i in range(0, x_count):
            for j in range(0, y_count):
                blocks.append(Block(field, i * self.block_width, j * self.block_width))
        return blocks

    def build_unused_block_indexes(self):
        indexes = []
        for i in range(0, len(self.blocks)):
            indexes.append(i)
        return indexes

    def get_random_block(self):
        if len(self.block_candidate_indexes) == 0:
            return None
        index = random.randint(0, len(self.block_candidate_indexes) - 1)
        candidate = self.blocks[self.block_candidate_indexes[index]]
        del self.block_candidate_indexes[index]
        return candidate

    def occupy_by_other(self, x, y):
        occupied_at = y // self.block_width * self.x_count + x // self.block_width
        if occupied_at in self.block_candidate_indexes:
            self.block_candidate_indexes.remove(occupied_at)

    def find_cell(self, x, y):
        return self.field.find_cell(x, y)

    def is_in_field(self, x, y):
        return 0 <= x < self.field.width and 0 <= y < self.field.height

    def near_to_production_cell(self, cell, distance):
        for x_offset in range(-distance + 1, distance):
            for y_offset in range(-distance + 1, distance):
                x = cell.x + x_offset
                y = cell.y + y_offset
                if not self.is_in_field(x, y):
                    continue
                neighbour = self.find_cell(x, y)
                if neighbour.state == CellState.PRODUCTION or neighbour.state == CellState.STOPPED:
                    return True
        return False


    def _new(self, expected_block_width=BLOCK_WIDTH):
        self.block_width = expected_block_width
        self.x_count = self.field.width // self.block_width
        self.blocks = self.create_blocks(self.field)
        self.block_candidate_indexes = self.build_unused_block_indexes()

    # def shrink_to_half(self):
    #     self._new(self.block_width // 2)


class Block:
    def __init__(self, field, start_x, start_y):
        self.field = field
        self.start_x = start_x
        self.start_y = start_y

    def center(self):
        x = self.start_x + BLOCK_WIDTH // 2
        y = self.start_y + BLOCK_WIDTH // 2
        return self.field.find_cell(x, y)

