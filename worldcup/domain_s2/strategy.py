from worldcup.domain_s2.state import Null


class RandomExploration:
    def __init__(self, block_map):
        self.block_map = block_map

    def do(self):
        last_operation = Null(self.block_map)
        return last_operation.next_action()