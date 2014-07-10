BLOCK_WIDTH = 10

class BlockMap:
    def __init__(self, field):
        self.blocks = BlockMap.create_blocks(field)

    @staticmethod
    def create_blocks(field):
        x_count = field.width // BLOCK_WIDTH
        y_count = field.height // BLOCK_WIDTH
        blocks = []
        for i in range(0, x_count):
            for j in range(0, y_count):
                blocks.append(Block(i * BLOCK_WIDTH, j * BLOCK_WIDTH))
        return blocks


class Block:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

