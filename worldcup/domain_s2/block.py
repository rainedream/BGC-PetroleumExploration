import random


BLOCK_WIDTH = 10


class BlockMap:
    def __init__(self, field):
        self.field = field
        self.x_count = self.field.width // BLOCK_WIDTH
        self.blocks = BlockMap.create_blocks(self.field)
        self.block_candidate_indexes = self.build_unused_block_indexes()

    @staticmethod
    def create_blocks(field):
        x_count = field.width // BLOCK_WIDTH
        y_count = field.height // BLOCK_WIDTH
        blocks = []
        for i in range(0, x_count):
            for j in range(0, y_count):
                blocks.append(Block(field, i * BLOCK_WIDTH, j * BLOCK_WIDTH))
        return blocks

    def build_unused_block_indexes(self):
        indexes = []
        for i in range(0, len(self.blocks)):
            indexes.append(i)
        return indexes

    def get_random_block(self):
        index = random.randint(0, len(self.block_candidate_indexes) - 1)
        candidate = self.blocks[self.block_candidate_indexes[index]]
        del self.block_candidate_indexes[index]
        return candidate

    def occupy_by_other(self, x, y):
        occupied_at = y // BLOCK_WIDTH * self.x_count + x // BLOCK_WIDTH
        if occupied_at in self.block_candidate_indexes:
            self.block_candidate_indexes.remove(occupied_at)

    def find_cell(self, x, y):
        return self.field.find_cell(x, y)


class Block:
    def __init__(self, field, start_x, start_y):
        self.field = field
        self.start_x = start_x
        self.start_y = start_y

    def center(self):
        x = self.start_x + BLOCK_WIDTH // 2
        y = self.start_y + BLOCK_WIDTH // 2
        return self.field.find_cell(x, y)

